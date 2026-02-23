import schedule
import time
from datetime import datetime
from supabase_client import get_available_inventory, get_sales_today, get_sales_this_week
from email_templates import daily_report_html
from email_sender import send_email
import os
from dotenv import load_dotenv
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

load_dotenv()

# Simple HTTP server to keep Railway awake
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>KEIPL Email Automation Running</h1><p>Status: Active</p>')
    
    def log_message(self, format, *args):
        pass  # Suppress HTTP logs

def run_health_server():
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    print(f"   Health check server running on port {port}")
    server.serve_forever()

def send_daily_report():
    """Send daily inventory report at 9 PM IST"""
    print(f"🔄 Generating daily report at {datetime.now()}")
    
    try:
        inventory = get_available_inventory()
        sales = get_sales_today()
        
        print(f"   Found {len(inventory)} available slabs")
        print(f"   Found {len(sales)} sales today")
        
        subject = f"KEIPL Daily Report - {datetime.now().strftime('%d %b %Y')}"
        body = daily_report_html(inventory, sales)
        
        partner_emails_str = os.getenv('PARTNER_EMAILS', '')
        if not partner_emails_str:
            print("❌ No partner emails configured")
            return
            
        partner_emails = [e.strip() for e in partner_emails_str.split(',')]
        
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
        inventory = get_available_inventory()
        sales = get_sales_this_week()
        
        print(f"   Found {len(inventory)} available slabs")
        print(f"   Found {len(sales)} sales this week")
        
        subject = f"KEIPL Weekly Summary - Week of {datetime.now().strftime('%d %b %Y')}"
        body = daily_report_html(inventory, sales)
        
        admin_email = os.getenv('ADMIN_EMAIL')
        if not admin_email:
            print("❌ No admin email configured")
            return
        
        send_email([admin_email], subject, body)
        
        print(f"✅ Weekly summary sent to {admin_email}")
        
    except Exception as e:
        print(f"❌ Error generating weekly summary: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 KEIPL Email Automation Service")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Start health check server in background thread
    health_thread = Thread(target=run_health_server, daemon=True)
    health_thread.start()
    
    # Schedule jobs
    schedule.every().day.at("21:00").do(send_daily_report)
    schedule.every().monday.at("08:00").do(send_weekly_summary)
    
    print("✅ Scheduled:")
    print("   • Daily report: Every day at 9:00 PM IST")
    print("   • Weekly summary: Every Monday at 8:00 AM IST")
    print()
    print("📧 Email automation is running...")
    print("   Press Ctrl+C to stop")
    print("=" * 50)
    print()
    
    # Run continuously
    while True:
        schedule.run_pending()
        time.sleep(60)
