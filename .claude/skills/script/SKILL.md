---
name: script
description: Écrit le script d'une vidéo d'Oba (voix off + textes à l'écran) dans un français parlé, humain, sans tournures de texte généré. À utiliser après le brief, avant le storyboard.
---

# Script

Sortie : `script.md` dans le dossier de production, avec deux colonnes par temps : **VOIX** (ce qui est dit) et **ÉCRAN** (ce qui s'affiche). Puis `audio/voix.txt` = la voix seule, en un bloc, prête pour ElevenLabs.

## La structure d'un 30 s (70 à 80 mots dits, pas un de plus)

| Temps | Durée | Rôle | Règle |
|---|---|---|---|
| Accroche | 0 à 2 s | arrêter le pouce | une situation que la personne vit, ou une phrase qui contredit ce qu'elle croit. Lisible sans le son dès l'image 0 |
| Le frottement | 2 à 8 s | « c'est moi » | un détail concret de son quotidien (le cahier, les captures WhatsApp, l'Excel qui plante), pas une généralité |
| Le basculement | 8 à 18 s | ce qui change | ce que fait l'application, montré à l'écran, dit avec des verbes d'action |
| La preuve | 18 à 25 s | crédibilité | UN fait de `brand/faits.md`, dit simplement |
| L'appel | 25 à 30 s | agir | « Écris-moi sur WhatsApp », le numéro à l'écran, et la signature Obafemi Euloge AGNOUN |

## Écrire comme Oba parle

- Tutoiement. Phrases de 4 à 12 mots. Une idée par phrase.
- Le concret avant l'abstrait : « tu notes tes commandes dans un cahier » plutôt que « ta gestion manque d'efficacité ».
- Des mots qu'on dit à Cotonou, pas des mots de plaquette. « Ton business », « tes clients », « ça te coûte des ventes ».
- Le rythme vient des longueurs variées : une phrase courte. Puis une un peu plus longue qui explique. Puis une très courte.
- Au moins une phrase qui ne pourrait être écrite par personne d'autre (Cotonou, Mobile Money, un projet réel).
- Le texte à l'écran ne répète pas la voix mot pour mot : il en garde 2 à 5 mots clés, ou montre ce que la voix décrit.

## Ce qui fait vendre (leçons de la vidéo 1, 23 oct. 2026)

- **L'appel donne une raison d'écrire maintenant et un geste minuscule** : « Écris APP sur WhatsApp, je te montre ce que ça donnerait pour ton business. » Un mot-clé par offre (APP, PAGE, MOTION) : Oba sait d'où vient chaque contact.
- **La preuve se dit en résultat pour le client, pas en nom de projet** : « Sur 1Peu 1Peu, chaque paiement est vérifié sans que personne ne regarde. » Le nom seul ne dit rien à la cible.
- **Le bénéfice final est concret et visible** : ce que la personne fait de son temps ou de son argent une fois l'application là (« le soir, tu fermes la boutique, les comptes sont déjà faits »).
- Pas plus de 2 phrases sur le problème avant de montrer la solution : au-delà, le spectateur décroche.

## Interdits (en plus de `scripts/verifier_texte.py`)

- Aucun tiret cadratin ni demi-cadratin. Aucun emoji.
- Pas de questions rhétoriques en série (« Et si… ? Et si… ? »).
- Pas de triades automatiques (« simple, rapide, efficace »).
- Pas de « Imagine… », « Découvre… », « Dans un monde où… », « Le secret… », « Révolutionner ».
- Aucun prix, aucune promesse chiffrée inventée, aucune garantie.
- Pas de superlatifs vides (« le meilleur », « unique », « incroyable »).

## Relecture obligatoire

1. Lis la voix à voix haute en chronométrant (ou compte : 2,7 mots par seconde). Plus de 80 mots : coupe.
2. Pour chaque phrase : « Oba le dirait-il comme ça à un client autour d'un café ? » Sinon, réécris.
3. `python3 scripts/verifier_texte.py script.md audio/voix.txt` doit afficher OK.
4. Propose deux accroches différentes dans `script.md` et indique laquelle tu retiens et pourquoi.
