import os
from dotenv import load_dotenv
import resend

load_dotenv()

def send_email(to_emails, subject, body_html):
    """Send email via Resend API with BCC support"""
    
    resend_api_key = os.getenv('RESEND_API_KEY')
    
    if not resend_api_key:
        print("❌ Resend API key not configured")
        return False
    
    # Set API key
    resend.api_key = resend_api_key
    
    try:
        # Get partner emails from to_emails parameter
        if isinstance(to_emails, list):
            all_partners = to_emails
        else:
            all_partners = [to_emails]
        
        # Your verified email (must be kriyastones@gmail.com for now)
        verified_email = "kriyastones@gmail.com"
        
        # Separate verified email and BCC partners
        if verified_email in all_partners:
            # Use verified email as TO
            to_address = [verified_email]
            # Others as BCC
            bcc_partners = [e for e in all_partners if e != verified_email]
        else:
            # If verified email not in list, add it as TO and all others as BCC
            to_address = [verified_email]
            bcc_partners = all_partners
        
        # Build params
        params = {
            "from": "Kriya Granite <onboarding@resend.dev>",
            "to": to_address,
            "subject": subject,
            "html": body_html,
        }
        
        # Add BCC if there are other partners
        if bcc_partners:
            params["bcc"] = bcc_partners
        
        # Send email
        response = resend.Emails.send(params)
        
        print(f"✅ Email sent: {subject}")
        print(f"   TO: {', '.join(to_address)}")
        if bcc_partners:
            print(f"   BCC: {len(bcc_partners)} partner(s) - {', '.join(bcc_partners)}")
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
            <h1 style="color: #00e676; margin: 0;">✅ Test Email from Kriya Granite</h1>
            <p style="font-size: 16px; color: #333; margin-top: 20px;">
                If you receive this, Resend email with BCC is working perfectly!
            </p>
            <p style="font-size: 14px; color: #666; margin-top: 20px;">
                — Kriya Granite Inventory System
            </p>
        </div>
    </body>
    </html>
    """
    
    # Test with multiple emails
    test_emails = ["kriyastones@gmail.com", "siva@kuiperexportsandimportsprivatelimited.com"]
    print(f"Testing email to: {', '.join(test_emails)}...")
    send_email(test_emails, "Kriya Granite - Test Email with BCC", test_html)
    print("✅ Check all inboxes!")
