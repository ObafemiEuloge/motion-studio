# Storyboard : du cahier à ton app (28 s, 1080 × 1920, 30 i/s)

Calé sur la voix (`audio/voix.alignment.json`, 24,8 s ; prise Bakumba unique, blancs ramenés à 0,30 s au plus par `scripts/resserrer_voix.py`). Fond : le plan d'interfaces du début à la fin. Musique : un seul lit chaleureux, sans coupure. Film de 28 s (la voix finit à 24,8 s, la signature tient plus de 7 s).

## Mise en page

- **Le fil** : un tube de verre vertical à gauche (x = 110, de 360 à 1240 px), quatre points numérotés. Un point « s'allume » (fond blanc cassé plein, chiffre sombre) sur le mot qui dit son numéro ; un trait blanc cassé descend dans le tube jusqu'à lui. Pas de halo.
- **L'étape en cours**, à droite (x 220 à 1010) : sur-titre « ÉTAPE n » + titre court en haut (y 210 à 330), puis ce que la personne voit (y 380 à 1300).
- **Illustrations dessinées au trait** (SVG, trait 3 à 4 px, blanc cassé, se tracent sous les yeux) : le fil emmêlé de l'accroche, deux bulles de conversation, la maquette en fil de fer, le téléphone de la version 1.
- **Champagne** : un seul élément par plan (« 15 min », le bloc déplacé de la maquette, « Version 1 », le montant reçu, « comment tu travailles », « APP »).

## Plans

| # | début | fin | voix (mots) | à l'écran | mouvement | son |
|---|---|---|---|---|---|---|
| 1 | 0,00 | 2,05 | Tu crois qu'une application, c'est compliqué ? | Image 0 : « Tu crois qu'une / application, / c'est compliqué ? » en 120 px centré. Dessous, un fil emmêlé qui se trace (0 à 1,6 s) | Titre posé ; le fil se dessine | lit musical ; léger frottement de trait |
| 2 | 2,05 | 4,10 | En vrai, ça tient en quatre étapes. | Le titre sort ; le fil se démêle et devient une ligne verticale à gauche (2,2 à 3,4) ; le tube de verre l'entoure ; quatre points éteints apparaissent sur « quatre » (3,18) | Morphose du tracé, `power2.inOut` 1,2 s ; points à 70 ms d'écart | souffle qui se démêle |
| 3 | 4,12 | 7,30 | Un : on échange quinze minutes sur WhatsApp, comme on parle là. | Point 1 allumé (4,12). « ÉTAPE 1 » / « On en parle sur WhatsApp. » ; dessin de deux bulles ; carte conversation : « Comment tu prends tes commandes ? » (4,57) / « Sur WhatsApp, et je note tout dans un cahier. » (5,74) ; pastille « 15 min » en champagne (sur « quinze », 5,10) | Titre par cache ; bulles qui montent | tic du point ; tics des bulles |
| 4 | 7,36 | 11,55 | Deux : je te montre la maquette de ton application. Tu changes ce que tu veux. | Point 2 allumé (7,36). « ÉTAPE 2 » / « Je te montre la maquette. » ; maquette au trait (cadre de téléphone, blocs, boutons en pointillés) qui se trace (sur « maquette », 8,55) ; sur « Tu changes » (10,04) un bloc glisse à une autre place et devient champagne | Tracé des traits 1,2 s ; le bloc glisse 0,6 s `expo.out` | tic du point ; souffle léger au tracé ; déclic au déplacement |
| 5 | 11,60 | 15,65 | Trois : je construis la première version… et tu la testes sur ton téléphone. | Point 3 allumé (11,60). « ÉTAPE 3 » / « Je construis, tu testes. » ; carte arrondie : l'écran de code d'Oba (sa séquence, sans visage, ralentie, étalonnée) sur « construis » (12,40) ; sur « tu la testes » (14,01) un téléphone avec la première version arrive devant, pastille « Version 1 » en champagne | Carte qui monte ; téléphone qui glisse et se pose | tic du point ; souffle de carte |
| 6 | 15,71 | 18,40 | Quatre : elle est en ligne, et tes clients l'utilisent. | Point 4 allumé (15,71). « ÉTAPE 4 » / « En ligne. » ; le téléphone reçoit « Paiement reçu · Mobile Money · 15 000 F » (sur « en ligne », 16,72 ; montant en champagne) puis « Nouvelle commande · Samedi · 2 robes » (sur « clients », 17,56) | Notifications qui tombent du haut de l'écran | tic du point ; tic de paiement |
| 7 | 18,57 | 20,60 | Toi, tu n'as qu'à me dire comment tu travailles. | L'étape 4 s'efface ; le fil entier, quatre points allumés ; « Toi, tu me dis / comment tu travailles. » (sur « Toi », 18,57 ; « comment tu travailles » en champagne, sur « comment », 19,65) | Titre par cache | rien de plus que la musique |
| 8 | 20,60 | 28,00 | Écris APP sur WhatsApp, je te montre ce que ça donnerait pour ton business. | Le fil sort ; la carte de signature monte : Obafemi / Euloge / Agnoun., trait, « Écris APP sur WhatsApp » (sur « APP », 21,36 ; APP en champagne), +229 01 96 25 66 94 (sur « WhatsApp », 21,80), « Applications web et mobiles, sur mesure. » (sur « je te montre », 22,48) ; un seul reflet | Carte qui monte ; nom ligne par ligne | une seule montée douce ; musique remontée après la voix |

## Transitions (4 sortes)

1. Le fil emmêlé se démêle et devient le fil des étapes (le dessin est la transition).
2. Changement d'étape par caches (titre qui part vers le haut pendant que le suivant monte) et visuel qui part pendant que le suivant monte.
3. Le téléphone glisse devant la carte de code.
4. La signature monte pendant que le fil sort.

## Bande de lecture et tailles

Tout texte entre 168 et 1330 px. Infos clés à 36 px minimum. Image 0 : la question en 120 px, plus de 60 % de la largeur.
