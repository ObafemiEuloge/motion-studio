#!/usr/bin/env python3
"""Ramène chaque blanc d'une voix off à une durée maximale et recale l'alignement.

Usage : python3 scripts/resserrer_voix.py ENTREE (sans extension) SORTIE (sans extension) [--max 0.22]
Lit ENTREE.mp3 et ENTREE.alignment.json (sortie de `eleven.py voix`), écrit SORTIE.mp3 et SORTIE.alignment.json.
Un blanc = moins de -35 dB pendant au moins 0,25 s. On garde les bords du blanc (souffle, fin de mot)
et on retire le milieu.
"""
import json, re, subprocess, sys


def blancs(chemin):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", chemin, "-af", "silencedetect=n=-35dB:d=0.25",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    debuts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    fins = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    return list(zip(debuts, fins))


def duree(chemin):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", chemin]).decode())


def main():
    args = sys.argv[1:]
    entree, sortie = args[0], args[1]
    maxi = float(args[args.index("--max") + 1]) if "--max" in args else 0.22
    total = duree(entree + ".mp3")
    coupes = []  # (debut, fin) des morceaux retirés
    for d, f in blancs(entree + ".mp3"):
        if f >= total - 0.01 or d <= 0.01:
            continue
        if f - d > maxi:
            coupes.append((d + maxi / 2, f - maxi / 2))
    gardes, t = [], 0.0
    for d, f in coupes:
        gardes.append((t, d)); t = f
    gardes.append((t, total))
    filtres = []
    for i, (d, f) in enumerate(gardes):
        filtres.append(f"[0:a]atrim={d:.3f}:{f:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.006,"
                       f"afade=t=out:st={max(0, f - d - 0.008):.3f}:d=0.008[a{i}]")
    filtres.append("".join(f"[a{i}]" for i in range(len(gardes))) + f"concat=n={len(gardes)}:v=0:a=1[out]")
    subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-i", entree + ".mp3", "-filter_complex", ";".join(filtres),
                           "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k", sortie + ".mp3"])

    def recale(x):
        retire = 0.0
        for d, f in coupes:
            if x >= f:
                retire += f - d
            elif x > d:
                retire += x - d
        return round(x - retire, 3)

    al = json.load(open(entree + ".alignment.json"))
    for m in al["mots"]:
        m["debut"], m["fin"] = recale(m["debut"]), recale(m["fin"])
    al.pop("brut", None)
    al["resserre"] = {"max_blanc_s": maxi, "retire_s": round(sum(f - d for d, f in coupes), 3), "coupes": coupes}
    json.dump(al, open(sortie + ".alignment.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(coupes)} blancs resserrés, {al['resserre']['retire_s']} s retirées, durée {duree(sortie + '.mp3'):.2f} s")


if __name__ == "__main__":
    main()
