/* =========================================================================
   INKLEAF BOOK HOUSE — main.js
   Handles: navbar scroll state, mobile menu, count-up stats, countdown
   timer, WhatsApp book ordering, scroll-to-top, AOS init, Swiper init,
   smooth scrolling + active nav link tracking.
   ========================================================================= */
document.addEventListener('DOMContentLoaded', function () {

    /* ---------------- AOS ---------------- */
    if (window.AOS) {
        AOS.init({
            duration: 700,
            once: true,
            offset: 80,
            easing: 'ease-out-cubic',
        });
    }

    /* ---------------- Navbar scroll state ---------------- */
    var navbar = document.getElementById('siteNavbar');
    function updateNavbarState() {
        if (!navbar) return;
        if (window.scrollY > 40) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
    updateNavbarState();
    window.addEventListener('scroll', updateNavbarState, { passive: true });

    /* ---------------- Mobile nav toggle ---------------- */
    var navToggle = document.getElementById('navToggle');
    var navMenu = document.getElementById('navMenu');
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            var isOpen = navMenu.classList.toggle('open');
            navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });
        navMenu.querySelectorAll('.nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                navMenu.classList.remove('open');
                navToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    /* ---------------- Active nav link on scroll ---------------- */
    var sections = Array.from(document.querySelectorAll('section[id]'));
    var navLinks = Array.from(document.querySelectorAll('.nav-link'));
    function setActiveLink() {
        var scrollPos = window.scrollY + 140;
        var current = sections[0];
        sections.forEach(function (sec) {
            if (sec.offsetTop <= scrollPos) current = sec;
        });
        navLinks.forEach(function (link) {
            link.classList.remove('active');
            if (current && link.getAttribute('href') === '#' + current.id) {
                link.classList.add('active');
            }
        });
    }
    if (sections.length) {
        window.addEventListener('scroll', setActiveLink, { passive: true });
        setActiveLink();
    }

    /* ---------------- Count-up statistics ---------------- */
    var countEls = document.querySelectorAll('.count-up');
    function animateCount(el) {
        var target = parseInt(el.getAttribute('data-target'), 10) || 0;
        var duration = 1600;
        var start = null;

        function step(timestamp) {
            if (!start) start = timestamp;
            var progress = Math.min((timestamp - start) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.floor(eased * target).toLocaleString('en-IN');
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                el.textContent = target.toLocaleString('en-IN');
            }
        }
        window.requestAnimationFrame(step);
    }

    if (countEls.length && 'IntersectionObserver' in window) {
        var statsObserver = new IntersectionObserver(function (entries, obs) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    animateCount(entry.target);
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.4 });
        countEls.forEach(function (el) { statsObserver.observe(el); });
    } else {
        countEls.forEach(animateCount);
    }

    /* ---------------- Countdown timer ---------------- */
    var countdownEl = document.getElementById('countdownTimer');
    if (countdownEl) {
        var hoursFromNow = parseFloat(countdownEl.getAttribute('data-hours')) || 24;
        var endTime = Date.now() + hoursFromNow * 60 * 60 * 1000;

        var hoursSpan = document.getElementById('cdHours');
        var minutesSpan = document.getElementById('cdMinutes');
        var secondsSpan = document.getElementById('cdSeconds');

        function pad(n) { return n < 10 ? '0' + n : '' + n; }

        function tickCountdown() {
            var remaining = endTime - Date.now();
            if (remaining <= 0) {
                hoursSpan.textContent = '00';
                minutesSpan.textContent = '00';
                secondsSpan.textContent = '00';
                return;
            }
            var h = Math.floor(remaining / (1000 * 60 * 60));
            var m = Math.floor((remaining / (1000 * 60)) % 60);
            var s = Math.floor((remaining / 1000) % 60);
            hoursSpan.textContent = pad(h);
            minutesSpan.textContent = pad(m);
            secondsSpan.textContent = pad(s);
            window.requestAnimationFrame(function () {
                setTimeout(tickCountdown, 250);
            });
        }
        tickCountdown();
    }

    /* ---------------- WhatsApp book ordering ---------------- */
    var orderButtons = document.querySelectorAll('.btn-order-whatsapp');
    orderButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {
            var title = btn.getAttribute('data-book') || 'this book';
            var author = btn.getAttribute('data-author') || '';
            var price = btn.getAttribute('data-price') || '';
            var message = 'Hi, I am interested in ordering ' + title +
                (author ? ' by ' + author : '') +
                (price ? ' - \u20B9' + price : '') +
                '. Please share availability.';
            var phoneMeta = document.querySelector('meta[name="whatsapp-number"]');
            var phone = phoneMeta ? phoneMeta.content : '919845022981';
            var url = 'https://wa.me/' + phone + '?text=' + encodeURIComponent(message);
            window.open(url, '_blank', 'noopener');
        });
    });

    /* ---------------- Scroll to top ---------------- */
    var scrollTopBtn = document.getElementById('scrollTopBtn');
    if (scrollTopBtn) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 480) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        }, { passive: true });

        scrollTopBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ---------------- Swiper: testimonials ---------------- */
    if (window.Swiper) {
        new Swiper('.testimonial-swiper', {
            slidesPerView: 1,
            spaceBetween: 24,
            loop: true,
            autoplay: { delay: 4500, disableOnInteraction: false },
            pagination: { el: '.swiper-pagination', clickable: true },
            breakpoints: {
                768: { slidesPerView: 2 },
                1200: { slidesPerView: 3 },
            },
        });

        /* ---------------- Swiper: best sellers ---------------- */
        new Swiper('.best-sellers-swiper', {
            slidesPerView: 1,
            spaceBetween: 24,
            loop: true,
            autoplay: { delay: 3800, disableOnInteraction: false },
            navigation: {
                nextEl: '.best-sellers-next',
                prevEl: '.best-sellers-prev',
            },
            pagination: { el: '.best-sellers-pagination', clickable: true },
            breakpoints: {
                768: { slidesPerView: 2 },
                1200: { slidesPerView: 4 },
            },
        });
    }
});
