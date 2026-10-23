#!/bin/bash
# Bruitages et musique de la vidéo 5 (ElevenLabs via scripts/eleven.py)
set -e
E=../../scripts/eleven.py
python3 $E bruitage "graphite pencil sketching quick precise lines on thick paper, close, dry, soft" 1.6 audio/brut/crayon.mp3
python3 $E bruitage "soft glassy shimmer reveal, gentle airy sparkle, short, clean, no whoosh" 1.0 audio/brut/revele.mp3
python3 $E bruitage "soft flowing liquid chime splitting into four gentle tones, delicate, clean" 1.5 audio/brut/courants.mp3
python3 $E bruitage "single soft tap on a smartphone glass keypad, subtle haptic click" 0.5 audio/brut/touche.mp3
python3 $E bruitage "soft paper sheet sliding up on a smooth table, short, subtle" 0.7 audio/brut/feuille.mp3
python3 $E bruitage "soft rising bell tone completing a circle, warm, gentle, short" 1.2 audio/brut/anneau.mp3
python3 $E bruitage "two thin glass cards sliding past each other, soft click at the end" 0.8 audio/brut/cartes.mp3
python3 $E bruitage "tiny precise mechanical click of a ruler snapping into place, very subtle" 0.5 audio/brut/declic.mp3
python3 $E musique "Warm, premium, minimal product film score. Soft felt piano motif over a gentle muted pulse and warm sub bass, light airy pads, subtle plucked synth arpeggio, confident and calm, steady from the first second to the very end, no build-down, no fade out, no silence, 92 bpm, instrumental" 30 assets/audio/musique.mp3
