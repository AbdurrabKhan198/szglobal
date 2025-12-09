// ============================================
// ARABIA TRADERS - INTERACTIVE JAVASCRIPT
// ============================================

// Navbar Scroll Effect
window.addEventListener('scroll', function() {
    const navbar = document.getElementById('mainNav');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth Scroll for Navigation Links - Handles both #section and full-url#section
document.querySelectorAll('a[href*="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        
        // Skip dropdown toggle links (Bootstrap handles these)
        if (this.classList.contains('dropdown-toggle')) {
            return true;
        }
        
        // Skip links in dropdown menu that don't have hash (regular navigation links)
        if (this.closest('.dropdown-menu') && !href.includes('#')) {
            return true; // Let normal navigation happen
        }
        
        // Check if it's an internal anchor link (starts with # or contains #)
        if (href && href.includes('#')) {
            const hash = href.split('#')[1];
            
            // If it's just a hash link on the same page
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            } 
            // If it's a full URL with hash (like /products/rice/#contact)
            else if (hash) {
                const urlPath = href.split('#')[0];
                const currentPath = window.location.pathname;
                
                // If it's linking to a different page, let it navigate normally
                // The browser will handle the hash navigation after page load
                if (urlPath && urlPath !== currentPath && urlPath !== '') {
                    // Allow normal navigation - browser will handle hash after load
                    return true;
                }
                // If it's the same page, handle smooth scroll
                else {
                    e.preventDefault();
                    const target = document.querySelector('#' + hash);
                    if (target) {
                        const offsetTop = target.offsetTop - 80;
                        window.scrollTo({
                            top: offsetTop,
                            behavior: 'smooth'
                        });
                    }
                }
            }
        }
    });
});

// Handle hash navigation after page load (for cross-page anchor links)
function handleHashNavigation() {
    if (window.location.hash) {
        const hash = window.location.hash;
        const target = document.querySelector(hash);
        if (target) {
            setTimeout(() => {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }, 300);
        }
    }
}

// Run on page load
window.addEventListener('load', handleHashNavigation);

// Also run on DOMContentLoaded for faster execution
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(handleHashNavigation, 100);
});

// Ensure all links are clickable (remove any pointer-events: none)
document.querySelectorAll('a').forEach(link => {
    link.style.pointerEvents = 'auto';
    link.style.cursor = 'pointer';
});

// Intersection Observer for Fade-in Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observe all cards and sections - but make them visible immediately
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.product-card, .spice-card, .feature-card');
    cards.forEach(card => {
        // Make visible immediately
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
        card.classList.add('visible');
        // Still observe for animations if needed
        observer.observe(card);
    });
});

// Parallax Effect for Hero Section
window.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        const heroContent = heroSection.querySelector('.hero-content');
        if (heroContent && scrolled < heroSection.offsetHeight) {
            heroContent.style.transform = `translateY(${scrolled * 0.5}px)`;
            heroContent.style.opacity = 1 - (scrolled / heroSection.offsetHeight) * 0.5;
        }
    }
    
    // Parallax for background elements
    const heroBackground = document.querySelector('.hero-background');
    if (heroBackground && scrolled < heroSection.offsetHeight) {
        heroBackground.style.transform = `translateY(${scrolled * 0.3}px)`;
    }
});

// Animated Counter for Stats
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            element.textContent = target + '+';
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(start) + '+';
        }
    }, 16);
}

// Observe stats section
const statsObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
            entry.target.classList.add('counted');
            const statNumbers = entry.target.querySelectorAll('.stat-number');
            statNumbers.forEach(stat => {
                const target = parseInt(stat.textContent.replace(/\D/g, ''));
                stat.textContent = '0+';
                setTimeout(() => {
                    animateCounter(stat, target);
                }, 200);
            });
        }
    });
}, { threshold: 0.5 });

const networkSection = document.querySelector('.network-section');
if (networkSection) {
    statsObserver.observe(networkSection);
}

// Spice Particles Animation Enhancement
document.querySelectorAll('.spice-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        const particles = this.querySelector('.spice-particles');
        if (particles) {
            // Create additional particles dynamically
            for (let i = 0; i < 5; i++) {
                const particle = document.createElement('div');
                particle.style.position = 'absolute';
                particle.style.width = '6px';
                particle.style.height = '6px';
                particle.style.background = '#FFB86C';
                particle.style.borderRadius = '50%';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.top = Math.random() * 100 + '%';
                particle.style.animation = `particleFloat ${2 + Math.random() * 2}s ease-in-out infinite`;
                particle.style.animationDelay = Math.random() * 2 + 's';
                particles.appendChild(particle);
            }
        }
    });
    
    card.addEventListener('mouseleave', function() {
        const particles = this.querySelector('.spice-particles');
        if (particles) {
            const dynamicParticles = particles.querySelectorAll('div');
            dynamicParticles.forEach(p => p.remove());
        }
    });
});

