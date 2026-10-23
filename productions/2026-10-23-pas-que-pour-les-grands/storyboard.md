# Storyboard : pas que pour les grands (28,5 s, 1080 × 1920, 30 i/s)

Calé sur la voix (`audio/voix.alignment.json`, 24,8 s ; prise Bakumba unique, blancs ramenés à 0,30 s par `scripts/resserrer_voix.py`). Fond : le plan d'interfaces, incliné dans l'autre sens que les vidéos 1 à 3 (rotation +18°), assombri pendant les illustrations. Musique : un seul lit, sans coupure.

## Illustrations (vecteurs dessinés et animés à la main)

- **La ville** : une tour de six étages (fenêtres qui s'allument une à une) et un petit immeuble, sur une ligne de sol. Trait blanc cassé 3,5 px, épaisseur constante quand la caméra pousse.
- **La boutique** : l'étage du bas de la tour devient une boutique (auvent festonné, poteaux, comptoir, porte).
- **Le gros plan** : sur le comptoir, un téléphone qui vibre ; des bulles de message qui s'échappent et tombent ; des pièces (cercle champagne, « F ») qui glissent par une fente du comptoir.
- **Les modules** : des cartons qui s'empilent (Stock), des fiches clients qui s'ajoutent (Clients).

## Plans

| # | début | fin | voix (mots) | à l'écran | mouvement | son |
|---|---|---|---|---|---|---|
| 1 | 0,00 | 2,90 | Une application ? C'est pour les grandes entreprises. | Image 0 : calé à gauche, « Une application ? / C'est pour les / **grandes** (180 px) / entreprises. » ; à droite la ville au trait, fenêtres de la tour qui s'allument une à une | Texte posé ; seule la tour vit (fenêtres) | lit musical |
| 2 | 2,91 | 5,80 | Non. Une application, ça se fait à ta taille. | Sur « Non » (2,91) un trait champagne barre « grandes » ; le texte part ; la tour rentre étage par étage dans le sol (3,05 à 4,40) et le rez-de-chaussée devient une boutique (auvent qui se trace, 4,2 à 5,0) ; « À ta taille. » (sur « à », 5,03) | Trait tracé 0,35 s ; étages qui descendent, `power2.in`, décalés | trait de feutre ; petits chocs sourds des étages |
| 3 | 5,83 | 10,10 | Toi, ce qui te fait perdre de l'argent aujourd'hui, c'est les commandes et les paiements. | La caméra pousse sur la boutique (5,85 à 6,9) ; « Ce qui te fait perdre : » (sur « Toi ») ; le téléphone vibre, des pièces glissent par la fente du comptoir (sur « perdre », 6,87) ; des bulles s'échappent et tombent, pastille « Commandes perdues » (sur « commandes », 8,91) ; deuxième vague de pièces, pastille « Paiements » (sur « paiements », 9,51) | Poussée de caméra `power2.inOut` ; le téléphone vibre trois fois | pièces qui tombent ; vibration |
| 4 | 10,10 | 12,85 | Alors on commence par ce qui te fait perdre le plus. | Plongée dans l'écran du téléphone : il grandit et devient la petite carte de verre « Commandes + paiements » (10,10 à 10,75) ; titre « On commence par ce qui te fait perdre le plus. » (sur « on commence », 10,46) | L'écran grandit en carte, `expo.inOut` | souffle de plongée |
| 5 | 12,89 | 16,75 | Une petite application, une seule fonction, qui marche tous les jours. | Pastille « 1 fonction » (sur « seule », 14,53) ; une commande « Samedi · 2 robes · 15 000 F » arrive, passe à « Payé » (sur « marche », 15,68) ; les pièces tombent maintenant dans la carte | L'interface travaille ; pièces qui tombent et se posent | déclic « Payé » ; pièces |
| 6 | 16,75 | 21,05 | Le reste viendra quand tu en auras besoin : ton stock, puis tes clients. | Titre « Le reste viendra quand tu en auras besoin. » (16,75) ; un trait relie la carte au module « Stock » qui s'accroche, cartons qui s'empilent (sur « stock », 19,14) ; puis module « Clients », fiches qui s'ajoutent (sur « clients », 20,29) | Modules qui se clipsent `expo.out` ; cartons qui tombent l'un sur l'autre | clic de module, deux variantes |
| 7 | 21,05 | 28,50 | Écris APP sur WhatsApp, je te montre ce que ça donnerait pour ton business. | La carte se retourne (21,05 à 21,65) : au dos, la signature : Obafemi / Euloge / Agnoun., « Écris APP sur WhatsApp » (APP en champagne, 21,45), +229 01 96 25 66 94 (sur « WhatsApp », 22,02), « Applications web et mobiles, sur mesure. » (sur « je te montre », 22,64) | Retournement en deux temps (`power2.in` puis `power3.out`) | souffle de carte qui se retourne ; montée douce |

## Transitions (5 sortes, aucune reprise des vidéos 1 à 3)

1. Mot barré au trait champagne.
2. La tour rentre dans le sol et devient une boutique (le dessin se transforme).
3. Poussée de caméra sur la boutique.
4. Plongée dans l'écran du téléphone, qui devient la carte.
5. La carte se retourne pour montrer la signature.

## Bande de lecture et tailles

Texte entre 168 et 1330 px. Infos clés à 36 px minimum. Champagne : un usage par plan (le trait qui barre, les pièces, la commande « Payé » non : les pièces restent l'accent des plans 3 et 5, « APP » à la fin).
