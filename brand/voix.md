# Voix off

- Fournisseur : ElevenLabs (secret réseau `api.elevenlabs.io` sur l'environnement cloud « ClaudeEnvironments »).
- Voix retenue : **À CHOISIR** (voir le skill `son`, section « Choisir la voix »). Une fois choisie par Oba, noter ici :
  - `voice_id` :
  - nom :
  - modèle : le plus récent qui gère le français (vérifier avec `python3 scripts/eleven.py modeles`)
  - réglages : stability 0.45, similarity_boost 0.8, style 0.25, use_speaker_boost true (à ajuster une fois, puis figer)
- Débit cible : 2,6 à 2,9 mots par seconde. 30 s de vidéo = 70 à 80 mots maximum.
- Prononciations à surveiller : « Obafemi » (o-ba-fé-mi), « AGNOUN » (a-gnoune), « Cotonou ». Si la voix les rate, les écrire phonétiquement dans le texte envoyé à ElevenLabs, jamais à l'écran.
