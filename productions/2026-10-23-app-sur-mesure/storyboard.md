# Storyboard : application sur mesure (30 s, 1080 × 1920, 30 i/s)

Calé sur la prise Bakumba du 23 oct. (`audio/voix.alignment.json`). Chaque début de plan tombe sur le mot qui le dit.

## Les deux mondes

- **0 à 11,6 s, le problème** : le plan d'interfaces 3D du studio (`#world`) défile derrière. Musique retenue, presque rien.
- **11,6 à 30 s, la solution** : coupe franche dans le silence du « Bon. » sur Oba à son bureau (séquence IMG_5677, ralentie 0,5×, étalonnage « B profond » : noirs profonds, froid, saturation basse, grain fin). La séquence reste en fond, assombrie ; les cartes de verre la floutent. On ne la voit nette que 0,7 s, seule, juste après « Bon. ». La musique s'ouvre sur « Une application ».

## Plans

| # | début | fin | voix (mots) | à l'écran | mouvement | son |
|---|---|---|---|---|---|---|
| 1 | 0,0 | 2,7 | « Mais j'ai déjà payé hein ! » [soupir] | Bulle de message en verre, déjà posée à l'image 0 : « Mais j'ai déjà payé hein ! », heure 21:47 | Image 0 lisible. Le monde défile derrière. La bulle ne bouge plus | lit musical très bas |
| 2 | 2,7 | 4,3 | Tu connais cette phrase. | Deux bulles avec la même phrase montent au-dessus (18:02, puis 13:15) et poussent la première vers le bas | Bulles qui arrivent, 0,6 s `expo.out`, 120 ms d'écart | tic de verre léger, 2 variantes |
| 3 | 4,3 | 7,4 | Tu fouilles WhatsApp… capture par capture. | Titre « Capture par capture. » en haut ; dessous, une colonne de captures de paiement Mobile Money qui défile vite puis ralentit | Les bulles sortent vers le haut (0,38 s `power3.in`) ; le titre monte depuis son cache ; la colonne défile (mouvement continu) | un souffle court sur le défilement |
| 4 | 7,4 | 10,9 | Le cahier dit une chose, le Mobile Money autre chose. | Deux cartes opaques : « CAHIER » qui compte jusqu'à 186 000 F (sur « cahier »), « MOBILE MONEY » qui compte jusqu'à 171 500 F (sur « Mobile Money »), le signe ≠ en champagne entre les deux (sur « autre chose ») | Chiffres qui comptent 1,1 s `power3.out`, puis tenus | petit clic quand chaque chiffre s'arrête, 2 variantes |
| 5 | 10,9 | 12,3 | [pause] Bon. | Tout sort (0,4 s). Coupe franche à 11,6 s sur Oba au bureau, seul à l'écran | Coupe dans le silence ; la séquence avance au ralenti, la caméra pousse très lentement (1 → 1,04 sur 18 s) | la musique s'arrête à 11,4 s |
| 6 | 12,3 | 14,5 | Une application peut faire ça à ta place. | Une carte de verre monte et se pose sur Oba : tableau « Commandes · aujourd'hui », quatre lignes, la dernière « Commande 0142 · En attente » | Carte `y +1250 → 0`, 1,1 s `expo.out` ; lignes à 80 ms d'écart | la musique s'ouvre ; souffle de verre qui se pose |
| 7 | 14,5 | 18,8 | Le client paie, et la commande passe à « payé ». Toute seule. | Interface qui travaille : la notification « Paiement reçu · Mobile Money · 15 000 F » entre en haut de la carte (sur « paie ») ; la ligne 0142 passe de « En attente » à « Payé » en champagne (sur « payé ») ; une pastille « Vérifié automatiquement » arrive (sur « Toute seule ») | Le mouvement est dans l'interface | tic sur la notification, petit déclic sur « Payé » |
| 8 | 18,8 | 24,5 | Sur Un Peu Un Peu, j'ai écrit toute l'API, paiements Mobile Money compris. [petit rire] | La carte du tableau part vers le haut ; une carte de preuve monte : sur-titre « DÉJÀ LIVRÉ », titre « 1Peu 1Peu », ligne « Toute l'API, paiements Mobile Money compris. », pastilles « Cofondateur », « FastAPI », « Mobile Money » | Enchaînement de cartes ; contenu ligne par ligne ; pastilles à 70 ms | souffle de verre (2e variante) ; tic sur les pastilles |
| 9 | 24,5 | 27,0 | Donc oui… je connais un peu le sujet. | La carte de preuve grandit et devient la signature : « DÉVELOPPEUR · COTONOU », Obafemi / Euloge / Agnoun, trait, « Applications web et mobiles, sur mesure. » ; le seul reflet du film traverse le verre | La carte grandit jusqu'au plan suivant ; nom ligne par ligne 80 ms ; trait `scaleX` | une seule montée douce qui se pose |
| 10 | 27,0 | 30,0 | Écris-moi sur WhatsApp. | Ligne « WhatsApp · +229 01 96 25 66 94 » qui monte sous la signature, tenue 3 s | Plus rien ne bouge sauf Oba en fond | la musique se pose sur un accord tenu |

## Transitions (4 sortes)

1. Bulles poussées par les suivantes (plan 2), puis sorties vers le haut par cache (plan 3).
2. Coupe franche dans le silence (plan 5).
3. Carte qui part pendant que la suivante monte (plan 8).
4. La carte grandit jusqu'à devenir la signature (plan 9).

## Bande de lecture

Tout texte entre 168 et 1330 px de haut. La carte de signature est posée de 360 à 1320 px pour que la ligne WhatsApp reste dans la bande.
