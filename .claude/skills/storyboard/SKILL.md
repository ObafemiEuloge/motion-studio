---
name: storyboard
description: Découpe le script d'Oba en plans minutés au dixième de seconde, dans la grammaire visuelle de la charte. À utiliser après le script, puis une seconde fois quand la voix est générée pour caler les plans sur les mots réels.
---

# Storyboard

Sortie : `storyboard.md`. Un tableau, un plan par ligne : `# | début | fin | voix (mots) | à l'écran | mouvement | son`.

## La grammaire du studio (tirée de l'ident v3 validé)

Plans disponibles. Varie : jamais deux fois le même type d'entrée à la suite.

1. **Titre sur le monde** : titre Plus Jakarta 700 qui monte depuis un cache, au-dessus du plan d'interfaces 3D qui défile.
2. **Carte de verre** : une carte de verre monte et se pose, son contenu monte ligne par ligne. Le verre floute de vraies interfaces derrière.
3. **Interface qui travaille** : une vraie interface (capture de Centime, tableau de bord, formulaire) dans un cadre de verre ; un élément change (un statut passe à « Payé », un chiffre compte, une ligne s'ajoute). Plan long (4 à 7 s), le mouvement est dans l'interface.
4. **Chiffre qui compte** : un chiffre vérifié compte jusqu'à sa valeur, une étiquette sous lui.
5. **Pastilles** : 2 à 4 pastilles de verre arrivent à 70 ms d'écart (Web, Mobile, Back-office, Mobile Money…).
6. **Oba à l'écran** : un extrait de `sources/selects/` dans une carte arrondie, étalonné, jamais plein écran brut.
7. **Signature finale** : la carte de l'ident v3 (nom, trait, promesse, pastilles), puis la ligne WhatsApp avec le numéro. Tenue au moins 2,5 s.

## Transitions (3 à 5 sortes par film, chacune causée par l'image)

- La carte de verre grandit jusqu'à devenir le plan suivant.
- Le titre repart dans son cache vers le haut pendant que le suivant monte (enchaînement de caches).
- Coupe franche sur le pic de vitesse d'un mouvement.
- Le plan d'interfaces change d'angle (rotation lente de la caméra, 3 à 5° par seconde).

## Rythme

- **L'image 0 est l'accroche en très grand** : 120 px minimum, 60 % de la largeur au moins, au centre de la bande lisible. Une bulle de message seule, petite, ne suffit pas.
- **Jamais un trou de son ou d'image de plus de 0,35 s** entre deux phrases.
- **Les infos clés à 36 px minimum** (montants, statuts, la preuve). Les détails d'interface peuvent être plus petits, mais rien d'important.
- **Le fond reste le monde de la charte** (plan d'interfaces, `ground`). Une séquence d'Oba ne sert jamais de fond flou : soit son visage est net et éclairé dans une carte, soit on ne l'utilise pas.

- Un nouveau temps toutes les 2 à 4 s, plans de 1 à 3 s, sauf le plan « interface qui travaille ».
- Le texte arrive sur le mot qui le dit (après la voix : recaler chaque début sur `audio/voix.alignment.json`).
- Tenue d'une ligne à lire : 0,5 s + 0,3 s par mot.
- Tout le texte dans la bande 168 à 1330 px de haut. Rien sous 1330 px sauf du décor.
- Image 0 = l'accroche déjà lisible. Jamais un écran vide ni le nom en ouverture.

## Le format long (60 à 120 s)

- Un chapitre = un monde de fond différent, choisi pour l'histoire (la vitrine encombrée de la plateforme, sa propre boutique, une carte, l'atelier…), toujours fait de vraies interfaces ou d'illustrations au trait, jamais un décor abstrait. On change de monde par une transition causée par l'image.
- Chaque chapitre a son plan clé, plus long, où une interface ou une illustration travaille (4 à 8 s).
- Les séquences d'Oba se placent sur un mot précis qui les justifie (« je l'ai déjà construit » sur ses mains au clavier), 2 à 4 s chacune, dans une carte, jamais en fond.
- Le calcul se pose ligne par ligne, chaque ligne sur le mot qui la dit ; le résultat arrive seul, en très grand.
- Pas plus de 2 éléments de texte nouveaux à lire en même temps.

## Son prévu par plan

Dans la colonne son : seulement les actions visibles (une carte qui se pose = souffle doux, un chiffre qui s'arrête = petit clic, une pastille = tic léger, la signature = une seule montée). Pas de son sur chaque coupe.
