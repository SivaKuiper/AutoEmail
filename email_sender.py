import os
from dotenv import load_dotenv
import resend

load_dotenv()

def send_email(to_emails, subject, body_html):
    """Send email via Resend API"""
    
    resend_api_key = os.getenv('RESEND_API_KEY')
    
    if not resend_api_key:
        print("❌ Resend API key not configured")
        return False
    
    # Set API key
    resend.api_key = resend_api_key
    
    try:
        # Prepare recipients
        if isinstance(to_emails, list):
            recipients = to_emails
        else:
            recipients = [to_emails]
        
        # Send email using Resend's domain
        params = {
            "from": "KEIPL Granite <onboarding@resend.dev>",
            "to": recipients,
            "subject": subject,
            "html": body_html,
        }
        
        response = resend.Emails.send(params)
        
        print(f"✅ Email sent: {subject}")
        print(f"   Email ID: {response['id']}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

# Test function
if __name__ == "__main__":
    test_html = """
    <html>
    <body style="font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5;">
        <div style="max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px;">
            <h1 style="color: #00e676; margin: 0;">✅ Test Email from KEIPL</h1>
            <p style="font-size: 16px; color: #333; margin-top: 20px;">
                If you receive this, Resend email automation is working perfectly!
            </p>
            <p style="font-size: 14px; color: #666; margin-top: 20px;">
                — KEIPL Granite Inventory System
            </p>
        </div>
    </body>
    </html>
    """
    
    admin_email = os.getenv('ADMIN_EMAIL')
    if admin_email:
        print(f"Sending test email to {admin_email}...")
        send_email([admin_email], "KEIPL Test Email via Resend", test_html)
        print("✅ Check your inbox!")
    else:
        print("❌ ADMIN_EMAIL not set in .env file")
