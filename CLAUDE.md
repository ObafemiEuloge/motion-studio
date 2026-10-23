# Studio motion d'Obafemi Euloge AGNOUN

Ce dépôt produit les vidéos courtes (Instagram Reels, TikTok, 1080 × 1920) d'Obafemi Euloge AGNOUN, développeur basé à Cotonou. Une vidéo = un dossier dans `productions/AAAA-MM-JJ-<slug>/`.

## Avant toute production

1. `npx hyperframes@0.8.188 skills update` (installe les skills HyperFrames : `/hyperframes`, `/hyperframes-cli`, `/media-use`, `/hyperframes-registry`).
2. `pip install --break-system-packages -q requests` si absent.
3. Navigateur de rendu : `export HYPERFRAMES_BROWSER_PATH=$(ls /opt/pw-browsers/chromium_headless_shell-*/*/headless_shell | head -1)`. S'il n'existe pas : `npx hyperframes browser ensure`.
4. Lis `brand/DESIGN.md` en entier. C'est la loi visuelle.
5. Lance le skill `produire` : il enchaîne tous les autres dans l'ordre.

## Règles qui ne se discutent pas

- **Aucun tiret cadratin (U+2014) ni demi-cadratin (U+2013)** dans les textes, scripts, légendes, sous-titres. Vérifié par `scripts/verifier_texte.py`.
- Tutoiement. Français naturel parlé, pas écrit. Aucun prix affiché.
- Appel à l'action : écrire à Oba sur WhatsApp, **+229 01 96 25 66 94**.
- Nom à l'écran : **Obafemi Euloge AGNOUN** (trois mots, même taille, même graisse).
- EducaPro = un projet **client** sur lequel Oba a travaillé (jamais « mon produit »). Centime (mescentimes.cloud) = **son propre** projet d'envergure. Spyral n'apparaît jamais.
- Ne jamais inventer un chiffre, un client ou un résultat. Les seuls faits utilisables sont dans `brand/faits.md`.
- Voix, musique et bruitages : ElevenLabs uniquement, via `scripts/eleven.py` (la clé est injectée par le secret réseau de l'environnement, ne jamais la demander ni l'écrire).
- Rien n'est publié par Claude. On livre le MP4, la couverture et la légende ; Oba publie.

## Où sont les choses

- `brand/` : charte (`DESIGN.md`), faits vérifiés (`faits.md`), voix (`voix.md`), polices.
- `.claude/skills/` : les skills du studio (brief, script, storyboard, motion, son, sequences, controle, publication, produire).
- `templates/base/` : le projet HyperFrames de départ (charte déjà câblée).
- `references/` : vidéos validées par Oba. Le niveau minimum.
- `sources/selects/` : extraits de ses vidéos déjà étalonnés et prêts à l'emploi.
- `scripts/` : outils (ElevenLabs, vérification du texte).
- `briefs/` : un brief par vidéo (`_modele.md` pour en créer un).
