import os
from dotenv import load_dotenv
from email_sender import send_email

# Load your local .env file
load_dotenv()

def test_connection():
    print("🧪 Starting Email Test...")
    
    # Get your details from .env (or hardcode them here for a 1-time test)
    recipient = os.getenv('ADMIN_EMAIL')
    subject = "🚀 KEIPL System Test"
    body = "<h1>Test Successful!</h1><p>Your Railway script is now authorized to send emails via Gmail SMTP.</p>"

    if not recipient:
        print("❌ Error: ADMIN_EMAIL not found in .env file.")
        return

    print(f"Sending test email to: {recipient}...")
    success = send_email([recipient], subject, body)

    if success:
        print("✅ SUCCESS! Check your inbox (and Spam folder just in case).")
    else:
        print("❌ FAILED. Check your EMAIL_PASS (App Password) and EMAIL_USER.")

if __name__ == "__main__":
    test_connection()
