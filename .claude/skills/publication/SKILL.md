---
name: publication
description: Prépare la publication Instagram et TikTok d'une vidéo du studio (légende humaine, couverture, hashtags, premier commentaire). Oba publie lui-même.
---

# Publication

Sortie : `publication.md` + `renders/<slug>_couverture.jpg`.

## Couverture
L'image de l'accroche (souvent l'image 0 ou 0,5 s), 1080 × 1920, texte dans le cadre central 1080 × 1350 (recadrage de la grille Instagram) : `ffmpeg -ss <t> -i renders/<slug>.mp4 -frames:v 1 -q:v 2 renders/<slug>_couverture.jpg`.

## Légende (Instagram et TikTok)
- Première ligne = une suite de l'accroche, pas sa répétition. Moins de 90 caractères (c'est ce qui s'affiche avant « plus »).
- 3 à 6 lignes courtes, tutoiement, même voix que le script. Une seule idée.
- Fin : « Écris-moi sur WhatsApp : +229 01 96 25 66 94 » (et « lien en bio » si Oba en a un).
- 3 à 5 hashtags précis (métier, besoin, audience ; jamais de ville ni de pays), jamais #viral ni #fyp. Exemples à adapter : #developpeurweb #applicationmobile #entrepreneur #MobileMoney #businessenligne.
- Passe `python3 scripts/verifier_texte.py publication.md`.

## Premier commentaire (facultatif)
Une question simple qui invite la cible à répondre (« Tu gères encore tes commandes dans un cahier ? »).

## Meilleurs créneaux à proposer
En semaine, heure de l'audience principale (GMT+1 par défaut) : 12 h à 13 h 30 et 19 h 30 à 21 h. À ajuster selon les statistiques de son compte.
