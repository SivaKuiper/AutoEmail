# 📧 KEIPL EMAIL AUTOMATION - RENDER DEPLOYMENT FIX

## ❌ YOUR ERROR:
```
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```

## ✅ THE PROBLEM:
Render expects files in the **ROOT** directory, not in a subfolder.

---

## 🔧 SOLUTION - TWO OPTIONS:

### **OPTION A: GitHub Repository** ⭐ **RECOMMENDED**

1. **Create GitHub Repository:**
   ```
   - Go to github.com
   - Create new repository: "keipl-email-automation"
   - Make it private
   ```

2. **Upload Files (in ROOT, not subfolder):**
   ```
   keipl-email-automation/
   ├── requirements.txt          ← ROOT level!
   ├── .env.example
   ├── email_sender.py
   ├── supabase_client.py
   ├── email_templates.py
   ├── daily_reports.py
   └── README.md
   ```

3. **Deploy on Render:**
   ```
   - Go to render.com
   - New Web Service
   - Connect GitHub repository
   - Build Command: pip install -r requirements.txt
   - Start Command: python daily_reports.py
   - Add environment variables (see below)
   ```

---

### **OPTION B: Direct Upload** (If no GitHub)

1. **Download all files from email_automation folder**

2. **Upload to Render as ZIP:**
   ```
   - Make sure files are in ROOT of ZIP, not in subfolder
   - Correct structure:
     email-automation.zip
     ├── requirements.txt        ← At top level!
     ├── email_sender.py
     └── ...
   
   - WRONG structure:
     email-automation.zip
     └── email_automation/       ← Don't nest!
         ├── requirements.txt
         └── ...
   ```

3. **Configure Render:**
   ```
   Build Command: pip install -r requirements.txt
   Start Command: python daily_reports.py
   ```

---

## 🔑 ENVIRONMENT VARIABLES (Add in Render Dashboard):

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key

GMAIL_EMAIL=your-factory-email@gmail.com
GMAIL_APP_PASSWORD=your_16_char_app_password

PARTNER_EMAILS=partner1@email.com,partner2@email.com
ADMIN_EMAIL=your-email@gmail.com
```

**How to add in Render:**
1. After creating web service
2. Go to "Environment" tab
3. Click "Add Environment Variable"
4. Add each variable above

---

## 📋 FILES INCLUDED:

1. **requirements.txt** - Python dependencies
2. **email_sender.py** - Gmail SMTP email sending
3. **supabase_client.py** - Database connection
4. **email_templates.py** - HTML email templates
5. **daily_reports.py** - Main automation script
6. **.env.example** - Configuration template

---

## ✅ QUICK TEST BEFORE DEPLOYING:

Test locally first:

```bash
# 1. Create .env file (copy from .env.example)
# Fill in your credentials

# 2. Install dependencies
pip install -r requirements.txt

# 3. Test Supabase connection
python supabase_client.py

# 4. Test email sending
python email_sender.py

# 5. Test daily report
python -c "from daily_reports import send_daily_report; send_daily_report()"

# If all tests pass, deploy to Render!
```

---

## 🚀 DEPLOYMENT CHECKLIST:

- [ ] Files in ROOT directory (not subfolder)
- [ ] requirements.txt accessible
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `python daily_reports.py`
- [ ] All environment variables added
- [ ] Gmail app password created
- [ ] Test email received

---

## 📧 WHAT HAPPENS AFTER DEPLOYMENT:

Once deployed successfully:

1. Service runs 24/7 on Render (FREE tier)
2. Every day at 8:00 AM IST:
   - Fetches inventory from Supabase
   - Generates professional HTML email
   - Sends to all partners automatically
3. Every Monday at 9:00 AM IST:
   - Sends weekly summary to admin

**You'll receive first email tomorrow at 8 AM!** 📧

---

## 🐛 TROUBLESHOOTING:

**Build Failed - Can't find requirements.txt:**
```
Fix: Make sure files are in ROOT, not in subfolder
Check: requirements.txt should be at top level of repo
```

**Build Failed - Module not found:**
```
Fix: Check requirements.txt is spelled correctly
     Make sure all dependencies listed
```

**Service Crashes - Email not sent:**
```
Fix: Check environment variables are set correctly
     Test Gmail credentials
     Check Supabase URL and key
```

**Emails not received:**
```
Fix: Check spam/junk folder
     Verify Gmail app password (16 chars, no spaces)
     Check partner emails are correct
```

---

## 💰 COST:

```
Render Free Tier:
✅ FREE forever for this use case
✅ 750 hours/month (enough for 24/7)
✅ Auto-sleeps after 15 min inactivity
✅ Wakes up on scheduled time
```

---

## 📞 NEED HELP?

Common issues:

1. **"Build failed - requirements.txt not found"**
   → Files in subfolder, move to root

2. **"Login failed - authentication error"**
   → Wrong Gmail app password, regenerate

3. **"No module named supabase"**
   → requirements.txt not installed, check build command

---

**Follow these steps and deployment will succeed!** ✅
