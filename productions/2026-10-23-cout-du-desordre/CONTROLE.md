# Contrôle : le coût du désordre (vidéo 2)

Rendu contrôlé : `renders/cout-du-desordre.mp4`, 30,0 s, 1080 × 1920, 30 i/s, H.264 + AAC (1 min 46 s de rendu).

## Texte
- [x] `python3 scripts/verifier_texte.py brief.md script.md storyboard.md audio/voix.txt publication.md index.html compositions/*.html` : OK.
- [x] Faits : seule réalisation citée, le logiciel de gestion de production pour une usine (ventes, production, rôles et permissions ; Django), conforme à `brand/faits.md`. Montants 25 000 F et 600 000 F affichés « Exemple » sur chaque carte, et le calcul (× 2 par mois × 12 mois) est à l'écran. Articles, quartiers, heures et délais illustrent la situation. Aucun montant de vente.
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun., trois lignes, 132 px, graisse 700.
- [x] Numéro WhatsApp : +229 01 96 25 66 94 (lu sur l'image à 28,5 s).

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji. Fond : plan d'interfaces sur tout le film. Le téléphone est un objet sobre, posé, sans logo de marque, et il ne flotte pas.
- [x] Champagne, un usage par plan : « perdues / oubliées », le point qui marque la commande dans la liste, 600 000 F, « À relancer », points des pastilles de preuve, « APP ».
- [x] Le verre a toujours quelque chose derrière : les cartes de la solution, de la preuve et de la signature floutent le plan d'interfaces.

## Mouvement et lecture
- [x] Test du pouce : l'image 0 réduite à 270 px reste lisible (124 px, soit 31 px à 270 px) et pose le problème.
- [x] Visage d'Oba : absent (aucune séquence, à la demande d'Oba).
- [x] Appel final : mot-clé APP (champagne) et raison d'écrire (« je te montre ce que ça donnerait pour ton business »).
- [x] `npx hyperframes check --json` : zéro erreur. Avertissements gardés : `line_unread` seulement sur les chiffres des rouleaux ; `nested_structure_needs_subcomposition` sur le plan d'interfaces du modèle.
- [x] `npx hyperframes snapshot --review` + revue : corrigés « perdues » et « oubliées » affichés côte à côte (empilement du mot qui roule), le jambage du « p » qui restait visible après le roulement, le téléphone et deux cartes visibles en bas de l'image avant leur entrée, des textes de 24 à 26 px dans le téléphone. Aucun titre ne bouge après son arrivée.
- [x] Image 0 lisible sans le son. Texte entre 196 et 1290 px de haut. Infos clés à 36 px ou plus (montants, étiquettes « Exemple », statuts, preuve, appel) ; dans le téléphone, messages en 38 px et liste en 30 à 34 px (interface du téléphone, lisible à 360 px).
- [x] Tenues : question 4,3 s (8 mots, 2,9) ; « Pas volées. » 1,9 s ; « oubliées » 0,8 s ; message de la cliente 2,6 s (7 mots, 2,6) ; « C'est noté » 1,3 s ; cartes de coût 2,4 à 5,3 s ; titre « Des applications sur mesure. » 4,3 s ; « À relancer » 1,1 s ; preuve 2,5 à 3,6 s ; signature 6,35 s après l'appel.

## Son
- [x] Aucun silence de plus de 0,35 s : `silencedetect=n=-35dB:d=0.35` sur le MP4 ne renvoie rien. Voix resserrée par `scripts/resserrer_voix.py` (9 blancs ramenés à 0,22 s, 2,36 s retirées).
- [x] Voix calée (texte / mot, écart ≤ 0,1 s) : question image 0 / « Combien » 0,0 ; « Pas volées. » 2,40 / 2,40 ; « oubliées » 3,49 / 3,49 (milieu du roulement) ; message 4,70 / « écrit » 4,60 ; « C'est noté » 6,09 / 6,09 ; 25 000 F 8,92 / « Vingt-cinq » 8,92 ; « Et si elle ne revient plus » 10,39 / 10,39 ; calcul et carte « 1 an » 11,79 et 11,85 / « sur » 11,79 ; 600 000 F 13,03 / « six » 13,03 ; titre 15,06 / « applications » 15,06 ; commande de samedi 17,18 / « tombe » 17,18 ; « À relancer » 18,30 / « rien » 18,30 ; « Une usine » 19,46 / 19,46 ; « Ventes et production » 20,58 / « ventes » 20,58 ; pastilles 21,22 / « production » 21,22 ; « Écris APP » 23,65 / « APP » 23,65 ; numéro 24,53 / « WhatsApp » 24,53 ; promesse 25,05 / « je » 25,05.
- [x] `npx hyperframes audio renders/cout-du-desordre.mp4 --json` : son présent, −14,2 LUFS, crête vraie −1,9 dBTP, aucun écrêtage.
- [x] Bruitages seulement sur des actions visibles (mot qui roule, « C'est noté », flot de discussions, arrêt des chiffres, cartes, commande qui arrive, « À relancer », signature). Jamais deux fois le même fichier d'affilée.

## Mesuré, pas écouté
Personne n'a écouté le son ici. À vérifier à l'oreille par Oba : « APP » (dit « ap » dans cette prise selon la transcription), les raccords aux endroits resserrés, le bruitage du flot de messages (nouveau), et l'équilibre voix et musique sur un téléphone.
