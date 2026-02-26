import os
from dotenv import load_dotenv
import resend

load_dotenv()

def send_email(to_emails, subject, body_html):
    """Send email via Resend API - Testing mode (only verified email)"""
    
    resend_api_key = os.getenv('RESEND_API_KEY')
    
    if not resend_api_key:
        print("❌ Resend API key not configured")
        return False
    
    # Set API key
    resend.api_key = resend_api_key
    
    try:
        # TEMPORARY: Only send to verified email until domain is verified
        # This avoids the Resend testing restriction
        verified_email = "siva.dubai@gmail.com"
        
        # Send email only to verified email (ignore other recipients for now)
        params = {
            "from": "Kriya Granite <onboarding@resend.dev>",
            "to": [verified_email],
            "subject": subject,
            "html": body_html,
        }
        
        # Send email
        response = resend.Emails.send(params)
        
        print(f"✅ Email sent: {subject}")
        print(f"   TO: {verified_email}")
        print(f"   Email ID: {response['id']}")
        print(f"   Note: Only sending to verified email until domain is verified")
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
            <h1 style="color: #00e676; margin: 0;">✅ Test Email from Kriya Granite</h1>
            <p style="font-size: 16px; color: #333; margin-top: 20px;">
                Email automation is working! You will receive daily reports at 9 PM IST.
            </p>
            <p style="font-size: 14px; color: #666; margin-top: 20px;">
                Note: Currently sending only to verified email. After domain verification, 
                all partners will receive emails automatically.
            </p>
            <p style="font-size: 14px; color: #666; margin-top: 20px;">
                — Kriya Granite Inventory System
            </p>
        </div>
    </body>
    </html>
    """
    
    print("Testing email to verified address...")
    send_email(["siva.dubai@gmail.com"], "Kriya Granite - Test Email", test_html)
    print("✅ Check siva.dubai@gmail.com inbox!")
