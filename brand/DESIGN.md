---
name: Obafemi Euloge AGNOUN, charte motion
version: 1.0 (validée le 23 oct. 2026 sur ident v3)
colors:
  ground: "#04060B"        # fond, presque noir bleuté, toujours uni
  surface: "#0B111D"       # cartes d'interface opaques derrière le verre
  ink: "#F5F3EE"           # texte principal, blanc cassé chaud
  ink-soft: "rgba(245,243,238,0.78)"   # texte secondaire
  ink-mute: "rgba(245,243,238,0.55)"   # sur-titres, étiquettes
  accent: "#D9C6A3"        # champagne pâle : UN seul usage porteur de sens par plan
  glass-fill: "rgba(255,255,255,0.055)"
  glass-stroke: "rgba(255,255,255,0.16)"
  glass-highlight: "rgba(255,255,255,0.28)"   # liseré intérieur du haut
typography:
  display: { family: "Plus Jakarta Sans", weight: 700, tracking: "-0.045em", line-height: 1.0 }
  title:   { family: "Plus Jakarta Sans", weight: 700, tracking: "-0.05em",  line-height: 0.98 }
  body:    { family: "Plus Jakarta Sans", weight: 500, tracking: "-0.01em" }
  eyebrow: { family: "Plus Jakarta Sans", weight: 600, tracking: "0.22em", case: uppercase }
  fonts-dir: brand/fonts
  sizes-1080x1920: { hero: "124-160px", name: "132px", body: "40-46px", eyebrow: "30px", chip: "32px", min: "28px" }
spacing:
  safe-left: 80px
  text-band-y: [168, 1330]   # tout texte lisible reste dans cette bande (UI Instagram / TikTok)
components:
  glass-card: { radius: 64px, blur: 34px, saturate: 150%, stroke: 1.5px, shadow: "0 50px 140px rgba(0,0,0,.6)" }
  chip: { radius: 999px, padding: "20px 34px", fill: glass-fill, stroke: glass-stroke, dot: accent 12px }
  ui-card: { radius: 26px, fill: surface, stroke: "rgba(255,255,255,.07)" }
---

# Intention

Le luxe calme d'Apple et Microsoft appliqué à un développeur africain qui livre du sur mesure. Peu d'éléments, chacun parfait. Le verre dépoli sert à **montrer de vraies interfaces derrière** : on doit toujours sentir le produit, le chiffre, l'application qui tourne. Jamais de décor abstrait.

# À faire

- Fond uni `ground`. La profondeur vient de vraies interfaces en 3D derrière le verre, jamais d'un halo.
- Du verre seulement s'il y a quelque chose derrière à flouter. Sinon, une carte opaque.
- Typo Plus Jakarta Sans grasse et serrée pour les titres, régulière pour le corps.
- Le champagne pour UN mot clé, un point final, un chiffre, une pastille. Jamais en aplat ni en dégradé.
- Entrées par cache (le texte monte depuis un masque, `expo.out`, 0,7 à 0,85 s). Une fois posé, le texte ne bouge plus.
- Sorties 40 à 50 % plus rapides que les entrées (`power3.in`).
- Mouvement continu porté par le monde (plan d'interfaces qui défile, interface qui fonctionne), pas par les titres.
- Un seul reflet lumineux traverse une carte de verre, une fois par film au maximum.
- Ton nom complet, toujours à la même taille et à la même graisse : Obafemi / Euloge / Agnoun.

# Interdits (refusés par Oba, ne jamais réintroduire)

- Halos, lueurs, dégradés de couleur en fond, « glow » autour du texte.
- Lettres qui sortent du flou une par une, flou d'entrée sur les titres.
- Prénom « Euloge » en petit, en italique ou dans une autre police.
- Typo fine et très espacée façon « luxe générique ».
- Emojis, mascottes, sol quadrillé, effets néon, glitch.
- Titres qui flottent, respirent ou continuent de grossir après leur arrivée.
- Le même whoosh sur chaque coupe.

# Référence

`references/idents/ident_v3.html` et `ident_v3.mp4` : la version validée. Toute nouvelle vidéo doit tenir ce niveau.
