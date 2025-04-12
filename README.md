# Birthday_wisher_smtp


```markdown


This is a Python app that sends automatic birthday emails with personalized messages. All you need is a Gmail account and a list of birthdays in a CSV file. Never forget a birthday again!

---

## 💡 Features

- Sends a birthday wish automatically if today's date matches any in your CSV.
- Chooses a random birthday letter from a list of templates.
- Sends the message via your Gmail using SMTP.
- Handles dynamic replacement of names in the letter.
- Email login credentials are secured using environment variables.

---

## 🗂 Folder Structure

```
birthday-wisher/
│
├── main.py                  # The main Python script
├── birthdays.csv            # Birthday data in CSV format
├── letter_templates/        # Folder containing birthday message templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── README.md                # You're reading this!
```

---

## 📥 Prerequisites

- Python 3.x
- A Gmail account
- App Passwords enabled (not your regular Gmail password)
- `pandas` library installed: `pip install pandas`

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/birthday-wisher.git
cd birthday-wisher
```

### 2. Add Your Birthday Data

Edit the `birthdays.csv` file like this:

```csv
name,email,year,month,day
Aisha,aisha@example.com,1999,9,15
John,john@example.com,1988,4,12
```

### 3. Add Your Message Templates

Inside the `letter_templates/` folder, create three text files:

**Example: letter_1.txt**
```
Dear [NAME],

Wishing you an amazing birthday and a wonderful year ahead!

– Your Python App 🎂
```

Repeat similarly for `letter_2.txt` and `letter_3.txt`.

---

## 🔐 Setup Gmail App Password (Recommended)

Using your regular Gmail password is not secure. Use an App Password instead:

1. Go to [https://myaccount.google.com](https://myaccount.google.com)
2. Under **Security**, turn on **2-Step Verification**.
3. Then go to the **App Passwords** section.
4. Choose "Mail" as the app and "Other (Custom name)" as the device name (e.g., `Python App`).
5. Google will generate a 16-digit app password. **Copy it and save it temporarily.**

---

## 🌍 Set Environment Variables

For security, avoid hardcoding credentials in the code.

### Windows (CMD):

```cmd
set EMAIL=yourgmail@gmail.com
set PASSWORD=your_app_password
```

### macOS/Linux (Bash):

```bash
export EMAIL=yourgmail@gmail.com
export PASSWORD=your_app_password
```

---

## 🚀 Run the Script

```bash
python main.py
```

If today’s date matches any birthday in your CSV, a birthday email will be sent.

---

## 📧 SMTP Server Settings

| Provider | SMTP Address             | Port |
|----------|--------------------------|------|
| Gmail    | smtp.gmail.com           | 587  |
| Yahoo    | smtp.mail.yahoo.com      | 587  |
| Outlook  | outlook.office365.com    | 587  |

You can change the SMTP address and port in `main.py` if needed.

---

## ✅ To-Do (Optional Enhancements)

- [ ] Add GitHub Action to run this daily.
- [ ] Use `.env` files and `python-dotenv` for smoother config.
- [ ] Add a GUI or web interface for non-coders.

---

## 🧾 License

MIT License © 2025  
Author: Armaan
```

---

Let me know if you'd like a `requirements.txt` or `.env` integration to go with it!
