import io, sys

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1) Insert new project card in the Personal projects grid, right after the Aula EAA card
anchor_html = '''            <a class="projectCard" href="https://claudiasunday.github.io/accesibility/" target="_blank" rel="noopener">
                <img src="aula-eaa-card.png" alt="Aula EAA — gamified accessibility course preview">
                <h3 data-i18n="aulaeaaTitle">Aula EAA</h3>
                <p data-i18n="aulaeaaDesc">A gamified, interactive course that teaches teams the European Accessibility Act (EAA) and WCAG criteria through lessons, quizzes, streaks and badges.</p>
                <div class="tags">#Accessibility #A11y #WCAG #Gamification #UX</div>
            </a>
'''
assert content.count(anchor_html) == 1, f"anchor_html count={content.count(anchor_html)}"

new_card = anchor_html + '''            <a class="projectCard" href="https://claudiasunday.github.io/ceramica-cenotipia/" target="_blank" rel="noopener">
                <img src="cianotipia-card.png" alt="Cianotipia &amp; Cerámica — cyanotype on ceramics study notebook preview">
                <h3 data-i18n="cianotipiaTitle">Cianotipia &amp; Cerámica</h3>
                <p data-i18n="cianotipiaDesc">A study notebook exploring how to combine 19th-century cyanotype photography with ceramic surfaces — from preparing digital images to printing Prussian-blue exposures on clay.</p>
                <div class="tags">#Ceramics #Cyanotype #Photography #CraftProcess</div>
            </a>
'''
content = content.replace(anchor_html, new_card, 1)

# 2) Insert dict keys in EN block
en_anchor = '''                    aulaeaaTitle: "Aula EAA",
                    aulaeaaDesc: "A gamified, interactive course that teaches teams the European Accessibility Act (EAA) and WCAG criteria through lessons, quizzes, streaks and badges.",
                    afinmesCta: "Try it &rarr;",'''
assert content.count(en_anchor) == 1, f"en_anchor count={content.count(en_anchor)}"
en_new = '''                    aulaeaaTitle: "Aula EAA",
                    aulaeaaDesc: "A gamified, interactive course that teaches teams the European Accessibility Act (EAA) and WCAG criteria through lessons, quizzes, streaks and badges.",
                    cianotipiaTitle: "Cianotipia & Cerámica",
                    cianotipiaDesc: "A study notebook exploring how to combine 19th-century cyanotype photography with ceramic surfaces — from preparing digital images to printing Prussian-blue exposures on clay.",
                    afinmesCta: "Try it &rarr;",'''
content = content.replace(en_anchor, en_new, 1)

# 3) Insert dict keys in ES block
es_anchor = '''                    aulaeaaTitle: "Aula EAA",
                    aulaeaaDesc: "Curso interactivo y gamificado que enseña a los equipos la Ley Europea de Accesibilidad (EAA) y los criterios WCAG a través de lecciones, quizzes, rachas e insignias.",
                    afinmesCta: "Pruébala &rarr;",'''
assert content.count(es_anchor) == 1, f"es_anchor count={content.count(es_anchor)}"
es_new = '''                    aulaeaaTitle: "Aula EAA",
                    aulaeaaDesc: "Curso interactivo y gamificado que enseña a los equipos la Ley Europea de Accesibilidad (EAA) y los criterios WCAG a través de lecciones, quizzes, rachas e insignias.",
                    cianotipiaTitle: "Cianotipia & Cerámica",
                    cianotipiaDesc: "Un cuaderno de estudio sobre cómo combinar la cianotipia (técnica fotográfica del siglo XIX) con superficies cerámicas — desde la preparación digital de la imagen hasta la exposición en azul de Prusia sobre barro.",
                    afinmesCta: "Pruébala &rarr;",'''
content = content.replace(es_anchor, es_new, 1)

# 4) Insert dict keys in CA block
ca_anchor = '''                    aulaeaaTitle: "Aula EAA",
                    aulaeaaDesc: "Curs interactiu i gamificat que ensenya als equips la Llei Europea d'Accessibilitat (EAA) i els criteris WCAG mitjançant lliçons, qüestionaris, ratxes i insígnies.",
                    afinmesCta: "Prova-la &rarr;",'''
assert content.count(ca_anchor) == 1, f"ca_anchor count={content.count(ca_anchor)}"
ca_new = '''                    aulaeaaTitle: "Aula EAA",
                    aulaeaaDesc: "Curs interactiu i gamificat que ensenya als equips la Llei Europea d'Accessibilitat (EAA) i els criteris WCAG mitjançant lliçons, qüestionaris, ratxes i insígnies.",
                    cianotipiaTitle: "Cianotipia & Ceràmica",
                    cianotipiaDesc: "Un quadern d'estudi sobre com combinar la cianotípia (tècnica fotogràfica del segle XIX) amb superfícies ceràmiques — des de la preparació digital de la imatge fins a l'exposició en blau de Prússia sobre fang.",
                    afinmesCta: "Prova-la &rarr;",'''
content = content.replace(ca_anchor, ca_new, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("OK: all 4 edits applied")
