# Assemble la voix v2 : python3 audio/v2/assembler_voix.py <dossier de production>, puis nivelle (acompressor puis loudnorm à -16 LUFS, voir brand/voix.md).
import json, subprocess, sys, os
P = sys.argv[1]  # dossier de production
A = os.path.join(P, "audio")
SR = 44100
segs = [  # (source, debut, fin, blanc_avant[, gain_dB]) ; aucun blanc au-delà de 0,35 s
    ("v1", 0.00, 1.45, 0.0),    # « Mais j'ai déjà payé hein ! »
    ("v1", 1.72, 2.22, 0.0),    # [soupir]
    ("v1", 4.28, 7.17, 0.05),   # Tu fouilles WhatsApp… capture par capture.
    ("v1", 7.48, 10.62, 0.15),  # Le cahier dit une chose, le Mobile Money autre chose.
    ("v1", 11.67, 11.90, 0.10, 10), # Bon. (murmuré dans la prise : remonté de 10 dB)
    ("v1", 12.28, 14.30, 0.12), # Une application peut faire ça à ta place.
    ("v1", 14.52, 15.34, 0.10), # Le client paie,
    ("v1", 15.60, 17.43, 0.08), # et la commande passe à « payé ».
    ("v1", 17.85, 18.45, 0.20), # Toute seule.
    ("benefice", 0.00, 2.00, 0.10),  # Le soir, tu fermes la boutique…
    ("benefice", 2.50, 3.76, 0.22),  # les comptes sont déjà faits.
    ("preuve", 0.00, 4.48, 0.15),    # Sur Un Peu Un Peu, chaque paiement est vérifié…
    ("appel_a", 0.00, 4.38, 0.10),   # Écris APP sur WhatsApp, je te montre…
]
src = {"v1": os.path.join(A, "v2", "v1_source.mp3"), "benefice": os.path.join(A, "v2", "benefice.mp3"),
       "preuve": os.path.join(A, "v2", "preuve.mp3"), "appel_a": os.path.join(A, "v2", "appel_a.mp3")}
alig = {k: json.load(open(v[:-4] + ".alignment.json"))["mots"] for k, v in src.items()}
parts, mots, t = [], [], 0.0
tmp = os.path.join(A, "v2", "tmp"); os.makedirs(tmp, exist_ok=True)
for i, seg in enumerate(segs):
    s, d, f, blanc = seg[:4]; gain = seg[4] if len(seg) > 4 else 0
    if blanc:
        p = os.path.join(tmp, f"blanc{i}.wav")
        subprocess.check_call(["ffmpeg","-v","error","-y","-f","lavfi","-i",f"anullsrc=r={SR}:cl=mono","-t",f"{blanc}",p]); parts.append(p); t += blanc
    p = os.path.join(tmp, f"seg{i}.wav"); dur = f - d
    subprocess.check_call(["ffmpeg","-v","error","-y","-ss",f"{d}","-t",f"{dur}","-i",src[s],"-ac","1","-ar",str(SR),
        "-af",f"volume={gain}dB,afade=t=in:d=0.008,afade=t=out:st={dur-0.012:.3f}:d=0.012",p]); parts.append(p)
    for m in alig[s]:
        if d - 0.001 <= m["debut"] < f:
            mots.append({"mot": m["mot"], "debut": round(t + m["debut"] - d, 3), "fin": round(t + min(m["fin"], f) - d, 3)})
    t += dur
liste = os.path.join(tmp, "liste.txt")
open(liste, "w").write("".join(f"file '{p}'\n" for p in parts))
brut = os.path.join(tmp, "voix_brute.wav")
subprocess.check_call(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",liste,"-c","copy",brut])
json.dump({"modele": "eleven_v4", "voice_id": "cEjGxRhK5rId1bacJPJr", "assemblage": "v2 : prise du 23 oct. recoupée + 3 phrases régénérées", "mots": mots},
          open(os.path.join(A, "voix.alignment.json"), "w"), ensure_ascii=False, indent=1)
print(f"{len(mots)} mots, fin {mots[-1]['fin']} s, total {t:.2f} s")
print(brut)
