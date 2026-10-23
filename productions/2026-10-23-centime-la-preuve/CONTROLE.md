# Contrôle : Centime, la preuve (vidéo 5)

Rendu contrôlé : `renders/centime-la-preuve.mp4`, 26,5 s, 1080 × 1920, 30 i/s, H.264 + AAC (2 min 55 s de rendu).

## Texte
- [x] `python3 scripts/verifier_texte.py script.md storyboard.md audio/voix.txt publication.md index.html compositions/*.html` : OK.
- [x] Faits : à l'écran, seulement « Chaque franc a un rôle », « En ligne depuis un an », « Version 2 » (faits.md). Aucun chiffre d'utilisateurs. Les montants de l'interface sont ceux des captures de démonstration de Centime, cohérents entre eux (58 000 + 25 000 + 2 000 + 15 000 = 100 000 ; 57 325 − 5 000 = 52 325 ; 27 675 + 5 000 = 32 675), écrits « F » comme dans les vidéos 1 à 4.
- [x] Captures : uniquement les captures de démonstration fournies par Oba (`sources/centime/`), aucune donnée personnelle ajoutée.
- [x] Centime présenté comme son propre produit ; aucun autre projet nommé.
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun., trois lignes, 132 px, graisse 700.
- [x] Numéro WhatsApp : +229 01 96 25 66 94 (lu sur l'image à 25,5 s).
- [x] Voix retranscrite par ElevenLabs (scribe) sur le rendu : identique au script.

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji.
- [x] Fond qui change avec l'histoire (demande d'Oba) : l'atelier (traits de construction, repères d'angle, croix) pour « j'ai construit » et « le soin » ; le mur des cinq vraies captures de Centime, en perspective, pour la démonstration et la signature. Toujours de vraies interfaces ou des traits de construction, jamais de décor abstrait.
- [x] Illustrations dessinées et animées à la main : téléphone au trait avec cotes et rayon, balayage qui le change en vraie capture, répartition du revenu le long d'un courant qui allume chaque enveloppe, feuille « Nouvelle dépense » avec le doigt qui touche le pavé puis l'enveloppe, chiffres qui roulent, anneau de douze mois, deux cartes de version qui changent de place, repères de précision transportés d'un téléphone à l'autre, contour qui s'ouvre en carte de signature.
- [x] Interface de Centime redessinée fidèlement aux captures (couleurs, libellés, montants) pour pouvoir l'animer ; les captures elles-mêmes au fond, dans le téléphone de l'accroche, dans la carte « Version 2 » et dans le téléphone du « soin ».
- [x] Champagne, un usage par plan : « la mienne. », la ligne de balayage, « tout seul. », le geste en cours, « un rôle. », le « 2 », « le tien. », « APP ».
- [x] Le verre floute bien ce qui est derrière : la découpe de la signature est retirée une fois ouverte (sinon le verre ne floute plus rien).

## Mouvement et lecture
- [x] Test du pouce : l'image 0 réduite à 270 px reste lisible (« la mienne. » 178 px, soit 44 px à 270 px ; lignes de 90 px, soit 22 px). « la mienne. » occupe 76 % de la largeur.
- [x] Visage d'Oba : n'apparaît pas.
- [x] Appel final : mot-clé APP (champagne) et raison d'écrire.
- [x] `npx hyperframes check --json` : zéro erreur. Avertissements gardés : `duplicate_media_discovery_risk` (les captures répétées sur le mur, voulu) ; `dead_stretch` 0 à 3,1 s (le téléphone se dessine pendant ce temps, l'outil ne voit pas les tracés) ; chiffres qui roulent signalés comme lus trop vite (ce sont des chiffres en mouvement, le résultat reste affiché).
- [x] Revue sur 30 instants : corrigés les montants « 00 000 » visibles avant la répartition, l'anneau qui arrivait sur la carte encore présente, deux animations qui se chevauchaient, le verre de la signature qui ne floutait pas.
- [x] Texte entre 236 et 1330 px de haut. Infos clés à 36 px ou plus (titres 72 à 90 px, interface 36 à 128 px ; libellés secondaires de l'interface 28 à 34 px, comme dans Centime).
- [x] Tenues : accroche 3,2 s ; « Centime » 0,8 s (dit en même temps) ; titres 1,4 à 2,2 s ; « En ligne depuis un an » 2,4 s ; « Version 2 » 0,9 s (dit en même temps) ; phrase clé 2,9 s puis 1,6 s pour « je le mets dans le tien. » (dite en même temps) ; signature 6,8 s après l'appel.

## Son
- [x] Aucun silence de plus de 0,35 s hors la fin : `silencedetect=n=-35dB:d=0.35` ne renvoie que 26,05 à 26,5 s (fondu final). Voix resserrée par `scripts/resserrer_voix.py` (12 blancs ramenés à 0,30 s).
- [x] Voix calée (texte / mot, écart ≤ 0,1 s) : accroche image 0 ; balayage 3,17 / « Elle » 3,17 ; « Centime » 3,96 / « Centime » 3,96 ; « Un revenu arrive. » 4,75 / « Un » 4,75 ; revenu 4,91 / « revenu » 4,91 ; « Rangé tout seul. » et courant 6,19 / « range » 6,19 ; feuille 7,88 / « Une dépense » 7,84 ; touche 5 à 8,89 / « Deux » 8,89 ; touche 000 à 9,10 / « gestes » 9,08 ; enveloppe 9,60 / « et » 9,60 ; feuille qui descend 9,90 / « noté » 9,92 ; « Chaque franc a un rôle. » 10,45 / « Et tu sais » 10,45 ; « En ligne depuis un an » 12,98 / « tourne » 12,98 ; « Version 2 » 14,70 / « version » 14,70 ; phrase clé 15,57 / « Le soin » 15,57 et 17,29 / « je le mets » 17,29 ; « Écris APP » 18,80 / « APP » 18,81 ; numéro 19,49 / « WhatsApp » 19,49 ; promesse 20,16 / « je » 20,16.
- [x] `ffmpeg ebur128` sur le rendu : −14,3 LUFS, crête −1,9 dBFS, aucun écrêtage.
- [x] Bruitages seulement sur des actions visibles (crayon, révélation, revenu, courant, feuille, touches, décompte, anneau, cartes, repères, signature). Jamais deux fois le même fichier d'affilée.

## Mesuré, pas écouté
Personne n'a écouté le son ici. À vérifier à l'oreille par Oba : la nouvelle musique (piano feutré), le bruitage du crayon sous l'accroche, les touches du pavé (sources très faibles remontées), « APP », l'équilibre voix et musique sur un téléphone.
