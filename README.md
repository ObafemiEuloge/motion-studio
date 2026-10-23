# motion-studio

Studio de production des vidéos motion d'**Obafemi Euloge AGNOUN** : Reels et TikTok premium (verre dépoli, typographie Apple, interfaces réelles), voix off, musique et bruitages sur mesure, écrits et montés avec Claude et [HyperFrames](https://hyperframes.heygen.com).

## Faire une vidéo

Dans une session Claude ouverte sur ce dépôt, dans l'environnement cloud qui porte le secret ElevenLabs :

```
/produire Offre : application sur mesure. Cible : un commerçant qui gère tout sur WhatsApp. Preuve : Centime. Séquence : aucune.
```

Claude enchaîne : brief, script, storyboard, voix, motion, musique et bruitages, contrôle, rendu, légende. Tu reçois le MP4, la couverture et la légende.

## Ce qu'il y a dedans

| Dossier | Rôle |
|---|---|
| `brand/` | charte visuelle, faits vérifiés, voix, polices |
| `.claude/skills/` | les étapes du studio, une par skill |
| `templates/base/` | projet HyperFrames de départ, charte déjà câblée |
| `references/` | vidéos validées : le niveau minimum |
| `sources/` | index et extraits préparés des séquences filmées |
| `scripts/` | ElevenLabs (voix, musique, bruitages) et vérification du texte |
| `productions/` | une vidéo par dossier (les rendus MP4 ne sont pas versionnés) |

Aucune clé n'est stockée ici : ElevenLabs est appelé via un secret réseau de l'environnement.
