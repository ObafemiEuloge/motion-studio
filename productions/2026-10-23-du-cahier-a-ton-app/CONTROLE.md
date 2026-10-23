# Contrôle : du cahier à ton app (vidéo 3)

Rendu contrôlé : `renders/du-cahier-a-ton-app.mp4`, 28,0 s, 1080 × 1920, 30 i/s, H.264 + AAC (1 min 54 s de rendu).

## Texte
- [x] `python3 scripts/verifier_texte.py script.md audio/voix.txt publication.md index.html compositions/*.html` : OK (et `storyboard.md`).
- [x] Faits : aucune réalisation chiffrée ; « 15 min » est la durée d'échange donnée par Oba. Aucun délai de projet, aucun montant de vente. Le montant de la notification (15 000 F) est un exemple d'interface.
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun., trois lignes, 132 px, graisse 700.
- [x] Numéro WhatsApp : +229 01 96 25 66 94 (lu sur l'image à 27,5 s).

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji. Fond : plan d'interfaces sur tout le film. Illustrations au trait (fil, bulles, maquette), sans personnage ni décor abstrait : chaque dessin montre un objet de l'histoire.
- [x] Champagne, un usage par plan : « compliqué », « 15 min », le bloc déplacé de la maquette, « Version 1 », « 15 000 F », « comment tu travailles », « APP ». Les points du fil s'allument en blanc cassé.
- [x] Le verre a toujours quelque chose derrière : tube du fil, carte de conversation, notifications (sur le téléphone) et signature floutent le plan d'interfaces.
- [x] Séquence d'Oba : uniquement à l'étape 3, dans une carte arrondie de 560 px, recadrée sur son écran de code (aucun visage), ralentie 0,5×, étalonnage « C froid net » retenu parmi 3 essais (`grade-compare`).

## Mouvement et lecture
- [x] Test du pouce : l'image 0 réduite à 270 px reste lisible (120 px, soit 30 px à 270 px) et pose la question.
- [x] Visage d'Oba : n'apparaît pas (cadrage sur l'écran).
- [x] Appel final : mot-clé APP (champagne) et raison d'écrire (« je te montre ce que ça donnerait pour ton business »).
- [x] `npx hyperframes check --json` : zéro erreur. Avertissements gardés : `nested_media_start_basis_ambiguous` (la vidéo de l'étape 3 démarre à 0,9 s dans sa scène, voulu) ; `nested_structure_needs_subcomposition` sur le plan d'interfaces du modèle ; avertissements WebGL du rendu logiciel.
- [x] Revue sur 13 instants : corrigés les chiffres éteints des points restés sous les points allumés (recouvrement, contraste 1:1), le bloc champagne de la maquette peu visible, le plan d'interfaces qui transparaissait dans la maquette. Aucun titre ne bouge après son arrivée.
- [x] Image 0 lisible sans le son. Texte entre 196 et 1290 px de haut. Infos clés à 36 px ou plus (titres d'étapes 62 px, bulles 42 px, notifications 38 à 44 px, pastilles 36 px ; « Version 1 » 30 px dans le petit téléphone, lisible à 360 px).
- [x] Tenues : question 2,05 s (6 mots, 2,3 ; elle reste lisible pendant sa sortie et la voix la dit) ; titres d'étapes 3,3 à 4,2 s ; bulles 2,5 et 2,9 s ; « 15 min » 2,4 s ; « Version 1 » 1,5 s ; « Paiement reçu » 1,8 s ; « Nouvelle commande » 1,1 s ; phrase clé 2,5 et 1,4 s ; signature 6,6 s après l'appel.

## Son
- [x] Aucun silence de plus de 0,35 s hors la fin : `silencedetect=n=-35dB:d=0.35` ne renvoie que 27,50 à 28,0 s (fondu final). Voix resserrée par `scripts/resserrer_voix.py` (14 blancs ramenés à 0,30 s).
- [x] Voix calée (texte / mot, écart ≤ 0,1 s) : question image 0 ; points 1 à 4 sur « Un » 4,12, « Deux » 7,36, « Trois » 11,60, « Quatre » 15,71 ; titres d'étapes 4,12 / 7,36 / 11,60 / 15,71 ; bulle d'Oba 4,57 / « on échange » 4,57 ; « 15 min » 5,10 / « quinze » 5,10 ; maquette tracée 8,55 / « maquette » 8,55 ; bloc qui change 10,04 / « Tu changes » 10,04 ; carte de code 12,25 / « construis » 12,40 ; téléphone 14,01 / « tu la testes » 14,01 ; « Paiement reçu » 16,72 / « en ligne » 16,72 ; « Nouvelle commande » 17,46 / « clients » 17,56 ; phrase clé 18,57 / « Toi » 18,57 et 19,65 / « comment » 19,65 ; « Écris APP » 21,36 / « APP » 21,36 ; numéro 21,80 / « WhatsApp » 21,80 ; promesse 22,48 / « je » 22,48.
- [x] `npx hyperframes audio renders/du-cahier-a-ton-app.mp4 --json` : son présent, −14,3 LUFS, crête vraie −2,3 dBTP, aucun écrêtage.
- [x] Bruitages seulement sur des actions visibles (trait qui se dessine, fil qui se démêle, points qui s'allument, maquette qui se trace, bloc qui change, carte, téléphone, paiement, signature). Jamais deux fois le même fichier d'affilée.

## Mesuré, pas écouté
Personne n'a écouté le son ici. À vérifier à l'oreille par Oba : « APP » (dit « ap » d'après la transcription), le bruitage du trait (source très faible remontée de 18 dB, possible souffle), les raccords aux endroits resserrés, l'équilibre voix et musique sur un téléphone.
