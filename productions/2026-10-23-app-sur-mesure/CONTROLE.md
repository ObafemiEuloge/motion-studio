# Contrôle : application sur mesure (vidéo 1)

Rendu contrôlé : `renders/app-sur-mesure.mp4`, 30,0 s, 1080 × 1920, 30 i/s, H.264 + AAC.

## Texte
- [x] `verifier_texte.py` sur `script.md`, `audio/voix.txt`, `publication.md`, `storyboard.md`, `index.html`, `compositions/*.html` : OK, aucun interdit.
- [x] Faits : seul 1Peu 1Peu est cité (cofondateur, toute l'API, FastAPI, paiements Mobile Money), conforme à `brand/faits.md`. Aucun montant de vente affiché. EducaPro absent, aucun projet exclu par CLAUDE.md. Montants (15 000 F, 186 000 F, 171 500 F), heures et numéros de commande : illustrations, signalées dans `script.md`.
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun, trois lignes, 132 px, graisse 700 toutes les trois, comme l'ident v3 validé.
- [x] Numéro WhatsApp à l'écran : +229 01 96 25 66 94 (vérifié sur l'image à 29,5 s).

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji. Fond uni ; profondeur par le plan d'interfaces puis par la séquence d'Oba. Les seuls dégradés sont le masque du plan d'interfaces (repris du modèle), le fondu haut et bas de la galerie de captures (masque) et le reflet unique du verre.
- [x] Champagne, un usage par plan : « 21:47 » (bulles), le point de « capture. », le signe ≠, le statut « Payé », les points des pastilles de preuve, le point de « Agnoun. ».
- [x] Le verre a toujours quelque chose derrière : les bulles floutent le plan d'interfaces ; le tableau, la preuve et la signature floutent la séquence d'Oba.
- [x] Séquence d'Oba : jamais en plein écran brut. Étalonnée « B profond » (comparée à 2 autres essais avec `grade-compare`), voile sombre uniforme, ralentie 0,5×, sans son d'origine.

## Mouvement et lecture
- [x] `npx hyperframes check --json` : zéro erreur. Avertissements gardés : `line_unread` sur les chiffres des rouleaux (ils défilent, on lit le total posé) et sur les deux bulles anciennes (même phrase que la bulle déjà lue) ; `nested_structure_needs_subcomposition` sur le plan d'interfaces du modèle ; avertissements WebGL du rendu logiciel, sans effet sur l'image.
- [x] `npx hyperframes snapshot --review` + revue : corrigé les pastilles de preuve qui passaient à la ligne, la coupe entre les deux extraits d'Oba (déplacée au pic de vitesse de la carte qui grandit, 24,88 s), des animations sans état de départ stable. Aucun titre ne bouge après son arrivée.
- [x] Image 0 lisible sans le son : la bulle « Mais j'ai déjà payé hein ! » est posée dès l'image 0.
- [x] Tout texte entre 200 (titre « Capture par capture. ») et 1271 px de haut (bande 168 à 1330), aucune taille sous 28 px. Lu sur 10 images à 360 px de large.
- [x] Tenues : bulle d'accroche 4,0 s ; « Capture par capture. » 2,7 s ; totaux 2 à 3 s ; tableau 6,5 s ; preuve 5 s ; signature 5 s ; ligne WhatsApp 2,9 s (au moins 2,5 s).

## Son
- [x] Voix calée (écart ≤ 0,1 s entre le texte et son mot, `audio/voix.alignment.json`) : bulle 2 / « Tu connais » 2,75 / 2,72 ; titre / « Tu fouilles » 4,35 / 4,32 ; cahier 7,5 / 7,52 ; Mobile Money 8,95 / 9,0 ; ≠ / « autre » 9,82 / 9,84 ; tableau / « Une application » 12,3 / 12,32 ; notification / « Le client » 14,56 / 14,56 ; « Payé » / « payé » 17,2 / 17,2 ; « Toute seule » 17,89 / 17,89 ; « 1Peu 1Peu » / « Un Peu Un Peu » 19,12 / 19,12 ; « paiements » 21,7 / 21,68 ; WhatsApp / « Écris-moi » 27,02 / 27,04.
- [x] `npx hyperframes audio renders/app-sur-mesure.mp4 --json` : son présent, −14,2 LUFS intégrés, crête vraie −2,4 dBTP, aucun écrêtage. Silences détectés seulement de 10,5 à 12,33 s : la pause voulue autour de « Bon. » (musique coupée, puis rouverte sur « Une application »). La musique tient jusqu'à 30 s avec un fondu de 1,2 s (premier rendu refait : le lit précédent s'éteignait seul à 25 s).
- [x] Bruitages seulement sur des actions visibles (bulles, défilement, chiffres qui s'arrêtent, cartes qui se posent, notification, « Payé », signature). Jamais deux fois le même fichier d'affilée (tic_a revient une fois, 12 s plus tard).

## Mesuré, pas écouté
Le son a été mesuré (sonie, crêtes, silences, transcription de la voix) mais personne ne l'a écouté ici. À vérifier à l'oreille par Oba : le petit rire avant « Donc oui… » (la transcription ne le détecte pas), l'équilibre voix et musique sur un téléphone, et le caractère des bruitages.