// Wood Carousel Auto-scroll (optional)
let woodCarouselScroll = false;
const woodCarousel = document.querySelector('.wood-carousel');

if (woodCarousel) {
    let scrollPosition = 0;
    const scrollSpeed = 0.5;
    
    function autoScroll() {
        if (!woodCarouselScroll) return;
        scrollPosition += scrollSpeed;
        woodCarousel.scrollLeft = scrollPosition;
        
        if (scrollPosition >= woodCarousel.scrollWidth - woodCarousel.clientWidth) {
            scrollPosition = 0;
        }
    }
    
    // Pause on hover
    woodCarousel.addEventListener('mouseenter', () => {
        woodCarouselScroll = false;
    });
    
    woodCarousel.addEventListener('mouseleave', () => {
        woodCarouselScroll = true;
    });
    
    // Start auto-scroll after 3 seconds
    setTimeout(() => {
        woodCarouselScroll = true;
        setInterval(autoScroll, 16);
    }, 3000);
}

// Mobile Menu Close on Click
const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
const navbarCollapse = document.querySelector('.navbar-collapse');
const navbarToggler = document.querySelector('.navbar-toggler');

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth < 992) {
            navbarCollapse.classList.remove('show');
        }
    });
});

// Add loading animation
window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});

// Cursor Effect (Optional Premium Touch)
let cursor = null;
if (window.innerWidth > 768) {
    cursor = document.createElement('div');
    cursor.className = 'custom-cursor';
    cursor.style.cssText = `
        width: 20px;
        height: 20px;
        border: 2px solid #FFB86C;
        border-radius: 50%;
        position: fixed;
        pointer-events: none;
        z-index: 9999;
        transition: transform 0.1s ease;
        display: none;
    `;
    document.body.appendChild(cursor);
    
    document.addEventListener('mousemove', (e) => {
        if (cursor) {
            cursor.style.display = 'block';
            cursor.style.left = e.clientX - 10 + 'px';
            cursor.style.top = e.clientY - 10 + 'px';
        }
    });
    
    document.querySelectorAll('a, button').forEach(el => {
        el.addEventListener('mouseenter', () => {
            if (cursor) cursor.style.transform = 'scale(1.5)';
        });
        el.addEventListener('mouseleave', () => {
            if (cursor) cursor.style.transform = 'scale(1)';
        });
    });
}

// Form Validation (if contact form exists)
const contactForm = document.querySelector('#contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        // Add form submission logic here
        alert('Thank you for your message! We will get back to you soon.');
    });
}

// Ensure all images are visible
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.style.opacity = '1';
        img.style.display = 'block';
    });
    
    // Make sure all product cards are visible
    const productCards = document.querySelectorAll('.product-card, .spice-card, .feature-card');
    productCards.forEach(card => {
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
        card.classList.add('visible');
    });
});

// Performance Optimization: Debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debounce to scroll handlers
const optimizedScrollHandler = debounce(() => {
    // Scroll-based animations
}, 10);

window.addEventListener('scroll', optimizedScrollHandler);

// Add entrance animations on page load
document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.fade-in-up');
    animatedElements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 100);
    });
});

// Export Lines Animation Enhancement
function createExportLine() {
    const exportLines = document.querySelector('.export-lines');
    if (!exportLines) return;
    
    setInterval(() => {
        const line = document.createElement('div');
        line.className = 'export-line';
        line.style.left = Math.random() * 100 + '%';
        line.style.animationDuration = (3 + Math.random() * 2) + 's';
        exportLines.appendChild(line);
        
        setTimeout(() => {
            line.remove();
        }, 5000);
    }, 2000);
}

createExportLine();

// Add 3D tilt effect to cards (subtle)
document.querySelectorAll('.product-card, .spice-card, .feature-card').forEach(card => {
    card.addEventListener('mousemove', function(e) {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 20;
        const rotateY = (centerX - x) / 20;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
    });
    
    card.addEventListener('mouseleave', function() {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
});

console.log('Arabia Traders - Premium Website Loaded Successfully');

