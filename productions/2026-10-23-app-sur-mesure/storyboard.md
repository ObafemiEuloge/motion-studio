# Storyboard : application sur mesure, version 2 (30 s, 1080 × 1920, 30 i/s)

Calé sur la voix v2 (`audio/voix.alignment.json`, 27,0 s). La voix v2 est un assemblage : prise du 23 oct. recoupée (phrases 1 à 6) + trois phrases régénérées avec la même voix et les mêmes réglages (bénéfice, preuve, appel). Aucun blanc de voix de plus de 0,35 s.

## Règles v2 appliquées

- Image 0 = l'accroche en très grand, au centre de la bande lisible (140 px, plus de 60 % de la largeur).
- Le monde d'interfaces est le fond du début à la fin ; il tourne de 5° sur « Bon. » (changement d'angle de caméra). Aucune séquence d'Oba.
- Musique continue : le lit « problème » se fond dans le lit « solution » sur « Bon. », sans trou.
- Infos clés à 36 px minimum (montants, statuts, preuve, appel). Seuls des détails d'interface (heure « à l'instant », libellés de captures) restent plus petits.

## Plans

| # | début | fin | voix (mots) | à l'écran | mouvement | son |
|---|---|---|---|---|---|---|
| 1 | 0,00 | 2,00 | « Mais j'ai déjà payé hein ! » [soupir] | « Un client, ce soir · 21:47 » puis « Mais j'ai / déjà payé / hein ! » en 140 px centré, « payé » en champagne | Déjà posé à l'image 0. Sort vers le haut par cache à 1,85 s | lit « problème » |
| 2 | 2,04 | 4,90 | Tu fouilles WhatsApp… capture par capture. | Titre « Capture par capture. » ; galerie de captures de paiement | Titre par cache sur « Tu » ; la galerie file vite puis ralentit | souffle de défilement |
| 3 | 5,08 | 8,30 | Le cahier dit une chose, le Mobile Money autre chose. | « CAHIER » 186 000 F (sur « cahier »), « MOBILE MONEY » 171 500 F (sur « Mobile »), ≠ champagne (sur « autre ») | Cartes opaques qui montent ; rouleaux de chiffres | clic à l'arrêt de chaque chiffre |
| 4 | 8,32 | 10,70 | Bon. Une application peut faire ça à ta place. | Les totaux sortent sur « Bon. » ; le plan d'interfaces tourne de 5° ; la carte de verre « Commandes · aujourd'hui » monte sur « Une application » | Carte `y +1250 → 0` 1,1 s `expo.out` | fondu enchaîné des musiques ; souffle de verre |
| 5 | 10,79 | 14,30 | Le client paie, et la commande passe à « payé ». Toute seule. | Notification « Paiement reçu » (sur « Le client ») ; 0142 passe à « Payé » (sur « payé », 13,25) ; pastille « Vérifié automatiquement » (sur « Toute », 13,72) | Interface qui travaille | tic, déclic « Payé » |
| 6 | 14,38 | 17,95 | Le soir, tu fermes la boutique… les comptes sont déjà faits. | La carte part ; sur le monde : « Ce soir · 21:47 » (sur « soir »), 186 000 F qui compte, « encaissé et vérifié », « Écart 0 F » (sur « comptes », 0 F en champagne) | Titre sur le monde, chiffre qui compte | tic léger à l'arrêt |
| 7 | 18,01 | 22,40 | Sur Un Peu Un Peu, chaque paiement est vérifié sans que personne ne regarde. | Carte de preuve : « DÉJÀ EN SERVICE », « 1Peu 1Peu » (sur « Un Peu »), « Paiements Mobile Money vérifiés côté serveur. » (sur « chaque paiement »), pastilles « Cofondateur », « Toute l'API » | Carte qui monte, lignes par cache, pastilles 70 ms | souffle de verre (2e variante) |
| 8 | 22,40 | 30,00 | Écris APP sur WhatsApp, je te montre ce que ça donnerait pour ton business. | La carte grandit et devient la signature : Obafemi / Euloge / Agnoun., trait, « Écris APP sur WhatsApp » (sur « APP », APP en champagne), +229 01 96 25 66 94 (sur « WhatsApp »), « Applications web et mobiles, sur mesure. » (sur « je te montre ») ; un seul reflet sur le verre | La carte grandit ; nom ligne par ligne 80 ms ; tenue 5 s après l'appel | une seule montée douce ; musique remontée après la voix, fondu final |

## Transitions (4 sortes)

1. Sortie par cache vers le haut (accroche, titre des captures).
2. Changement d'angle du plan d'interfaces sur « Bon. ».
3. Carte qui part pendant que la suivante monte (tableau vers bénéfice, bénéfice vers preuve).
4. La carte de preuve grandit jusqu'à devenir la signature.

## Bande de lecture

Tout texte entre 168 et 1330 px de haut. La signature est posée de 360 à 1320 px ; le numéro finit vers 1290 px.
