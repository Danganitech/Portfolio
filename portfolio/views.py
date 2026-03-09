from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import datetime


# ─────────────────────────────────────────────
#  ALL PORTFOLIO DATA  (edit here to update site)
# ─────────────────────────────────────────────

PROFILE = {
    "name": "Ahmad Dangani Hussaini",
    "tagline": "Software Engineer | Django Developer | AI & Blockchain Enthusiast",
    "location": "Katsina / Kano, Nigeria",
    "email": "ahmaddanganihussaini@gmail.com",
    "phone": "+234 808 827 8847",
    "linkedin": "linkedin.com/in/ahmad-dangani-hussaini-b511702b9",
    "summary": (
        "Software engineering graduate with expertise in Django, HTML, CSS, and JavaScript. "
        "Experienced through academic projects including a full-stack YouTube proxy application "
        "and professional exposure during NYSC service in Human Resources, Corporate Affairs, "
        "and Marketing. Expanding knowledge in generative AI, prompt engineering, and cloud "
        "technologies via Coursera, LinkedIn Learning, Google Cloud Skills Boost, and Simplilearn. "
        "Strong problem-solving, collaboration, and adaptability skills with a passion for "
        "delivering innovative solutions."
    ),
}

STATS = [
    {"value": "1+",  "label": "Years Experience"},
    {"value": "5+",  "label": "Certifications"},
    {"value": "3+",  "label": "Projects Built"},
    {"value": "2",   "label": "Degrees Earned"},
]

QUICK_FACTS = [
    {"icon": "📍", "label": "Location",    "value": "Katsina / Kano, Nigeria"},
    {"icon": "🎓", "label": "Degree",      "value": "B.Sc. Software Engineering"},
    {"icon": "🏛️", "label": "University",  "value": "Bayero University Kano"},
    {"icon": "✉️", "label": "Email",       "value": "ahmaddanganihussaini@gmail.com"},
]

HIGHLIGHTS = [
    {"icon": "🚀", "text": "Full-stack developer with Django & JavaScript expertise"},
    {"icon": "🤖", "text": "Actively expanding into Generative AI & Prompt Engineering"},
    {"icon": "☁️", "text": "Hands-on with Google Cloud (Vertex AI, Cloud Shell)"},
    {"icon": "🤝", "text": "Strong communicator with real-world HR & marketing exposure"},
]

LANGUAGES = ["English", "Hausa"]

EDUCATION = [
    {
        "years": "2018 – 2024",
        "degree": "B.Sc. Software Engineering",
        "institution": "Bayero University Kano, Nigeria",
        "note": "Final Year Project: YouTube Proxy Application",
    },
    {
        "years": "2016 – 2018",
        "degree": "National Innovation Diploma — Software Engineering",
        "institution": "Dialogue Institute of Computer, Nigeria",
        "note": None,
    },
    {
        "years": "2007 – 2013",
        "degree": "Secondary School Certificate",
        "institution": "Auntie Rahmatu College, Katsina",
        "note": None,
    },
]

EXPERIENCE = [
    {
        "years": "2024 – 2025",
        "role": "HR, Corporate Affairs & Marketing",
        "company": "National Youth Service Corps (NYSC)",
        "location": "Kano, Nigeria",
        "responsibilities": [
            "Supported HR functions including staff documentation and onboarding.",
            "Assisted corporate affairs with communications and event coordination.",
            "Contributed to marketing initiatives through client engagement and service promotion.",
        ],
    },
]

PROJECTS = [
    {
        "icon": "📺",
        "name": "YouTube Proxy Application",
        "description": (
            "A full-stack web proxy application built with Django, HTML, CSS, and JavaScript. "
            "Integrated the YouTube Data API for secure video search and display. Implemented "
            "user authentication, session management, and custom folder creation for organizing "
            "saved videos — serving as the final year capstone project at BUK."
        ),
        "tech": ["Django", "Python", "JavaScript", "HTML/CSS", "YouTube API", "SQLite", "Auth"],
        "github": "",
        "live": "",
    },
    {
        "icon": "🤖",
        "name": "AI Prompt Engineering Toolkit",
        "description": (
            "Exploration and implementation of generative AI capabilities using Vertex AI "
            "on Google Cloud Platform. Covers prompt design patterns, vector search, embeddings, "
            "and BigQuery integration for AI-powered data analytics."
        ),
        "tech": ["Vertex AI", "GCP", "BigQuery", "Vector Search", "Embeddings", "Python"],
        "github": "",
        "live": "",
    },
    {
        "icon": "🎨",
        "name": "UI/UX Design System",
        "description": (
            "Component library and design system built with Figma, translated into responsive "
            "HTML/CSS implementations. Focus on accessibility, consistent visual language, "
            "and pixel-perfect front-end execution."
        ),
        "tech": ["Figma", "HTML", "CSS", "Responsive Design", "Accessibility"],
        "github": "",
        "live": "",
    },
]

