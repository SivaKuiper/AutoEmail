import smtplib
import os
import ssl  # New import for security
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_emails, subject, html_content):
    """Sends email using Gmail SMTP via SSL (Port 465)"""
    smtp_server = "smtp.gmail.com"
    smtp_port = 465  # Switched from 587
    
    sender_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        msg = MIMEMultipart()
        msg['From'] = f"KEIPL Reports <{sender_email}>"
        msg['To'] = ", ".join(to_emails) 
        msg['Subject'] = subject
        msg.attach(MIMEText(html_content, 'html'))

        # Connect using SMTP_SSL for Port 465
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, to_emails, msg.as_string())
        
        return True
    except Exception as e:
        print(f"❌ Gmail Send Error: {e}")
        return False
