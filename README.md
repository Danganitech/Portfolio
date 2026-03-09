# Ahmad Dangani Hussaini — Portfolio Website

A modern, full-stack personal portfolio built with **Django** (backend) and vanilla **HTML/CSS/JS** (frontend).

---

## 🗂️ Project Structure

```
ahmad_portfolio/
├── config/
│   ├── settings.py       # Django settings
│   └── urls.py           # Root URL config
├── portfolio/
│   ├── views.py          # All views + ALL portfolio data lives here
│   └── urls.py           # Portfolio URL patterns
├── templates/
│   └── portfolio/
│       └── index.html    # Django template (main page)
├── static/
│   └── portfolio/
│       ├── css/style.css
│       ├── js/main.js
│       └── Ahmad_Dangani_Hussaini_CV.pdf   ← Add your CV here
├── requirements.txt
└── manage.py
```

---

## 🚀 Quick Start

### 1. Clone & setup environment
```bash
git clone <your-repo>
cd ahmad_portfolio
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. Collect static files
```bash
python manage.py collectstatic
```

### 4. Start the server
```bash
python manage.py runserver
```

Visit → **http://127.0.0.1:8000**

---

## ✏️ Updating Content

All portfolio data (projects, skills, certs, etc.) is stored as Python dicts/lists at the **top of `portfolio/views.py`**.  
Just edit the variables — no database needed:

| Variable            | What it controls               |
|---------------------|-------------------------------|
| `PROFILE`           | Name, email, phone, LinkedIn  |
| `STATS`             | Hero stats numbers             |
| `EDUCATION`         | Education history              |
| `EXPERIENCE`        | Work experience                |
| `PROJECTS`          | Project cards                  |
| `SKILL_CATEGORIES`  | Skill bars + percentages       |
| `TOOLS`             | Tool chips                     |
| `CERTIFICATIONS`    | Certificate cards              |

---

## 📧 Setting Up Email (Contact Form)

Add a Gmail App Password and set these environment variables:

```bash
export EMAIL_HOST_USER="yourname@gmail.com"
export EMAIL_HOST_PASSWORD="your-16-char-app-password"
```

Or create a `.env` file and load it with `python-dotenv`.

---

## 🌐 Deployment (Render / Railway / VPS)

1. Set `DEBUG = False` in `settings.py`
2. Set `ALLOWED_HOSTS = ['yourdomain.com']`
3. Use `gunicorn config.wsgi:application` as your start command
4. Set `SECRET_KEY` as an environment variable
5. Run `collectstatic` before deploying

---

## 📄 Adding Your CV

Place your PDF at:
```
static/portfolio/Ahmad_Dangani_Hussaini_CV.pdf
```
The "Download CV" button in the navbar will serve it automatically.

---

## 🎨 Features

- ✅ Dark / Light mode toggle (persisted in localStorage)
- ✅ Custom animated cursor
- ✅ Typing animation in hero
- ✅ Particle canvas background
- ✅ Scroll-triggered reveal animations
- ✅ Animated skill bars
- ✅ AJAX contact form with Django backend
- ✅ Mobile responsive + hamburger menu
- ✅ CV download button
- ✅ Active nav link highlighting
- ✅ Page loader animation