SKILL_CATEGORIES = [
    {
        "icon": "💻",
        "name": "Programming",
        "skills": [
            {"name": "Python (Django)",  "level": 82},
            {"name": "JavaScript",       "level": 70},
            {"name": "SQL",              "level": 68},
            {"name": "Git",              "level": 75},
        ],
    },
    {
        "icon": "🌐",
        "name": "Web & Design",
        "skills": [
            {"name": "HTML5 / CSS3",     "level": 88},
            {"name": "Figma",            "level": 65},
            {"name": "REST APIs",        "level": 72},
            {"name": "Responsive UI",    "level": 80},
        ],
    },
    {
        "icon": "🤖",
        "name": "AI & Cloud",
        "skills": [
            {"name": "Generative AI",    "level": 65},
            {"name": "Prompt Engineering","level": 70},
            {"name": "Google Cloud",     "level": 60},
            {"name": "Data Analytics",   "level": 58},
        ],
    },
    {
        "icon": "🧠",
        "name": "Soft Skills",
        "skills": [
            {"name": "Problem Solving",        "level": 90},
            {"name": "Team Collaboration",     "level": 88},
            {"name": "Emotional Intelligence", "level": 85},
            {"name": "Time Management",        "level": 82},
        ],
    },
]

TOOLS = [
    {"icon": "🐍", "name": "Python"},
    {"icon": "🎸", "name": "Django"},
    {"icon": "🟨", "name": "JavaScript"},
    {"icon": "🐙", "name": "Git / GitHub"},
    {"icon": "🗄️", "name": "PostgreSQL"},
    {"icon": "💾", "name": "SQLite"},
    {"icon": "☁️", "name": "Google Cloud"},
    {"icon": "🧠", "name": "Vertex AI"},
    {"icon": "📊", "name": "BigQuery"},
    {"icon": "🎨", "name": "Figma"},
    {"icon": "🤖", "name": "Microsoft Copilot"},
    {"icon": "🔍", "name": "Cloud Shell"},
]

CERTIFICATIONS = [
    {"logo": "🟦", "provider": "Coursera",       "name": "ChatGPT Prompt Engineering for Developers", "year": "2024"},
    {"logo": "🟦", "provider": "Coursera",       "name": "Introduction to Generative AI",              "year": "2024"},
    {"logo": "🟦", "provider": "Coursera",       "name": "Figma Basics",                              "year": "2024"},
    {"logo": "🟥", "provider": "Google Cloud",   "name": "Vertex AI Prompt Design",                   "year": "2024"},
    {"logo": "🟥", "provider": "Google Cloud",   "name": "Vector Search & Embeddings",                "year": "2024"},
    {"logo": "🟥", "provider": "Google Cloud",   "name": "BigQuery & TensorFlow MinDiff",             "year": "2024"},
    {"logo": "🟦", "provider": "LinkedIn Learning","name": "Generative AI & Microsoft Copilot",        "year": "2024"},
    {"logo": "🟧", "provider": "Simplilearn",    "name": "Introduction to Data Analytics",            "year": "2024"},
]

CONTACT_ITEMS = [
    {"icon": "✉️",  "label": "Email",    "value": PROFILE["email"],   "href": f"mailto:{PROFILE['email']}",  "external": False},
    {"icon": "📞",  "label": "Phone",    "value": PROFILE["phone"],   "href": f"tel:{PROFILE['phone']}",     "external": False},
    {"icon": "💼",  "label": "LinkedIn", "value": "ahmad-dangani-hussaini", "href": f"https://{PROFILE['linkedin']}", "external": True},
    {"icon": "📍",  "label": "Location", "value": PROFILE["location"], "href": "#",                          "external": False},
]


# ─────────────────────────────────────────────
#  VIEWS
# ─────────────────────────────────────────────

def index(request):
    """Main portfolio page."""
    context = {
        "profile":          PROFILE,
        "stats":            STATS,
        "quick_facts":      QUICK_FACTS,
        "highlights":       HIGHLIGHTS,
        "languages":        LANGUAGES,
        "education":        EDUCATION,
        "experience":       EXPERIENCE,
        "projects":         PROJECTS,
        "skill_categories": SKILL_CATEGORIES,
        "tools":            TOOLS,
        "certifications":   CERTIFICATIONS,
        "contact_items":    CONTACT_ITEMS,
        "current_year":     datetime.datetime.now().year,
    }
    return render(request, "portfolio/index.html", context)


def contact(request):
    """Handle contact form submissions (AJAX + standard POST)."""
    if request.method != "POST":
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed(["POST"])

    name    = request.POST.get("name", "").strip()
    email   = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "").strip()
    message = request.POST.get("message", "").strip()

    # Basic validation
    if not all([name, email, subject, message]):
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"status": "error", "message": "All fields are required."})
        messages.error(request, "All fields are required.")
        return redirect("portfolio:index")

    # Build email body
    body = (
        f"New portfolio contact from {name} <{email}>\n\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}"
    )

    try:
        send_mail(
            subject=f"[Portfolio Contact] {subject}",
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[PROFILE["email"]],
            fail_silently=False,
        )
        status, msg = "success", "Message sent! I'll get back to you soon."
    except Exception as e:
        status, msg = "error", "Failed to send message. Please email me directly."

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"status": status, "message": msg})

    getattr(messages, status)(request, msg)
    from django.shortcuts import redirect
    return redirect("portfolio:index")
