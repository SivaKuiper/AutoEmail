def send_email(to_emails, subject, body_html):
    """Send email via Resend API"""
    
    resend_api_key = os.getenv('RESEND_API_KEY')
    
    if not resend_api_key:
        print("❌ Resend API key not configured")
        return False
    
    resend.api_key = resend_api_key
    
    try:
        # Get partner emails from environment
        partner_emails_str = os.getenv('PARTNER_EMAILS', '')
        all_partners = [e.strip() for e in partner_emails_str.split(',')]
        
        # Your verified email (TO)
        verified_email = "kriyastones@gmail.com"
        
        # Other partners (BCC - they won't see each other)
        other_partners = [e for e in all_partners if e != verified_email]
        
        # Send email
        params = {
            "from": "Kriya Granite <onboarding@resend.dev>",
            "to": [verified_email],  # Your verified email
            "bcc": other_partners if other_partners else None,  # Others as BCC
            "subject": subject,
            "html": body_html,
        }
        
        # Remove bcc if empty
        if not params["bcc"]:
            del params["bcc"]
        
        response = resend.Emails.send(params)
        
        print(f"✅ Email sent: {subject}")
        print(f"   To: {verified_email}")
        if other_partners:
            print(f"   BCC: {len(other_partners)} partners")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False
```

**Then in Railway Variables:**
```
PARTNER_EMAILS = kriyastones@gmail.com,siva@kuiperexports.com,partner2@email.com
```

**Result:**
- ✅ You receive in inbox (TO)
- ✅ Partners receive as BCC (invisible to each other)
- ✅ Works immediately, no DNS needed!

**Downside:** 
- Partners see it's addressed to you, not them
- Slightly less professional

---

### **OPTION 3: Keep Current Setup** 💌 **SIMPLEST**

**Keep only your email:**
```
PARTNER_EMAILS = kriyastones@gmail.com
