# Contrôle : pas que pour les grands (vidéo 4)

Rendu contrôlé : `renders/pas-que-pour-les-grands.mp4`, 28,5 s, 1080 × 1920, 30 i/s, H.264 + AAC (1 min 30 s de rendu).

## Texte
- [x] `python3 scripts/verifier_texte.py script.md storyboard.md audio/voix.txt publication.md index.html compositions/*.html` : OK. (`brief.md` ne signale qu'un mot interdit dans la citation d'Oba, gardée telle quelle.)
- [x] Faits : aucune réalisation, aucun chiffre de résultat, aucun délai, aucun montant de vente. Le montant de la commande (15 000 F) est un exemple d'interface.
- [x] Nom à l'écran : Obafemi / Euloge / Agnoun., trois lignes, 132 px, graisse 700.
- [x] Numéro WhatsApp : +229 01 96 25 66 94 (lu sur l'image à 27,5 s).
- [x] Voix retranscrite par ElevenLabs (scribe) sur le rendu : identique au script, « ta taille » bien entendu.

## Charte
- [x] Aucun halo, dégradé de fond, flou d'entrée de titre, emoji. Fond : le plan d'interfaces du début à la fin, incliné dans l'autre sens que les vidéos 1 à 3, assombri pendant les illustrations puis rallumé derrière la signature.
- [x] Illustrations dessinées et animées à la main, en vecteurs, sans personnage : la ville (fenêtres qui s'allument une à une), la tour qui rentre dans le sol palier par palier, le rez-de-chaussée qui devient une boutique (enseigne, auvent festonné, étagères, comptoir, fente), le téléphone qui vibre, les messages qui s'échappent et tombent, les pièces qui glissent par la fente et roulent hors de la boutique, la carte qui sort de l'écran du téléphone, les cartons qui s'empilent, les fiches clients.
- [x] Champagne, un usage par plan : le trait qui barre « grandes », les pièces (plans 3 et 5), « APP ».
- [x] Le verre a toujours quelque chose derrière : pastilles, carte, modules et signature floutent le plan d'interfaces.
- [x] Plans et transitions nouveaux par rapport aux vidéos 1 à 3 : accroche calée à gauche avec la ville, mot barré, tour qui s'enfonce, caméra qui pousse sur la boutique, entrée dans l'écran du téléphone, modules qui s'accrochent, carte qui se retourne.

## Mouvement et lecture
- [x] Test du pouce : l'image 0 réduite à 270 px reste lisible (« grandes » 220 px, soit 55 px à 270 px ; lignes de 96 px, soit 24 px) et pose l'objection. « grandes » occupe 68 % de la largeur.
- [x] Visage d'Oba : n'apparaît pas (aucune séquence, demande d'Oba).
- [x] Appel final : mot-clé APP (champagne) et raison d'écrire (« je te montre ce que ça donnerait pour ton business »).
- [x] `npx hyperframes check --json` : zéro erreur. Avertissements gardés : `nested_structure_needs_subcomposition` sur le plan d'interfaces du modèle ; `container_overflow` des textes dans leurs masques (voulu) ; reflet de la signature hors carte (voulu, masqué).
- [x] Revue sur 30 instants : corrigés le toit et l'antenne qui restaient en l'air après la descente des étages, les messages qui passaient sur l'enseigne, les pièces qui roulaient trop peu, les lettres des jours éteintes sous les jours allumés (contraste 1:1), le temps mort de 3,4 s dans la carte (la commande arrive maintenant sur « Une petite application »), les pièces qui traversaient le titre, l'antenne qui touchait « grandes » sur la miniature.
- [x] Texte entre 268 et 1330 px de haut. Infos clés à 36 px ou plus (titres 74 à 124 px, pastilles 38 à 40 px, carte 36 à 50 px, modules 40 px ; jours de la semaine 28 px, décoratifs).
- [x] Tenues : accroche 3,3 s ; « À ta taille. » 1,3 s (3 mots, dite en même temps) ; « Ce qui te fait perdre : » 3,6 s ; pastilles 1,2 et 0,6 s (un mot chacune, dits en même temps) ; titres de la phrase clé 5,9 et 4,1 s ; signature 7,1 s après l'appel.

## Son
- [x] Aucun silence de plus de 0,35 s : `silencedetect=n=-35dB:d=0.35` ne renvoie rien (la musique tient jusqu'au fondu final). Voix resserrée par `scripts/resserrer_voix.py` (blancs ramenés à 0,30 s).
- [x] Voix calée (texte / mot, écart ≤ 0,1 s) : accroche image 0 ; trait sur « Non » 2,91 ; « À ta taille. » 5,03 / « à » 5,03 ; titre 6,55 / « te fait perdre » 6,55 ; vibrations et pièces 6,87 / « perdre » 6,87 ; messages et « Commandes » 8,91 / « commandes » 8,91 ; « Paiements » 9,51 / « paiements » 9,51 ; entrée dans l'écran 10,10 / « Alors » 10,10 ; titre 10,46 / « on » 10,46 ; commande 12,92 / « Une petite » 12,89 ; « 1 fonction » 14,53 / « seule » 14,53 ; « Payé » 15,68 / « marche » 15,68 ; jours 16,02 / « tous les jours » 16,02 ; titre 16,75 / « Le reste » 16,75 ; module Stock 19,10 / « stock » 19,14 ; module Clients 20,25 / « clients » 20,29 ; retournement 21,05 / « Écris » 20,98 ; « Écris APP » 21,42 / « APP » 21,38 ; numéro 22,02 / « WhatsApp » 22,02 ; promesse 22,64 / « je » 22,64.
- [x] `npx hyperframes audio renders/pas-que-pour-les-grands.mp4 --json` : son présent, −14,3 LUFS, crête vraie −1,7 dBTP, aucun écrêtage.
- [x] Bruitages seulement sur des actions visibles (trait, étages, boutique, vibrations, pièces, entrée dans l'écran, pastille, pièces dans la carte, « Payé », modules, retournement, signature). Jamais deux fois le même fichier d'affilée.

## Mesuré, pas écouté
Personne n'a écouté le son ici. À vérifier à l'oreille par Oba : « APP » (transcrit « APP »), les chocs des étages (calés à l'œil sur les paliers, pas au son), les pièces et la vibration qui se superposent vers 6,9 s, l'équilibre voix et musique sur un téléphone.
