---
name: produire
description: Produit une vidéo complète d'Obafemi Euloge AGNOUN de A à Z (brief, script, storyboard, voix, musique, bruitages, motion, rendu, contrôle, légende). À utiliser dès qu'on demande une nouvelle vidéo, un reel ou un TikTok.
---

# Produire une vidéo, de A à Z

Enchaîne les skills du studio dans cet ordre. Ne saute aucune étape, n'en fusionne aucune.

| # | Étape | Skill | Ce qui sort |
|---|---|---|---|
| 0 | Préparer | (ci-dessous) | dossier `productions/AAAA-MM-JJ-<slug>/` |
| 1 | Brief | `brief` | `brief.md` |
| 2 | Script | `script` | `script.md` (voix off + textes à l'écran) |
| 3 | Storyboard | `storyboard` | `storyboard.md` (plans minutés) |
| 4 | Voix | `son` (voix) | `audio/voix.mp3`, `audio/voix.alignment.json` |
| 5 | Re-minutage | `storyboard` | storyboard calé sur les mots réels de la voix |
| 6 | Images d'Oba | `sequences` | extraits étalonnés dans `assets/media/` (si le brief en prévoit) |
| 7 | Motion | `motion` | projet HyperFrames rendu possible |
| 8 | Musique et bruitages | `son` (musique, bruitages, mixage) | `assets/audio/*`, pistes placées |
| 9 | Contrôle | `controle` | `CONTROLE.md`, toutes les cases cochées |
| 10 | Rendu | `motion` (rendu) | `renders/<slug>.mp4` |
| 11 | Publication | `publication` | `publication.md` (légende, couverture, hashtags) |

## 0. Préparer

```bash
SLUG=<mots-cles-courts>; D=productions/$(date +%F)-$SLUG
cp -r templates/base $D && mkdir -p $D/audio $D/renders
```
Lis `brand/DESIGN.md`, `brand/faits.md`, `brand/voix.md`, puis regarde `references/idents/ident_v3.mp4` (quelques images avec ffmpeg) pour avoir le niveau en tête.

## Mode sans questions

Une tâche programmée n'a personne pour répondre. Si une information manque au brief, prends l'option la plus prudente (faits de `brand/faits.md` uniquement, offre principale), écris en tête de `brief.md` ce que tu as supposé, et va jusqu'au MP4.

## Livraison

Envoie à Oba le MP4, l'image de couverture et le texte de `publication.md`, en une seule fois. Ajoute une ligne : ce qui a été mesuré (niveaux sonores, lisibilité) et ce qu'il doit vérifier lui-même à l'écoute. Ne publie jamais à sa place. Pousse le dossier de production sur le dépôt (sans les rendus lourds : `renders/` est ignoré par git).
