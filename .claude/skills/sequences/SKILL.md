---
name: sequences
description: Prépare les vidéos filmées par Oba (repérage des bons moments, recadrage, étalonnage dans la charte sombre) pour les intégrer aux vidéos motion. À utiliser quand Oba fournit une nouvelle séquence ou quand un brief prévoit son image.
---

# Séquences d'Oba

## Recevoir une séquence

1. Les originaux restent chez Oba. Il les compresse avant envoi : `ffmpeg -i IN.MOV -vf "scale=-2:1920" -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 160k OUT_1080.mp4`.
2. Planche contact pour repérer : `ffmpeg -i f.mp4 -vf "fps=1/2,scale=270:-2,tile=6x3" -frames:v 1 planche.jpg`. Note dans `sources/INDEX.md` les moments utilisables (début, fin, ce qu'il fait, son regard).

## Préparer un extrait (un « select »)

- 1 à 4 s, sans le son d'origine (sauf si Oba parle et qu'on veut sa vraie voix).
- Recadrage serré visage ou mains, format de la carte qui l'accueillera.
- Étalonnage dans la charte : la séquence d'origine est claire et chaude (mur beige, plafond bois). Passe-la par `npx hyperframes media-treatment` (lis `/media-use`, `references/media-treatments.md`) : noirs profonds, saturation réduite, légère dominante froide, grain fin. Compare 3 essais avec `npx hyperframes grade-compare` et garde le plus sobre.
- Si le fond gêne : `npx hyperframes remove-background` sur l'extrait, puis pose Oba devant le fond `ground` ou derrière une carte de verre.
- Exporte en `sources/selects/<date>-<moment>.mp4` (moins de 8 Mo) et ajoute une ligne à `sources/INDEX.md`.

## À l'écran

Toujours dans une carte arrondie (rayon 48 à 64 px) ou derrière du verre, jamais en plein écran brut. Un extrait d'Oba par film maximum tant qu'on n'a pas de plans tournés sur fond sombre.
