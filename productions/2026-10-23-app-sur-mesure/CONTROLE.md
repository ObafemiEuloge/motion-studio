# Contrôle : application sur mesure (vidéo 1, version 2)

Rendu contrôlé : `renders/app-sur-mesure.mp4`, 30,0 s, 1080 × 1920, 30 i/s, H.264 + AAC, rendu le 23 oct. 2026 (1 min 54 s).

## Texte
- [x] `python3 scripts/verifier_texte.py script.md audio/voix.txt publication.md index.html compositions/*.html` : OK (et `storyboard.md`, `brand/voix.md`).
- [x] Faits : seul 1Peu 1Peu est cité, en résultat (« chaque paiement est vérifié sans que personne ne regarde », « Paiements Mobile Money vérifiés côté serveur », « Cofondateur », « Toute l'API »), conforme à `brand/faits.md`. Aucun montant de vente. Montants, heure 21:47 et numéro de commande : illustrations, signalées dans `script.md`.
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun., trois lignes, 132 px, graisse 700, comme l'ident v3.
- [x] Numéro WhatsApp : +229 01 96 25 66 94 (lu sur l'image à 28,5 s).

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji. Fond uni + plan d'interfaces sur tout le film. Seuls dégradés : masque du plan (modèle), fondu de la galerie (masque), reflet unique du verre.
- [x] Champagne, un usage par plan : « payé » (accroche), le point de « capture. », ≠, statut « Payé », « 0 F », points des pastilles de preuve, « APP » (signature ; le point de « Agnoun. » passe en blanc cassé pour garder un seul champagne).
- [x] Le verre a toujours quelque chose derrière : le tableau, la preuve et la signature floutent le plan d'interfaces.

## Mouvement et lecture
- [x] Test du pouce : l'image 0 réduite à 270 px de large reste lisible (« Mais j'ai déjà payé hein ! » en 150 px, soit 37 px à 270 px) et dit le problème.
- [x] Visage d'Oba : n'apparaît pas (séquence retirée en v2), donc rien de flou.
- [x] Appel final : mot-clé APP (en champagne) et raison d'écrire (« je te montre ce que ça donnerait pour ton business »).
- [x] `npx hyperframes check --json` : zéro erreur. Avertissements gardés : `line_unread` uniquement sur les chiffres des rouleaux (on lit le total posé) ; `container_overflow` sur les rouleaux du bilan (la colonne de chiffres dépasse sa fenêtre par construction) ; `nested_structure_needs_subcomposition` sur le plan d'interfaces du modèle.
- [x] `npx hyperframes snapshot --review` + revue : corrigés en cours de route le chevauchement accroche / galerie, une scène qui s'arrêtait avant la fin de sa sortie (écran vide à 2,3 s), des jambages et accents qui dépassaient des caches (« Écart », « Écris », « DÉJÀ », sorties à −135 %), des zéros rognés dans les compteurs. Aucun titre ne bouge après son arrivée.
- [x] Image 0 lisible sans le son. Tout texte entre 200 et 1290 px de haut (bande 168 à 1330). Infos clés à 36 px ou plus (statuts, notification, pastilles, étiquettes des totaux, sur-titres de l'accroche et du bilan) ; seuls « à l'instant », « Commandes · aujourd'hui » et les libellés des captures restent plus petits (détails d'interface).
- [x] Tenues (0,5 s + 0,3 s par mot) : accroche 2,05 s (5 mots, 2,0) ; « Capture par capture. » 1,4 s (3 mots, 1,4) ; totaux 1,7 à 3,2 s ; « Payé » 1,25 s ; « Vérifié » 0,8 s (1 mot, 0,8) ; « Écart 0 F » 1,4 s (3 mots, 1,4) ; preuve 2,7 à 3,8 s ; signature 6,85 s après l'appel (au moins 2,5 s).

## Son
- [x] Aucun silence de plus de 0,35 s : `silencedetect=n=-35dB:d=0.35` sur le MP4 ne renvoie que la fin (29,08 à 30 s, fondu final). En voix seule non plus (prise recoupée, blancs de 0,05 à 0,22 s).
- [x] Voix calée, écart ≤ 0,1 s (texte / mot) : accroche image 0 / « Mais » 0,08 ; titre captures 3,40 / « capture » 3,40 ; CAHIER 5,08 / « Le » 5,08 ; MOBILE MONEY 6,55 / « le » 6,56 ; ≠ 7,40 / « autre » 7,40 ; tableau 8,62 / « Une » 8,67 ; notification 10,79 / « Le » 10,79 ; « Payé » 13,25 / « payé » 13,25 ; « Vérifié » 13,72 / « Toute » 13,72 ; « Ce soir » 14,62 / « soir » 14,62 ; « Écart 0 F » 16,66 / « les » 16,66 ; « 1Peu 1Peu » 18,41 / « Un » 18,41 ; corps de la preuve 19,53 / « chaque » 19,53 ; « Écris APP » 23,15 / « APP » 23,15 ; numéro 23,87 / « WhatsApp » 23,87 ; promesse 24,70 / « je » 24,71.
- [x] `npx hyperframes audio renders/app-sur-mesure.mp4 --json` : son présent, −15,0 LUFS, crête vraie −1,1 dBTP, aucun écrêtage.
- [x] Bruitages seulement sur des actions visibles (galerie, arrêt des chiffres, cartes qui se posent, notification, « Payé », « 0 F », signature). Jamais deux fois le même fichier d'affilée.

## Mesuré, pas écouté
Personne n'a écouté le son ici. À vérifier à l'oreille par Oba : la prononciation de « APP » (dit comme « ap » ou épelé ? une variante « app » prononcé comme un mot est prête dans `audio/v2/appel_b.mp3`), les raccords entre phrases de l'ancienne prise et phrases régénérées, le « Bon. » (remonté de 10 dB car murmuré), et l'équilibre voix et musique sur un téléphone.
