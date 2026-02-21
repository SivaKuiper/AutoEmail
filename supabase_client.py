from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Supabase client (compatible with v2.9.0+)
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

def get_available_inventory():
    """Get all available (unsold) slabs"""
    
    # Get all slabs
    slabs_response = supabase.table('slabs').select('*').execute()
    slabs = slabs_response.data if slabs_response.data else []
    
    # Get all sales
    sales_response = supabase.table('sales').select('slab_id').execute()
    sold_slab_ids = [s['slab_id'] for s in (sales_response.data if sales_response.data else [])]
    
    # Filter available slabs
    available = [s for s in slabs if s['id'] not in sold_slab_ids]
    
    return available

def get_blocks_by_status(status='COMPLETED'):
    """Get blocks by status"""
    response = supabase.table('blocks').select('*').eq('status', status).execute()
    return response.data if response.data else []

def get_sales_today():
    """Get today's sales"""
    from datetime import datetime, timedelta
    
    today = datetime.now().date()
    response = supabase.table('sales').select('*').gte('created_at', today.isoformat()).execute()
    return response.data if response.data else []

def get_sales_this_week():
    """Get this week's sales"""
    from datetime import datetime, timedelta
    
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    response = supabase.table('sales').select('*').gte('created_at', week_start.isoformat()).execute()
    return response.data if response.data else []

# Test connection
if __name__ == "__main__":
    print("Testing Supabase connection...")
    try:
        inventory = get_available_inventory()
        print(f"✅ Connected! Found {len(inventory)} available slabs")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
