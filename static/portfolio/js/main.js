// ===========================
// LOADER
// ===========================
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('loader').classList.add('hidden');
  }, 1800);
});

// ===========================
// CUSTOM CURSOR
// ===========================
const dot = document.getElementById('cursorDot');
const outline = document.getElementById('cursorOutline');
let mouseX = 0, mouseY = 0, outX = 0, outY = 0;

document.addEventListener('mousemove', e => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  dot.style.left = mouseX - 4 + 'px';
  dot.style.top = mouseY - 4 + 'px';
});

function animateCursor() {
  outX += (mouseX - outX - 16) * 0.1;
  outY += (mouseY - outY - 16) * 0.1;
  outline.style.left = outX + 'px';
  outline.style.top = outY + 'px';
  requestAnimationFrame(animateCursor);
}
animateCursor();

document.querySelectorAll('a, button, .project-card, .cert-card, .contact-item, .quick-fact').forEach(el => {
  el.addEventListener('mouseenter', () => outline.classList.add('expanded'));
  el.addEventListener('mouseleave', () => outline.classList.remove('expanded'));
});

// ===========================
// THEME TOGGLE
// ===========================
const themeBtn = document.getElementById('themeToggle');
const body = document.body;
const savedTheme = localStorage.getItem('theme') || 'dark';
body.className = savedTheme;

themeBtn.addEventListener('click', () => {
  const isDark = body.classList.contains('dark');
  body.className = isDark ? 'light' : 'dark';
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
});

// ===========================
// NAVBAR SCROLL
// ===========================
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
  updateActiveNav();
});

function updateActiveNav() {
  const sections = document.querySelectorAll('section[id]');
  const links = document.querySelectorAll('.nav-link');
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 200) current = sec.id;
  });
  links.forEach(l => {
    l.classList.toggle('active', l.getAttribute('href') === '#' + current);
  });
}

// ===========================
// MOBILE MENU
// ===========================
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger.addEventListener('click', () => {
  mobileMenu.classList.toggle('open');
});

document.querySelectorAll('.mobile-link').forEach(link => {
  link.addEventListener('click', () => mobileMenu.classList.remove('open'));
});

// ===========================
// TYPING ANIMATION
// ===========================
const phrases = [
  'full-stack web apps.',
  'AI-powered solutions.',
  'Django backends.',
  'cloud systems.',
  'clean, fast UIs.',
  'the future of the web.'
];

let phraseIndex = 0, charIndex = 0, isDeleting = false;
const typingEl = document.getElementById('typingText');

function type() {
  if (!typingEl) return;
  const current = phrases[phraseIndex];
  if (isDeleting) {
    typingEl.textContent = current.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typingEl.textContent = current.substring(0, charIndex + 1);
    charIndex++;
  }
  if (!isDeleting && charIndex === current.length) {
    setTimeout(() => { isDeleting = true; }, 1800);
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    phraseIndex = (phraseIndex + 1) % phrases.length;
  }
  setTimeout(type, isDeleting ? 50 : 85);
}
setTimeout(type, 2000);

// ===========================
// SCROLL REVEAL
// ===========================
const revealEls = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, (entry.target.dataset.delay || 0));
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

revealEls.forEach((el, i) => {
  el.dataset.delay = (i % 4) * 80;
  revealObserver.observe(el);
});

// ===========================
// SKILL BARS ANIMATION
// ===========================
const skillFills = document.querySelectorAll('.skill-fill');
const skillObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.width = entry.target.dataset.width + '%';
      skillObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.3 });
skillFills.forEach(f => skillObserver.observe(f));

// ===========================
// HERO CANVAS PARTICLES
// ===========================
const canvas = document.getElementById('heroCanvas');
if (canvas) {
  const ctx = canvas.getContext('2d');
  let particles = [];

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 1.5 + 0.5;
      this.opacity = Math.random() * 0.5 + 0.1;
      this.vx = (Math.random() - 0.5) * 0.3;
      this.vy = (Math.random() - 0.5) * 0.3;
    }
    update() {
      this.x += this.vx; this.y += this.vy;
      if (this.x < 0 || this.x > canvas.width || this.y < 0 || this.y > canvas.height) this.reset();
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(108, 99, 255, ${this.opacity})`;
      ctx.fill();
    }
  }

  for (let i = 0; i < 80; i++) particles.push(new Particle());

  function drawLines() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.strokeStyle = `rgba(108,99,255,${0.06 * (1 - dist / 120)})`;
          ctx.lineWidth = 0.5;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    drawLines();
    requestAnimationFrame(animate);
  }
  animate();
}

// ===========================
// CONTACT FORM (AJAX)
// ===========================
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = document.getElementById('submitBtn');
    btn.disabled = true;
    btn.querySelector('.btn-text').textContent = 'Sending...';

    const formData = new FormData(contactForm);
    try {
      const res = await fetch(contactForm.action, {
        method: 'POST',
        headers: { 'X-CSRFToken': formData.get('csrfmiddlewaretoken'), 'X-Requested-With': 'XMLHttpRequest' },
        body: formData
      });
      const data = await res.json();
      const msgEl = document.createElement('div');
      msgEl.className = `form-msg form-msg-${data.status}`;
      msgEl.textContent = data.message;
      contactForm.insertBefore(msgEl, btn);
      if (data.status === 'success') contactForm.reset();
    } catch {
      const msgEl = document.createElement('div');
      msgEl.className = 'form-msg form-msg-error';
      msgEl.textContent = 'Something went wrong. Please try again.';
      contactForm.insertBefore(msgEl, btn);
    } finally {
      btn.disabled = false;
      btn.querySelector('.btn-text').textContent = 'Send Message';
    }
  });
}
