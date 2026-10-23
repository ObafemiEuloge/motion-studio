#!/usr/bin/env python3
"""Vérifie un texte (script, légende, HTML) avant livraison.

Usage : python3 scripts/verifier_texte.py fichier [fichier ...]
Sort en erreur si un interdit est trouvé.
"""
import re, sys

INTERDITS = {
    "—": "tiret cadratin",
    "–": "tiret demi-cadratin",
}
# Tournures qui sonnent « texte généré ». Liste vivante : ajouter ce qu'Oba refuse.
CLICHES = [
    r"dans un monde o[uù]", r"\bplong(e|eons|ez) dans\b", r"\bà l'ère (du|de la|des)\b", r"\bincontournable\b",
    r"\brévolutionn", r"\bsans plus attendre\b", r"\bboost(e|er|ez)\b", r"\bgame.?changer\b", r"\bn'attends plus\b",
    r"\bfais passer .* au niveau supérieur\b", r"\bpas seulement\b.*\bmais aussi\b", r"\bdécouvre(z)? comment\b",
    r"\bsolution(s)? innovante", r"\bdigitalis", r"\bvéritable\b", r"\bunique en son genre\b", r"\ble secret\b",
    r"\b3 ans de python\b", r"\bspyral\b", r"\bfcfa\b|\bprix\b|\btarif\b",
]


def verifier(chemin):
    texte = open(chemin, encoding="utf-8").read()
    pb = []
    for car, nom in INTERDITS.items():
        if car in texte:
            pb.append(f"{nom} trouvé ({texte.count(car)} fois)")
    bas = texte.lower()
    for motif in CLICHES:
        m = re.search(motif, bas)
        if m:
            pb.append(f"tournure à éviter : « {m.group(0)} »")
    return pb


if __name__ == "__main__":
    total = 0
    for f in sys.argv[1:]:
        for p in verifier(f):
            print(f"{f} : {p}")
            total += 1
    if total:
        sys.exit(1)
    print("OK : aucun interdit trouvé.")
