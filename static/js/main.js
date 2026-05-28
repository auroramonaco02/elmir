// ============================================
// ELMIR_DE — Main JavaScript
// ============================================

// Mobile menu toggle
function toggleMenu() {
    const menu = document.getElementById('mobileMenu');
    if (menu) menu.classList.toggle('open');
}

// Scroll animations
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.program-card, .vacancy-card, .city-tag, .ausbildung-card, .vacancy-full-card').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
}

// Navbar scroll effect
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// Smooth counter animation
function animateCounters() {
    document.querySelectorAll('.stat-num').forEach(el => {
        const text = el.textContent;
        const num = parseInt(text.replace(/\D/g, ''));
        if (isNaN(num)) return;
        const suffix = text.replace(/[0-9]/g, '');
        let start = 0;
        const duration = 1500;
        const step = Math.ceil(num / (duration / 16));
        const timer = setInterval(() => {
            start += step;
            if (start >= num) {
                start = num;
                clearInterval(timer);
            }
            el.textContent = start + suffix;
        }, 16);
    });
}

// Init
document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initScrollAnimations();

    // Animate counters when hero is visible
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        const obs = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
                obs.disconnect();
            }
        }, { threshold: 0.5 });
        obs.observe(heroStats);
    }
});

// Add CSS for fade-in animations
const style = document.createElement('style');
style.textContent = `
.fade-in { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease, transform 0.6s ease; }
.fade-in.visible { opacity: 1; transform: translateY(0); }
.navbar.scrolled { background: rgba(10,10,10,0.98); box-shadow: 0 2px 24px rgba(0,0,0,0.3); }
`;
document.head.appendChild(style);
