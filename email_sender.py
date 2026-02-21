import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_emails, subject, body_html):
    """Send email via Gmail SMTP"""
    
    gmail_email = os.getenv('GMAIL_EMAIL')
    gmail_password = os.getenv('GMAIL_APP_PASSWORD')
    
    if not gmail_email or not gmail_password:
        print("❌ Gmail credentials not configured in .env file")
        return False
    
    # Create message
    msg = MIMEMultipart('alternative')
    msg['From'] = f"KEIPL Granite <{gmail_email}>"
    msg['To'] = ', '.join(to_emails) if isinstance(to_emails, list) else to_emails
    msg['Subject'] = subject
    
    # Attach HTML body
    html_part = MIMEText(body_html, 'html')
    msg.attach(html_part)
    
    try:
        # Connect to Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(gmail_email, gmail_password)
            server.send_message(msg)
        
        print(f"✅ Email sent: {subject}")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

# Test function
if __name__ == "__main__":
    test_html = """
    <html>
    <body>
        <h1>Test Email from KEIPL</h1>
        <p>If you receive this, email automation is working! ✅</p>
    </body>
    </html>
    """
    
    admin_email = os.getenv('ADMIN_EMAIL')
    if admin_email:
        send_email([admin_email], "KEIPL Test Email", test_html)
    else:
        print("❌ ADMIN_EMAIL not set in .env file")
