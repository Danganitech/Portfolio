# Ahmad Dangani Hussaini — Personal Portfolio

> A modern, full-stack personal portfolio website built with **Django** backend and vanilla **HTML/CSS/JS** frontend.

🌐 **Live Site:** [https://ahmad-portfolio.onrender.com](https://ahmad-portfolio.onrender.com)

---

## 👨‍💻 About

This is the personal portfolio of **Ahmad Dangani Hussaini**, a Software Engineering graduate from Bayero University Kano, Nigeria. The site showcases my projects, skills, certifications, and work experience, and includes a working contact form.

---

## ✨ Features

- 🌙 Dark / Light mode toggle
- ⌨️ Animated typing effect in hero section
- ✨ Particle canvas background
- 📊 Animated skill bars on scroll
- 🖱️ Custom cursor animation
- 📬 AJAX contact form with Django email backend
- 📱 Fully mobile responsive
- 📄 CV download button
- 🔄 Scroll-triggered reveal animations
- ⚡ WhiteNoise for static file serving

---

## 🗂️ Project Structure

```
clean_portfolio/
├── config/
│   ├── settings.py       # Django settings (uses environment variables)
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI entry point
├── portfolio/
│   ├── views.py          # All views + portfolio data
│   └── urls.py           # Portfolio URL patterns
├── templates/
│   └── portfolio/
│       └── index.html    # Main Django template
├── static/
│   └── portfolio/
│       ├── css/style.css
│       ├── js/main.js
│       └── Ahmad_Dangani_Hussaini_CV.pdf
├── .env                  # Local environment variables (never commit this!)
├── .gitignore
├── build.sh              # Render deployment build script
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Danganitech/Portfolio.git
cd Portfolio
```

### 2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the project root
```
SECRET_KEY=your-secret-key-here
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Start the development server
```bash
python manage.py runserver
```

Visit → **http://127.0.0.1:8000**

---

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `EMAIL_HOST_USER` | Gmail address for contact form |
| `EMAIL_HOST_PASSWORD` | Gmail App Password (16 characters) |

> ⚠️ **Never hardcode credentials in your code or commit your `.env` file to GitHub.**

---

## 📧 Setting Up Gmail (Contact Form)

1. Enable **2-Step Verification** on your Google account
2. Go to **Security → App Passwords**
3. Generate a new App Password for "Mail"
4. Add it to your `.env` file as `EMAIL_HOST_PASSWORD`

---

## ✏️ Updating Portfolio Content

All portfolio data (projects, skills, certifications, etc.) is stored as Python dictionaries at the **top of `portfolio/views.py`**. Just edit the variables — no database needed:

| Variable | What it controls |
|---|---|
| `PROFILE` | Name, email, phone, LinkedIn |
| `STATS` | Hero stats numbers |
| `EDUCATION` | Education history |
| `EXPERIENCE` | Work experience |
| `PROJECTS` | Project cards |
| `SKILL_CATEGORIES` | Skill bars + percentages |
| `TOOLS` | Tool chips |
| `CERTIFICATIONS` | Certificate cards |

---

## 🌐 Deployment (Render)

This project is configured for deployment on [Render](https://render.com).

| Field | Value |
|---|---|
| **Runtime** | Python 3 |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn config.wsgi:application` |

Set the environment variables (`SECRET_KEY`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`) in the Render dashboard under **Environment**.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.2 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Outfit, JetBrains Mono (Google Fonts) |
| Static Files | WhiteNoise |
| Deployment | Render |
| Version Control | Git / GitHub |

---

## 📬 Contact

- **Email:** ahmaddanganihussaini@gmail.com
- **Phone:** +234 808 827 8847
- **LinkedIn:** [ahmad-dangani-hussaini](https://linkedin.com/in/ahmad-dangani-hussaini-b511702b9)
- **Location:** Katsina / Kano, Nigeria

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ by Ahmad Dangani Hussaini · 2025*