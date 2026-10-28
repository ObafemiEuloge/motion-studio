---
name: controle
description: Contrôle qualité d'une vidéo du studio avant rendu final et livraison (texte, charte, mouvement, lisibilité téléphone, son). À utiliser avant chaque livraison, sans exception.
---

# Contrôle

Écris `CONTROLE.md` dans le dossier de production avec chaque case et ce que tu as mesuré. Une case non cochée bloque la livraison.

## Texte
- [ ] `python3 scripts/verifier_texte.py script.md audio/voix.txt publication.md index.html compositions/*.html` affiche OK.
- [ ] Chaque fait vient de `brand/faits.md`. Aucun prix (sauf le calcul d'économie de l'offre Boutique en ligne). EducaPro dit « pour un client ». Aucune ville ni le nom d'un pays.
- [ ] Les chiffres affichés sont exactement ceux dits par la voix, et le calcul tombe juste.
- [ ] Nom à l'écran : Obafemi Euloge AGNOUN, trois mots, même taille.
- [ ] Numéro WhatsApp exact : +229 01 96 25 66 94.

## Charte
- [ ] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji (comparer à `brand/DESIGN.md`, section Interdits).
- [ ] Champagne : un seul usage porteur de sens par plan.
- [ ] Le verre a toujours quelque chose derrière à flouter.

## Mouvement et lecture
- [ ] Test du pouce : l'image 0 réduite à 270 px de large reste lisible et dit le problème.
- [ ] Le visage d'Oba, s'il apparaît, est net et éclairé ; sinon le plan est retiré.
- [ ] L'appel final contient le mot-clé de l'offre (APP, BOUTIQUE, PAGE, MOTION) et la raison d'écrire.
- [ ] Format long : chaque chapitre se comprend sans le son (un titre ou un chiffre clé à l'écran), et aucune séquence d'Oba ne garde son son d'origine.
- [ ] `npx hyperframes check --json` : zéro erreur ; avertissements lus et justifiés.
- [ ] `npx hyperframes snapshot --review` puis `/hyperframes` `references/review.md` : aucun titre qui bouge après son arrivée, aucun saut aux coupes.
- [ ] Image 0 lisible sans le son. Tout texte entre 168 et 1330 px, taille ≥ 28 px.
- [ ] Chaque ligne tient au moins 0,5 s + 0,3 s par mot. Signature finale ≥ 2,5 s.

## Son
- [ ] Aucun silence de plus de 0,35 s : `ffmpeg -i renders/<slug>.mp4 -af silencedetect=n=-35dB:d=0.35 -f null - 2>&1 | grep silence_start` ne renvoie rien (sauf la fin).
- [ ] Voix calée : chaque texte arrive sur son mot (écart ≤ 0,1 s).
- [ ] `npx hyperframes audio renders/<slug>.mp4 --json` : son présent, −16 à −14 LUFS, crête ≤ −1 dBTP.
- [ ] Bruitages seulement sur des actions visibles ; pas deux fois le même fichier d'affilée.

Signale à Oba ce qui a été mesuré mais pas écouté.
