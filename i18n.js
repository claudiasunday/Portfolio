// Shared trilingual (EN/ES/CA) engine for claudiasunday.com
// Each page defines its own dictionary and calls I18N_APPLY(dict).
window.I18N_SHARED = {
    en: {
        navWork: "Work",
        navAbout: "About me",
        navOOO: "OOO",
        navContact: "Contact me",
        footerLocation: "2024 / 2025 · Leysin, Switzerland &amp; Barcelona, Spain",
        footerLinkedin: "Add me on LinkedIn",
        contactHeading: "Looking for a Product Designer? Say hi.",
        moreProjects: "More projects",
        confidentialTitle: "Confidential project",
        confidentialBtn: "Request more information"
    },
    es: {
        navWork: "Trabajo",
        navAbout: "Sobre mí",
        navOOO: "OOO",
        navContact: "Contáctame",
        footerLocation: "2024 / 2025 · Leysin, Suiza y Barcelona, España",
        footerLinkedin: "Añádeme en LinkedIn",
        contactHeading: "¿Buscas una Product Designer? Escríbeme.",
        moreProjects: "Más proyectos",
        confidentialTitle: "Proyecto confidencial",
        confidentialBtn: "Solicitar más información"
    },
    ca: {
        navWork: "Feina",
        navAbout: "Sobre mi",
        navOOO: "OOO",
        navContact: "Contacta'm",
        footerLocation: "2024 / 2025 · Leysin, Suïssa i Barcelona, Espanya",
        footerLinkedin: "Afegeix-me a LinkedIn",
        contactHeading: "Busques una Product Designer? Escriu-me.",
        moreProjects: "Més projectes",
        confidentialTitle: "Projecte confidencial",
        confidentialBtn: "Sol·licitar més informació"
    }
};

function I18N_APPLY(pageDict) {
    var lang = localStorage.getItem('lang') || 'en';

    function merge(lang) {
        var merged = {};
        var shared = window.I18N_SHARED[lang] || {};
        var page = (pageDict && pageDict[lang]) || {};
        for (var k in shared) merged[k] = shared[k];
        for (var k2 in page) merged[k2] = page[k2];
        return merged;
    }

    function apply(lang) {
        document.documentElement.lang = lang;
        var dict = merge(lang);
        document.querySelectorAll('[data-i18n]').forEach(function (el) {
            var key = el.getAttribute('data-i18n');
            if (dict[key] != null) {
                el.innerHTML = dict[key];
            }
        });
        document.querySelectorAll('.langToggle button').forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-setlang') === lang);
        });
    }

    apply(lang);

    document.querySelectorAll('.langToggle button').forEach(function (btn) {
        btn.addEventListener('click', function () {
            lang = btn.getAttribute('data-setlang');
            localStorage.setItem('lang', lang);
            apply(lang);
        });
    });
}
