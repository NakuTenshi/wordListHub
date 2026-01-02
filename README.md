# WordListHub

WordListHub is a lightweight Django-based web application that provides a **secure web interface for browsing and viewing wordlists stored on a server**.  
It is designed for **bug bounty hunters, recon workflows, and payload management**, with a strong focus on safe path handling and directory traversal protection.

---

## 🚀 Features

- Browse wordlist directories via a web interface
- View wordlist files directly in the browser
- Secure path sanitization (prevents directory traversal)
- Simple and lightweight Django setup
- Ideal for bug bounty and security testing workflows

---

## 📁 Project Structure

Your wordlists **must** be placed inside the following directory:

```bash
Desktop/wordListHub
├── db.sqlite3
├── Downloader
├── manage.py
├── static
├── templates
├── wordlist        <-- ⚠️ PLACE YOUR WORDLISTS HERE
└── wordListHub
```

```

📌 Only files and directories inside the wordlist/ directory will be accessible through the application.

```


## ⚙️ Installation & Setup
1️⃣ Clone the repository

```bash

git clone https://github.com/yourusername/wordlisthub.git
cd wordlisthub

```
2️⃣ Create a virtual environment (recommended)
```bash 
python3 -m venv venv
source venv/bin/activate

```

3️⃣ Install dependencies
```bash

pip install django

```

## 🔐 Important Security Configuration
**🔑 Change the Django SECRET_KEY**

**Before running the project, you MUST change the SECRET_KEY in:**
```python3
# wordListHub/settings.py
SECRET_KEY = 'change-this-secret-key'

```

---
#### 🧠 Use Cases

*   Bug bounty payload management
*   Recon wordlist organization
*   Local wordlist browsing server
*   Internal security tooling


----

Created By: **Ehsan**
