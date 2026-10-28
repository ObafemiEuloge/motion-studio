"""Assemble scenes/*.html en compositions/*.html : insère le style et le script communs.

Usage : python3 outils/assembler.py
"""
import pathlib
ici = pathlib.Path(__file__).resolve().parent.parent
css = (ici / "scenes/_commun.css").read_text()
js = (ici / "scenes/_commun.js").read_text()
import json
carte = json.loads((ici / "outils/carte.json").read_text())
cercles = "".join(f'<circle class="pt" cx="{x}" cy="{y}" r="4" />' for x, y in carte["points"])
allumes = json.dumps([carte["points"][i] for i in carte["allumes"]])
for src in sorted((ici / "scenes").glob("*.html")):
    s = src.read_text().replace("/*COMMUN*/", css).replace("//COMMUN", js).replace("@@CARTE@@", cercles).replace("@@ALLUMES@@", allumes)
    (ici / "compositions" / src.name).write_text(s)
    print("compositions/" + src.name)
