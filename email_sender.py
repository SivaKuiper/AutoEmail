import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email(to_emails, subject, html_content):
    """Sends email using Gmail SMTP instead of Resend"""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # These must match the names you set in Railway Variables
    sender_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')

    # Basic check to ensure credentials exist
    if not sender_email or not password:
        print("❌ Error: EMAIL_USER or EMAIL_PASS environment variables are missing.")
        return False

    try:
        # 1. Create the container (MIME message)
        msg = MIMEMultipart()
        msg['From'] = f"KEIPL Reports <{sender_email}>"
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject

        # 2. Attach the HTML content
        msg.attach(MIMEText(html_content, 'html'))

        # 3. Connect to Gmail's Server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure TLS
        
        # 4. Login and Send
        server.login(sender_email, password)
        server.sendmail(sender_email, to_emails, msg.as_string())
        server.quit()
        
        return True
    except Exception as e:
        print(f"❌ Failed to send email via Gmail: {e}")
        return False
