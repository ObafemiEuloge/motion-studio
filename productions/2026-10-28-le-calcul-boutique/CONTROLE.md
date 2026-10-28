# Contrôle : le calcul (offre Boutique en ligne, 30 s)

Rendu contrôlé : `renders/le-calcul-boutique.mp4`, 28,5 s, 1080 × 1920, 30 i/s, H.264 + AAC (2 min 3 s de rendu).

## Texte
- [x] `python3 scripts/verifier_texte.py brief.md script.md storyboard.md audio/voix.txt publication.md index.html compositions/*.html` : OK.
- [x] Faits (`brand/faits.md`, offre Boutique en ligne) : 2 000 000 F → jusqu'à 300 000 F (15 %) ; 3 000 000 F → 300 000 F (10 %) contre 125 000 F → 175 000 F de plus ; près de 17 pays africains ; 3 semaines. Mêmes chiffres que la vidéo longue. « presque tout » : les frais de paiement restent, la barre ne se remplit pas jusqu'au bout et sa légende le dit.
- [x] Aucune plateforme ni aucun agrégateur nommé ; aucune ville ni nom de pays ; aucun montant d'installation.
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun., 132 px, graisse 700. Sur-titre « Développeur · Partout, à distance ».
- [x] Numéro WhatsApp : +229 01 96 25 66 94 (lu sur l'image à 24 s).
- [x] Voix retranscrite par ElevenLabs (scribe) sur le rendu : identique au script.

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée, emoji.
- [x] Monde de fond nouveau : des notifications de paiement réparties en profondeur, qui avancent vers la caméra (vraie parallaxe 3D), atténuées sous la barre, la carte et le calcul.
- [x] Effets nouveaux, jamais utilisés dans les vidéos 1 à 6 : compteurs à tambours 3D (cylindres de dix faces), douze mois croqués, barre « chez toi » avec légende, Afrique en points couchée en 3D avec 17 piliers qui se lèvent, barres en volume dont le haut se détache et vole vers le résultat, cartes qui se retournent, signature qui se redresse depuis la profondeur.
- [x] Retour d'Oba sur l'anneau « chez toi » (pas assez moderne, textes mal placés) : remplacé par une colonne de texte calée à gauche et une barre large qui se remplit à 96,5 %, légende « Chez toi / Frais de paiement ».
- [x] Champagne, un usage par plan : « combien ? », « − 300 000 F », « chez toi. » et la barre, le bloc détaché et « + 175 000 F », « En ligne », « BOUTIQUE ».

## Mouvement et lecture
- [x] Test du pouce : image 0 lisible à 270 px (« combien ? » 196 px, soit 49 px ; lignes de 100 px, soit 25 px). « combien ? » occupe 80 % de la largeur.
- [x] Pas de visage (aucune séquence).
- [x] Appel final : mot-clé BOUTIQUE et raison d'écrire (« On fait ton calcul ensemble. »).
- [x] `npx hyperframes check --json` : zéro erreur (les dix faces de chaque tambour sont exclues du contrôle de chevauchement, par construction).
- [x] Revue sur 25 instants : corrigés les chiffres des tambours rognés et grossis par la perspective (faces avant ramenées à la profondeur zéro), le « F » collé au dernier chiffre, les piliers qui restaient à plat, le flux trop présent derrière la carte, le chiffre 17 qui tournait encore à la sortie, les étiquettes des barres trop près des volumes.
- [x] Texte entre 236 et 1330 px. Infos clés à 36 px ou plus.

## Son
- [x] `silencedetect=n=-35dB:d=0.35` : aucun silence (la musique tient jusqu'au bout).
- [x] Voix calée (écart ≤ 0,1 s) : question image 0 ; 2 000 000 sur « deux » 2,71 ; − 300 000 sur « trois » 4,55 ; mois croqués sur « Chaque mois » 5,68 ; « Avec ta propre boutique » 6,39 ; barre sur « presque » 7,95 ; « chez toi. » 8,95 ; Mobile Money 9,71 ; Carte 10,59 ; 17 piliers sur « dix-sept » 11,59 ; 3 000 000 sur « trois » 13,15 ; bloc détaché sur « gardes » 14,96 ; + 175 000 sur « cent » 15,44 ; « de plus, chaque mois. » 16,88 ; « Ta boutique, » 17,39 ; tonnom.com 18,1 à 18,7 (« à ton nom » 18,15) ; trois cartes sur « trois semaines » 19,0 ; « Écris BOUTIQUE » 20,36 ; numéro 20,96 ; « On fait ton calcul » 21,57.
- [x] `ffmpeg ebur128` : −14,3 LUFS, crête −1,9 dBFS, aucun écrêtage.
- [x] 15 bruitages sur des actions visibles, jamais deux fois le même fichier d'affilée.

## Mesuré, pas écouté
À vérifier à l'oreille par Oba : la nouvelle musique (plus enlevée), les bruitages de tambours et de piliers (nouveaux), « BOUTIQUE », l'équilibre voix et musique sur un téléphone.
