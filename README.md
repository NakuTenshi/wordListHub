# WordListHub

WordListHub is a lightweight Django-based web application for **browsing, viewing, uploading, and downloading wordlists** stored on a server.  
It is designed mainly for **bug bounty hunters, recon workflows, and payload management**, with strong focus on secure path handling.

---

## 🚀 Features

- Browse wordlist directories via a web interface
- View wordlist files directly in the browser (raw text)
- Upload wordlists (staff users only)
- Download all wordlists as a ZIP archive
- Simple API endpoint to list directories (staff only)
- Protection against directory traversal attacks

---

## 📁 Required Project Structure

Your wordlists **must be placed inside the `wordlist/` directory** in the project root.

Expected structure:

```
Desktop/wordListHub
├── db.sqlite3
├── Downloader
├── manage.py
├── static
├── templates
├── wordlist        <-- ⚠️ PLACE YOUR WORDLISTS HERE
└── wordListHub
```

Only files and directories inside `wordlist/` will be accessible through the application.

---

## ⚙️ Important Configuration

### 1️⃣ MEDIA_ROOT

`MEDIA_ROOT` in `wordListHub/settings.py` **must point to the `wordlist/` directory**.

Example:

```python
MEDIA_ROOT = "/home/username/Desktop/wordListHub/wordlist"
```

---

### 2️⃣ SECRET_KEY (Required)

You **must change the Django `SECRET_KEY`** before running the project.

File:
```
wordListHub/settings.py
```

Recommended approach (environment variable):

```python
import os
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret-key")
```

⚠️ Never commit your real SECRET_KEY to a public repository.

---

## ▶️ Running the Project (Local)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wordlisthub.git
cd wordlisthub
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install django
```

4. Apply migrations and run server:
```bash
python manage.py migrate
python manage.py runserver
```

Open in browser:
```
http://127.0.0.1:8000/?path=/
```

---

## 🔎 Available Endpoints

- `/`  
  Browse directories using the `path` parameter  
  Example:
  ```
  /?path=/subdir/
  ```

- `/show?file=...`  
  View wordlist file content

- `/upload`  
  Upload wordlists (authenticated staff users only)

- `/api/get_dirs/`  
  Returns directory list as JSON (staff users only)

- `/api/download`  
  Download all wordlists as a ZIP file

---

## 🔐 Security Notes

- All user-supplied paths are sanitized using `Path.resolve()` and `is_relative_to()`
- Access outside `MEDIA_ROOT` is blocked
- Upload and API access are restricted to staff users
- Designed for local or trusted environments
- Add authentication and HTTPS before public deployment

---

## 🧠 Common Use Cases

- Bug bounty payload management
- Recon wordlist hosting
- Internal security tooling
- Centralized wordlist server

---

Created By: **ehsan**
