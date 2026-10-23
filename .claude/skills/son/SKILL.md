---
name: son
description: Voix off d'Oba (voix ElevenLabs choisie), musique originale et bruitages sur mesure via ElevenLabs, puis mixage dans HyperFrames. À utiliser pour toute piste audio d'une vidéo du studio, et pour choisir ou changer la voix.
---

# Son

Tout passe par `python3 scripts/eleven.py` (la clé vient du secret réseau ; si l'appel répond 401 ou 403, arrête-toi et dis à Oba que le secret ElevenLabs n'est pas actif sur cet environnement).

## 1. Choisir la voix (une seule fois, puis figer dans `brand/voix.md`)

1. `python3 scripts/eleven.py modeles` : retiens le modèle TTS le plus récent marqué FR.
2. `python3 scripts/eleven.py voix-candidates --n 30`, puis avec `--accent african`, `--accent nigerian`, `--accent ivorian`, `--accent cameroonian` (garder ce qui répond).
3. Écarte les voix « narration de documentaire », « publicité criée », trop graves ou trop lisses. Cherche : homme de 25 à 40 ans, accent d'Afrique de l'Ouest francophone, posé, chaleureux, conversationnel.
4. Fais lire à 3 candidates le même extrait du script (`extrait`), envoie les 3 MP3 à Oba et laisse-le choisir à l'oreille.
5. Ajoute la voix choisie au compte (`ajouter-voix`), note `voice_id`, modèle et réglages dans `brand/voix.md`. Ensuite, on ne change plus.

## 2. Voix off d'une vidéo

```bash
export ELEVEN_TTS_MODEL=<modèle de brand/voix.md>
python3 scripts/eleven.py voix <voice_id> audio/voix.txt audio/voix
```
- Écoute indirecte : vérifie la durée totale (25 à 29 s pour un 30 s) et les mots mal lus dans `voix.alignment.json`. Mot mal prononcé : réécris-le phonétiquement dans `voix.txt` seulement.
- La voix est l'horloge : recale le storyboard sur `mots[].debut`.

## 3. Musique originale

- Une piste par vidéo, instrumentale, 2 à 3 s plus longue que le film.
- Prompt type (à adapter à chaque film, jamais le même mot pour mot) : « minimal premium tech underscore, warm analog synth pads, soft sub pulse, clean muted piano motif, 96 bpm, restrained, no vocals, builds gently to a lift at 24 seconds, ends on a held chord ».
- `python3 scripts/eleven.py musique "<prompt>" 33 assets/audio/musique.mp3`, puis `npx hyperframes beats assets/audio/musique.mp3` pour caler les poses fortes (arrivée de la carte, signature) sur les temps.

## 4. Bruitages sur mesure

Seulement sur une action visible (voir le storyboard). Exemples de descriptions :
- carte de verre qui se pose : « soft glass panel sliding into place, airy, short, high-end UI sound, no click » (0,8 s)
- pastille : « tiny soft glass tick, minimal UI, very short » (0,3 s)
- chiffre qui s'arrête : « subtle soft digital settle, premium, very short » (0,4 s)
- signature : « elegant soft riser into a gentle low impact, premium, restrained » (2 s)
Génère 2 variantes pour un son répété et alterne-les.

## 5. Mixage (dans la composition HyperFrames)

- Chaque piste est un `<audio id=…>` placé au bon `data-start`. Lis `/media-use` (`references/mixing.md`).
- Niveaux : voix pleine, musique autour de 0,14 sous la voix et 0,35 sans voix, bruitages 3 à 6 dB au-dessus du lit.
- Un bruitage tombe une image après son action visuelle.
- Mix final autour de −14 LUFS, crête vraie ≤ −1 dBTP : `npx hyperframes normalize-audio`, puis contrôle avec `npx hyperframes audio renders/<slug>.mp4 --json`.
