import schedule
import time
from datetime import datetime
from supabase_client import get_available_inventory, get_sales_today, get_sales_this_week
from email_templates import daily_report_html
from email_sender import send_email
import os
from dotenv import load_dotenv

load_dotenv()

def send_daily_report():
    """Send daily inventory report at 9 PM IST"""
    print(f"🔄 Generating daily report at {datetime.now()}")
    
    try:
        # Fetch data
        inventory = get_available_inventory()
        sales = get_sales_today()
        
        print(f"   Found {len(inventory)} available slabs")
        print(f"   Found {len(sales)} sales today")
        
        # Generate email
        subject = f"FACTORY Daily Inventory Report - {datetime.now().strftime('%d %b %Y')}"
        body = daily_report_html(inventory, sales)
        
        # Get partner emails
        partner_emails_str = os.getenv('PARTNER_EMAILS', '')
        if not partner_emails_str:
            print("❌ No partner emails configured")
            return
            
        partner_emails = [e.strip() for e in partner_emails_str.split(',')]
        
        # Send email
        success = send_email(partner_emails, subject, body)
        
        if success:
            print(f"✅ Daily report sent to {len(partner_emails)} partners")
        else:
            print(f"❌ Failed to send daily report")
            
    except Exception as e:
        print(f"❌ Error generating daily report: {e}")
        import traceback
        traceback.print_exc()

def send_weekly_summary():
    """Send weekly summary on Monday 8 AM IST"""
    print(f"🔄 Generating weekly summary at {datetime.now()}")
    
    try:
        # Fetch data
        inventory = get_available_inventory()
        sales = get_sales_this_week()
        
        print(f"   Found {len(inventory)} available slabs")
        print(f"   Found {len(sales)} sales this week")
        
        # Generate email
        subject = f"FACTORY Weekly Summary - Week of {datetime.now().strftime('%d %b %Y')}"
        body = daily_report_html(inventory, sales)
        
        # Get admin email
        admin_email = os.getenv('ADMIN_EMAIL')
        if not admin_email:
            print("❌ No admin email configured")
            return
        
        # Send email
        send_email([admin_email], subject, body)
        
        print(f"✅ Weekly summary sent to {admin_email}")
        
    except Exception as e:
        print(f"❌ Error generating weekly summary: {e}")
        import traceback
        traceback.print_exc()

# --- MAIN EXECUTION BLOCK ---
# All lines below must have ZERO spaces at the very beginning
if __name__ == "__main__":
    print("=" * 50)
    print("🚀 KEIPL Email Automation Service")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # TRIGGER TEST IMMEDIATELY ON STARTUP
    print("🧪 Running immediate test send...")
    send_daily_report()
    
    # Schedule future jobs
    schedule.every().day.at("21:00").do(send_daily_report)
    schedule.every().monday.at("08:00").do(send_weekly_summary)
    
    print("✅ Scheduled:")
    print("   • Daily report: Every day at 9:00 PM IST")
    print("   • Weekly summary: Every Monday at 8:00 AM IST")
    print()
    print("📧 Email automation is running...")
    print("   Press Ctrl+C to stop")
    print("=" * 50)
    
    while True:
        schedule.run_pending()
        time.sleep(60)
