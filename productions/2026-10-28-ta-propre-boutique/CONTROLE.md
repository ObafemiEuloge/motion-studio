# Contrôle : ta propre boutique (offre Boutique en ligne)

Rendu contrôlé : `renders/ta-propre-boutique.mp4`, 100,8 s, 1080 × 1920, 30 i/s, H.264 + AAC (version corrigée du 28 oct.).

Corrections demandées par Oba après la première livraison :
- [x] Une ligne verticale traversait la carte 1Peu 1Peu (et la carte des mains au clavier) : c'était la frise des 3 semaines, visible avant son chapitre. Elle n'apparaît plus qu'à « Trois semaines ».
- [x] Première phrase : « Tu vends tes formations ou tes produits digitaux en ligne ? ». Seule cette phrase a été régénérée (même voix, même réglage) puis recollée à la prise ; tout ce qui suit est décalé de 1,34 s (`audio/voix.alignment.json`, champ `ouverture_v2`). Les temps ci-dessous sont ceux de la première prise : ajouter 1,34 s après 1,5 s.
- [x] La musique a été prolongée (fondu enchaîné de 2,5 s sur un passage du même lit) pour couvrir les 1,34 s de plus.

## Texte
- [x] `python3 scripts/verifier_texte.py brief.md script.md storyboard.md audio/voix.txt publication.md index.html compositions/*.html` : OK.
- [x] Faits : tous dans `brand/faits.md`, section « Offre Boutique en ligne » (ajoutée le 28 oct. avec la page d'Oba et ses réponses). 5 à 15 % ; 2 000 000 F → 100 000 à 300 000 F ; près de 17 pays africains, près de 50 opérateurs ; 3 semaines ; 1Peu 1Peu.
- [x] Seul montant de l'offre à l'écran : le calcul d'économie validé par Oba (3 000 000 / 300 000 / 125 000 = 75 000 de frais + 50 000 de forfait / + 175 000 par mois / plus de 2 100 000 F sur un an). Le calcul tombe juste. Aucun montant d'installation.
- [x] Aucune plateforme de vente ni aucun agrégateur nommé (« Plateforme » générique). Aucune ville, aucun nom de pays (« pays africains » demandé par Oba). Aucun client inventé : les noms de clients de l'espace vendeur sont des traits.
- [x] Chiffres dits = chiffres affichés, dans le même ordre (vérifié sur la transcription du rendu).
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun., trois lignes, 132 px, graisse 700. Sur-titre « Développeur · Partout, à distance » (règle du 24 oct.).
- [x] Numéro WhatsApp : +229 01 96 25 66 94 (lu sur l'image à 95 s).

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji.
- [x] Fond qui change avec l'histoire : la vitrine encombrée d'une plateforme (claire, serrée), puis le mur des écrans de ta boutique (sombre, aéré), puis la feuille de calcul (lignes de cahier), puis de nouveau ta boutique.
- [x] Illustrations dessinées et animées sur mesure : vente découpée par une lame, formation qui se construit (vidéos, fiches, lune et horloge), fiche rangée dans la vitrine, part qui monte vers la plateforme, barre du mois amputée, boutique montée dans un téléphone (adresse tapée), Afrique en points avec 17 pays allumés et une clé, trajet de l'argent qui contourne « Moi » et « Plateforme », espace vendeur à onglets, barres du calcul, paiements 1Peu 1Peu vérifiés seuls, frise des 3 semaines avec deux points qui avancent ensemble, carte de signature ouverte en iris.
- [x] Champagne, un usage par plan : « avant toi. », « − 15 % », la part 100 000 à 300 000 F, « À ton nom. », « Chez toi », l'écart et « + 175 000 F », le dernier « Vérifié », le « 3 » et « Ta boutique est en ligne. », « BOUTIQUE ».
- [x] Le verre a toujours quelque chose derrière (vitrine ou mur de ta boutique) ; la découpe de la signature est retirée après ouverture pour que le verre floute.

## Mouvement et lecture
- [x] Test du pouce : l'image 0 réduite à 270 px reste lisible (« avant toi. » 156 px, soit 39 px ; lignes de 100 px, soit 25 px). « avant toi. » occupe 63 % de la largeur ; « quelqu'un se sert » 85 %.
- [x] Visage d'Oba : net et éclairé (séquence pensive, étalonnée, carte de 580 × 726). Les mains au clavier sans visage. Son d'origine supprimé (`-an`).
- [x] Appel final : mot-clé BOUTIQUE (champagne) et raison d'écrire (« On fait ton calcul ensemble. »).
- [x] Format long : chaque chapitre se comprend sans le son (titre ou chiffre clé : « Des semaines de travail. », « C'est pratique. », « − 15 % », « 100 000 à 300 000 F », « C'est ton travail... », « À ton nom. », « 17 / 50 », « Affiché = payé. », « Chez toi », « Tu vois tout. », « + 175 000 F », « Déjà construit. », « 3 semaines. »).
- [x] `npx hyperframes check --json` : zéro erreur. Avertissements gardés : `nested_media_start_basis_ambiguous` (vidéos qui démarrent 0,12 et 0,15 s après leur scène, voulu) ; textes de l'écran de téléphone réduit sous 28 px (décor) ; débordements de caches (voulus).
- [x] Revue sur 50 instants : corrigés le mur de la vitrine trop présent, la barre du mois qui chevauchait la pastille « Plateforme », le chiffre « 50 » coupé, la courbe de l'espace vendeur invisible (`pathLength` sur courbe, remplacé par une découpe), la pièce posée sur « Ton client », le mur trop chargé derrière la carte de l'Afrique, les listes d'onglets superposées, le sur-titre de la signature sur deux lignes, un temps mort de 3,3 s à l'accroche (une deuxième vente arrive derrière sur « chaque vente »).
- [x] Texte entre 210 et 1330 px de haut. Infos clés à 36 px ou plus.
- [x] Tenues : chaque titre reste au moins le temps de sa phrase ; signature 8,8 s après « Écris ».

## Son
- [x] `silencedetect=n=-35dB:d=0.35` : seulement 98,07 à 99,5 s (fondu final de la musique, sous la signature). Voix resserrée (43 blancs ramenés à 0,30 s).
- [x] Voix calée (écart ≤ 0,1 s) : accroche image 0 ; lame sur « sert » 3,94 ; « Des semaines » 4,84 ; « Les vidéos / fiches / nuits » 7,37 / 8,33 / 9,29 ; fiche rangée sur « plateforme » 11,53 ; « C'est pratique. » 13,25 ; coches 14,65 / 16,45 / 17,53 ; « elle garde sa part » 20,22 ; 5 / 10 / 15 % sur 21,40 / 22,08 / 23,08 ; « 2 000 000 F » sur « deux » 27,26 ; part sur « cent » 28,64 ; « qui partent » 30,24 ; publicités 32,51 ; « C'est ton travail » 34,09 ; « Ta propre boutique » 38,67 ; « À ton nom » 40,04 ; Mobile Money / Carte 41,79 / 42,67 ; 17 sur « dix-sept » 43,92 ; 50 sur « cinquante » 45,76 ; clé et « accès » 47,23 ; « Affiché = payé » 51,03 ; « Au franc près » 52,91 ; « L'argent arrive » 53,99 ; « Moi » 55,75 ; « Plateforme » 56,62 ; « Chez toi » 57,84 ; onglets 58,91 / 59,63 / 60,43 ; « Tu vois tout » 61,11 ; courbe sur « grandit » 63,29 ; « Faisons le calcul » 64,94 ; 3 000 000 66,38 ; 300 000 68,66 ; 125 000 72,12 ; + 175 000 73,39 ; « chaque mois » 76,03 ; « 2 100 000 » 76,84 ; mains au clavier 78,62 ; « Déjà construit » 79,69 ; « Vérifié » 83,69 ; « Sans que personne ne regarde » 84,62 ; « 3 semaines » 86,15 ; « en ligne » 87,75 ; « Avec toi » 88,43 ; « Écris BOUTIQUE » 90,62 ; numéro 91,49 ; « On fait ton calcul » 91,88.
- [x] `ffmpeg ebur128` sur le rendu : −14,1 LUFS, crête −1,7 dBFS, aucun écrêtage.
- [x] 36 bruitages, seulement sur des actions visibles, jamais deux fois le même fichier d'affilée (vérifié par `outils/sons.py`).

## Mesuré, pas écouté
Personne n'a écouté le son ici. À vérifier à l'oreille par Oba : la nouvelle musique (piano feutré, 102 s), le soupir avant « C'est ton travail », « Un Peu Un Peu », « BOUTIQUE », le bruitage de clavier sous ses mains, les bruitages très faibles remontés (notification, clé, verre), l'équilibre voix et musique sur un téléphone.
