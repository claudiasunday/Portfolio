/* Site-wide "scroll reveal" — text and cards fade + rise into view as you scroll.
   Separate from the word-by-word "teleprompter" effect (.scrollReveal / srWord),
   which is left untouched so both effects can coexist without conflicting. */
(function () {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    var selector = [
        'section > h2',
        'section > .sub',
        '.pixelsTitle',
        '.ceramics > p:not(.scrollReveal)',
        '.bioPhoto',
        '.projectCard',
        '.featuredCase',
        '.timelineItem',
        '.insightBox',
        '.confidentialBox',
        '.flowItem',
        '.resultCard',
        '.beforeAfterBlock',
        '.ooStep',
        '.ooHeroFull',
        '.igReelCard',
        '.frictionTable',
        '.researchNotesGrid > *',
        '.cvSkillsGrid > div',
        'footer.site'
    ].join(',');

    var els = [];
    try {
        els = Array.prototype.slice.call(document.querySelectorAll(selector));
    } catch (e) {
        return;
    }

    els.forEach(function (el) {
        if (el.classList.contains('scrollReveal')) { return; }
        el.classList.add('revealOnScroll');
    });

    var revealEls = document.querySelectorAll('.revealOnScroll');

    if (!('IntersectionObserver' in window)) {
        revealEls.forEach(function (el) { el.classList.add('inView'); });
        return;
    }

    var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('inView');
                io.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    revealEls.forEach(function (el) { io.observe(el); });
})();
