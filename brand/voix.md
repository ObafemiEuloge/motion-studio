# Voix off

- Fournisseur : ElevenLabs (secret réseau `api.elevenlabs.io` sur l'environnement cloud « ClaudeEnvironments »).
- Voix retenue par Oba le 23 oct. 2026, à l'oreille, parmi 6 candidates (`productions/2026-10-23-app-sur-mesure/audio/candidates/`) :
  - `voice_id` : `cEjGxRhK5rId1bacJPJr` (ajoutée au compte sous le nom « Bakumba (voix d'Oba) »)
  - nom : Bakumba, voix masculine moyenne-grave, accent sénégalais, conversationnelle
  - modèle : `eleven_v4`
  - réglages : stability 0.45, similarity_boost 0.8, style 0.25, use_speaker_boost true, seed 7 (ceux de `scripts/eleven.py`)
- Débit cible : 2,6 à 2,9 mots par seconde. 30 s de vidéo = 70 à 80 mots maximum, moins s'il y a des pauses.
- Jeu : `eleven_v4` comprend les indications entre crochets dans `audio/voix.txt` : `[sighs]`, `[pause]`, `[laughs softly]`. Vérifié par transcription : elles sont jouées, pas lues. Les points de suspension marquent une hésitation courte. Ces indications n'existent que dans `voix.txt`, jamais à l'écran.
- Prononciations à surveiller : « Obafemi » (o-ba-fé-mi), « AGNOUN » (a-gnoune), « 1Peu 1Peu » (écrire « Un Peu Un Peu »). Si la voix les rate, les écrire phonétiquement dans le texte envoyé à ElevenLabs, jamais à l'écran.
- Blancs : aucun blanc de plus de 0,35 s dans la voix finale (`silencedetect=n=-35dB:d=0.35`). Si la prise en contient, recouper la prise phrase par phrase avec l'alignement et recoller avec des blancs de 0,1 à 0,22 s (automatique : `python3 scripts/resserrer_voix.py audio/prise audio/voix --max 0.22` ; à la main pour mélanger deux prises : `productions/2026-10-23-app-sur-mesure/audio/v2/assembler_voix.py`). Pour changer une phrase, ne régénérer que celle-là.
- Nivellement avant mixage : `acompressor=threshold=-26dB:ratio=2.5:attack=8:release=120` puis `loudnorm=I=-16:TP=-1.5:LRA=9` en deux passes (linéaire) vers `audio/voix_mix.mp3`. La voix murmurée d'un mot isolé (« Bon. ») peut demander +10 dB sur ce seul morceau.
