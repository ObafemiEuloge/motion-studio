"""Place les bruitages dans index.html (entre <!--SONS--> et <!--/SONS-->).

Chaque ligne : (début en s, fichier, volume). Pistes 23 et 24 en alternance.
Usage : python3 outils/sons.py
"""
import pathlib, re, subprocess
ici = pathlib.Path(__file__).resolve().parent.parent
SONS = [
    (0.25, "notif", 0.35),       # la vente arrive (image 0)
    (3.96, "coupe", 0.4),        # « sert » : la part est découpée
    (7.40, "tic_a", 0.3),        # « vidéos »
    (8.36, "tic_b", 0.3),        # « fiches »
    (9.32, "touche", 0.3),       # « nuits »
    (11.55, "verre", 0.35),      # la formation se pose dans la vitrine
    (14.68, "tic_a", 0.3),       # coche « Prête vite »
    (16.48, "tic_b", 0.3),       # coche « Mobile Money »
    (17.56, "touche", 0.3),      # coche « Plusieurs pays »
    (20.25, "pieces", 0.35),     # « garde sa part »
    (21.42, "chiffre_a", 0.3),   # 5 %, 10 %, 15 %
    (27.28, "notif", 0.3),       # la barre des 2 000 000
    (28.66, "coupe", 0.35),      # la part se détache
    (30.10, "pieces", 0.35),     # « partent »
    (32.53, "tic_a", 0.3),       # la publicité
    (37.20, "verre", 0.35),      # la boutique apparaît
    (43.95, "points", 0.35),     # les pays s'allument
    (47.25, "cle", 0.4),         # la clé
    (52.95, "tic_b", 0.3),       # « au franc près »
    (54.00, "flux", 0.35),       # l'argent part du client
    (57.86, "paye", 0.4),        # « chez toi »
    (58.93, "tic_a", 0.3),       # Produits
    (59.65, "tic_b", 0.3),       # Ventes
    (60.45, "touche", 0.3),      # Clients
    (63.80, "flux", 0.3),        # la courbe qui monte
    (66.00, "chiffre_a", 0.3),   # 3 000 000
    (67.80, "tic_b", 0.3),       # barre plateforme
    (69.61, "tic_a", 0.3),       # barre boutique
    (73.41, "resultat", 0.4),    # + 175 000 F
    (76.86, "chiffre_a", 0.3),   # + 2 100 000 F
    (78.70, "clavier", 0.3),     # ses mains au clavier
    (82.60, "tic_b", 0.25),      # paiements vérifiés
    (83.72, "paye", 0.35),       # « vérifié »
    (86.17, "anneau", 0.35),     # 3 semaines
    (88.45, "touche", 0.3),      # « avec toi »
    (90.40, "signature", 0.4),   # la signature
]
# La nouvelle première phrase décale de 1,34 s tout ce qui suit 1,5 s (temps ci-dessus = prise v1)
DECALAGE = 1.34
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
