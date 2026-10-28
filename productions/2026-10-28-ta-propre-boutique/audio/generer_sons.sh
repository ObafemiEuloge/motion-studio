#!/bin/bash
# Musique et bruitages de la vidéo 6 (ElevenLabs via scripts/eleven.py)
E=../../scripts/eleven.py
python3 $E musique "Premium minimal tech product film score, like a calm keynote: soft felt piano motif, warm analog pads, gentle muted pulse, light glassy plucks, restrained and emotional in the first half, slowly opening and confident in the second half, steady energy from the first second to the very end, no build-down, no fade out, no silence, 90 bpm, instrumental" 102 assets/audio/musique.mp3
python3 $E bruitage "soft premium smartphone notification chime, single, clean, clearly audible" 1.0 audio/brut/notif.mp3
python3 $E bruitage "clean soft slicing sound of a sharp blade through paper, short, close, clearly audible" 0.7 audio/brut/coupe.mp3
python3 $E bruitage "a few coins sliding away and dropping softly, short, clean, clearly audible" 1.2 audio/brut/pieces.mp3
python3 $E bruitage "soft quiet mechanical keyboard typing, steady, close microphone, clearly audible" 3.0 audio/brut/clavier.mp3
python3 $E bruitage "small key turning in a lock then a soft click, clean, close, clearly audible" 0.9 audio/brut/cle.mp3
python3 $E bruitage "delicate sparkle of many tiny soft glass ticks spreading, short, airy, clearly audible" 1.4 audio/brut/points.mp3
python3 $E bruitage "warm positive soft chime, two gentle notes rising, premium, clearly audible" 1.2 audio/brut/resultat.mp3
python3 $E bruitage "soft smooth airy flow sound moving left to right, gentle, short, no whoosh hit" 1.0 audio/brut/flux.mp3
python3 $E bruitage "soft glass panel settling into place, airy, short, premium interface sound" 0.8 audio/brut/verre.mp3
echo FIN
