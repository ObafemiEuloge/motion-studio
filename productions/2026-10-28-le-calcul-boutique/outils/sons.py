"""Place les bruitages dans index.html (entre <!--SONS--> et <!--/SONS-->).

Chaque ligne : (début en s, fichier, volume). Pistes 23 et 24 en alternance.
Usage : python3 outils/sons.py
"""
import pathlib, re, subprocess
ici = pathlib.Path(__file__).resolve().parent.parent
SONS = [
    (0.20, "notif", 0.3),      # le flux de paiements (image 0)
    (2.73, "tambour", 0.4),    # 2 000 000
    (4.57, "coupe", 0.35),     # − 300 000
    (5.70, "croc", 0.4),       # les mois croqués
    (6.45, "verre", 0.35),     # ta boutique
    (7.97, "flux", 0.3),       # l'anneau se remplit
    (9.73, "tic_a", 0.3),      # Mobile Money
    (10.61, "tic_b", 0.3),     # Carte
    (11.61, "piliers", 0.4),   # 17 piliers
    (13.17, "tambour", 0.35),  # 3 000 000
    (14.98, "coupe", 0.3),     # le bloc se détache
    (15.46, "resultat", 0.4),  # + 175 000 F
    (18.29, "touche", 0.3),    # tonnom.com
    (19.17, "cartes", 0.4),    # trois semaines
    (20.05, "signature", 0.4), # la signature
]
# La nouvelle première phrase décale de 1,34 s tout ce qui suit 1,5 s (temps ci-dessus = prise v1)
DECALAGE = 0
lignes, piste, prec = [], 23, None
for i, (t, f, v) in enumerate(SONS):
    t = round(t + DECALAGE, 2) if t > 1.5 else t
    assert f != prec, f"{f} deux fois d'affilée à {t}"
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                              str(ici / "assets/audio" / (f + ".mp3"))], capture_output=True, text=True).stdout)
    lignes.append(f'      <audio id="sfx-{i:02d}-{f}" class="clip" data-start="{t}" data-duration="{d:.2f}" data-track-index="{piste}" data-volume="{v}" src="assets/audio/{f}.mp3"></audio>')
    piste, prec = (24 if piste == 23 else 23), f
p = ici / "index.html"; s = p.read_text()
s = re.sub(r"<!--SONS-->.*?(<!--/SONS-->|\n    </div>)", lambda m: "<!--SONS-->\n" + "\n".join(lignes) + "\n      <!--/SONS-->" + ("" if m.group(1) == "<!--/SONS-->" else "\n    </div>"), s, flags=re.S)
p.write_text(s); print(len(lignes), "bruitages placés")
