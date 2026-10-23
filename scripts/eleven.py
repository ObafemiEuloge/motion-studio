#!/usr/bin/env python3
"""Outil ElevenLabs du studio.

La clé n'est jamais dans ce fichier : dans l'environnement cloud, le proxy ajoute
l'en-tête xi-api-key aux requêtes vers api.elevenlabs.io (secret réseau). En local,
on peut définir ELEVENLABS_API_KEY.

Commandes :
  modeles                                   liste les modèles TTS et leurs langues
  voix-candidates [--accent X] [--n 12]     cherche des voix masculines francophones dans la bibliothèque
  ajouter-voix PUBLIC_USER_ID VOICE_ID NOM  ajoute une voix de la bibliothèque au compte
  extrait VOICE_ID TEXTE SORTIE.mp3         lit un texte (sans horodatage), pour comparer des voix
  voix VOICE_ID FICHIER_TEXTE SORTIE        voix off + horodatage : SORTIE.mp3 et SORTIE.alignment.json
  bruitage "DESCRIPTION" DUREE SORTIE.mp3   effet sonore (0,5 à 30 s)
  musique "PROMPT" DUREE_S SORTIE.mp3       musique instrumentale sur mesure
"""
import base64, json, os, sys, time
import requests

API = "https://api.elevenlabs.io"
TIMEOUT = 300


def _headers():
    h = {"Content-Type": "application/json"}
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key:
        h["xi-api-key"] = key
    return h


def _req(method, path, **kw):
    for attempt in range(3):
        r = requests.request(method, API + path, headers=_headers(), timeout=TIMEOUT, **kw)
        if r.status_code in (429, 500, 502, 503) and attempt < 2:
            time.sleep(4 * (attempt + 1))
            continue
        if r.status_code >= 400:
            sys.exit(f"ElevenLabs {r.status_code} sur {path} : {r.text[:400]}")
        return r


def modeles():
    for m in _req("GET", "/v1/models").json():
        if not m.get("can_do_text_to_speech"):
            continue
        langs = ",".join(l.get("language_id", "") for l in m.get("languages", []))
        fr = "FR" if "fr" in langs.split(",") else "  "
        print(f"{fr}  {m['model_id']:<32} {m.get('name','')}")


def voix_candidates(accent=None, n=12):
    params = {"gender": "male", "language": "fr", "page_size": 100, "sort": "trending"}
    if accent:
        params["accent"] = accent
    data = _req("GET", "/v1/shared-voices", params=params).json()
    voices = data.get("voices", [])
    out = []
    for v in voices:
        out.append({
            "nom": v.get("name"), "voice_id": v.get("voice_id"), "public_owner_id": v.get("public_owner_id"),
            "accent": v.get("accent"), "age": v.get("age"), "locale": v.get("locale"),
            "usage": v.get("use_case"), "description": (v.get("description") or "")[:160],
            "apercu": v.get("preview_url"), "clones": v.get("cloned_by_count"),
        })
    print(json.dumps(out[:n], ensure_ascii=False, indent=1))


def ajouter_voix(public_user_id, voice_id, nom):
    r = _req("POST", f"/v1/voices/add/{public_user_id}/{voice_id}", json={"new_name": nom})
    print(r.json())


def _tts_body(texte, model_id, seed):
    return {
        "text": texte,
        "model_id": model_id,
        "language_code": "fr",
        "seed": seed,
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.8, "style": 0.25, "use_speaker_boost": True},
    }


def extrait(voice_id, texte, sortie, model_id=None):
    model_id = model_id or os.environ.get("ELEVEN_TTS_MODEL", "eleven_multilingual_v2")
    r = _req("POST", f"/v1/text-to-speech/{voice_id}", params={"output_format": "mp3_44100_128"},
             json=_tts_body(texte, model_id, 7))
    open(sortie, "wb").write(r.content)
    print(sortie)


def voix(voice_id, fichier_texte, sortie, model_id=None):
    model_id = model_id or os.environ.get("ELEVEN_TTS_MODEL", "eleven_multilingual_v2")
    texte = open(fichier_texte, encoding="utf-8").read().strip()
    r = _req("POST", f"/v1/text-to-speech/{voice_id}/with-timestamps",
             params={"output_format": "mp3_44100_128"}, json=_tts_body(texte, model_id, 7))
    d = r.json()
    open(sortie + ".mp3", "wb").write(base64.b64decode(d["audio_base64"]))
    al = d.get("alignment") or {}
    chars, starts, ends = al.get("characters", []), al.get("character_start_times_seconds", []), al.get("character_end_times_seconds", [])
    mots, cur, t0 = [], "", None
    for c, s, e in zip(chars, starts, ends):
        if c.isspace():
            if cur:
                mots.append({"mot": cur, "debut": round(t0, 3), "fin": round(prev_e, 3)})
            cur, t0 = "", None
            continue
        if t0 is None:
            t0 = s
        cur += c
        prev_e = e
    if cur:
        mots.append({"mot": cur, "debut": round(t0, 3), "fin": round(prev_e, 3)})
    json.dump({"modele": model_id, "voice_id": voice_id, "mots": mots, "brut": al}, open(sortie + ".alignment.json", "w"), ensure_ascii=False, indent=1)
    print(sortie + ".mp3", sortie + ".alignment.json", f"{len(mots)} mots, fin {mots[-1]['fin'] if mots else 0} s")


def bruitage(description, duree, sortie):
    r = _req("POST", "/v1/sound-generation", params={"output_format": "mp3_44100_128"},
             json={"text": description, "duration_seconds": float(duree), "prompt_influence": 0.6, "model_id": "eleven_text_to_sound_v2"})
    open(sortie, "wb").write(r.content)
    print(sortie)


def musique(prompt, duree_s, sortie):
    body = {"prompt": prompt, "music_length_ms": int(float(duree_s) * 1000), "force_instrumental": True}
    model = os.environ.get("ELEVEN_MUSIC_MODEL")
    if model:
        body["model_id"] = model
    r = _req("POST", "/v1/music", json=body)
    open(sortie, "wb").write(r.content)
    print(sortie)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd, args = a[0], a[1:]
    if cmd == "modeles":
        modeles()
    elif cmd == "voix-candidates":
        acc = args[args.index("--accent") + 1] if "--accent" in args else None
        n = int(args[args.index("--n") + 1]) if "--n" in args else 12
        voix_candidates(acc, n)
    elif cmd == "ajouter-voix":
        ajouter_voix(*args[:3])
    elif cmd == "extrait":
        extrait(*args[:3])
    elif cmd == "voix":
        voix(*args[:3])
    elif cmd == "bruitage":
        bruitage(*args[:3])
    elif cmd == "musique":
        musique(*args[:3])
    else:
        sys.exit(__doc__)
