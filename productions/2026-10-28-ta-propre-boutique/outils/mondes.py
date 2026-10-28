"""Génère les trois mondes de fond (scenes/vitrine.html, scenes/mur.html, scenes/cahier.html).

Usage : python3 outils/mondes.py puis python3 outils/assembler.py
"""
import pathlib
import random

ici = pathlib.Path(__file__).resolve().parent.parent
random.seed(6)

ICONES = {
    "play": '<path d="M-14 -18 L18 0 L-14 18 Z" />',
    "livre": '<path d="M-22 -16 H-2 V18 H-22 Z M2 -16 H22 V18 H2 Z" />',
    "micro": '<rect x="-8" y="-20" width="16" height="26" rx="8" /><path d="M-15 0 a15 15 0 0 0 30 0 M0 15 V22" />',
    "graph": '<path d="M-20 16 V-16 M-20 16 H20 M-14 8 L-4 -2 L4 4 L16 -10" />',
}
noms = list(ICONES)

# ---------- La vitrine : des dizaines de fiches produits, serrées, toutes pareilles
fiches = []
for i in range(54):
    ic = ICONES[noms[(i * 3 + i // 9) % 4]]
    w1, w2 = random.choice([70, 78, 84, 64]), random.choice([46, 52, 58, 40])
    fiches.append(
        f'        <div class="fiche"><div class="couv"><svg width="80" height="80" viewBox="-40 -40 80 80"><g fill="none" stroke="#9AA4B2" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{ic}</g></svg></div>'
        f'<i style="width:{w1}%"></i><i style="width:{w2}%"></i><div class="bas"><b></b><span></span></div></div>'
    )

VITRINE = """<template>
  <style>
/*COMMUN*/
    #v-monde { position: absolute; inset: 0; perspective: 1500px; perspective-origin: 50% 45%; overflow: hidden;
      -webkit-mask-image: radial-gradient(ellipse 80% 62% at 50% 50%, #000 40%, transparent 100%);
              mask-image: radial-gradient(ellipse 80% 62% at 50% 50%, #000 40%, transparent 100%); }
    #v-mur { position: absolute; left: -620px; top: 40px; width: 2560px; display: grid; grid-template-columns: repeat(9, 262px); gap: 22px; }
    .fiche { height: 330px; border-radius: 22px; background: #EEF1F5; padding: 14px; }
    .fiche .couv { height: 150px; border-radius: 14px; background: #DCE1E8; display: flex; align-items: center; justify-content: center; }
    .fiche i { display: block; height: 14px; border-radius: 7px; background: #C9D0DA; margin-top: 14px; }
    .fiche .bas { display: flex; justify-content: space-between; align-items: center; margin-top: 22px; }
    .fiche .bas b { width: 80px; height: 18px; border-radius: 9px; background: #AEB7C3; }
    .fiche .bas span { width: 88px; height: 40px; border-radius: 20px; background: #BFC7D2; }
  </style>
  <div id="root" data-composition-id="vitrine" data-width="1080" data-height="1920">
    <div id="v-monde" data-layout-ignore>
      <div id="v-mur">
@@TUILES@@
      </div>
    </div>
  </div>
  <script>
    (function () {
      const DEBUT = 0;
//COMMUN
      // La vitrine d'une plateforme : un mur de fiches qui glisse, ta formation y est une parmi d'autres
      tl.fromTo("#v-mur", { rotationY: -32, rotationX: 4, z: -200, transformOrigin: "50% 50%" }, { rotationY: -32, rotationX: 4, z: -200, duration: 0.01 }, 0);
      tl.fromTo("#v-mur", { x: 0, y: 0 }, { x: -420, y: -160, duration: 37.6, ease: "none" }, 0);
      tl.fromTo("#v-monde", { opacity: 0.13 }, { opacity: 0.13, duration: 0.01 }, 0);
      // « Tu l'as mise sur une plateforme » : la vitrine se montre un peu plus
      tl.fromTo("#v-monde", { opacity: 0.13 }, { immediateRender: false, opacity: 0.2, duration: 1.0, ease: "power1.inOut" }, at(10.8));
      // « Alors je te propose autre chose » : la vitrine s'éteint
      tl.fromTo("#v-monde", { opacity: 0.2 }, { immediateRender: false, opacity: 0, duration: 0.9, ease: "power1.inOut" }, at(36.6));
      window.__timelines["vitrine"] = tl;
    })();
  </script>
</template>
"""


def ecran(k):
    if k == 0:  # accueil
        c = '<div class="e-nav"><b></b><i></i></div><div class="e-hero"><i style="width:80%"></i><i style="width:62%"></i><i class="p" style="width:46%"></i><span class="btn"></span></div><div class="e-cartes"><div></div><div></div></div>'
    elif k == 1:  # fiche produit
        c = '<div class="e-nav"><b></b><i></i></div><div class="e-couv"></div><i style="width:74%"></i><i class="p" style="width:52%"></i><i class="p" style="width:66%"></i><span class="btn"></span>'
    elif k == 2:  # paiement
        c = '<div class="e-nav"><b></b><i></i></div><i style="width:58%"></i><div class="e-champ"></div><div class="e-champ"></div><div class="e-moyens"><div></div><div></div></div><span class="btn"></span>'
    else:  # espace vendeur
        c = '<div class="e-nav"><b></b><i></i></div><div class="e-kpi"><div></div><div></div></div><svg width="236" height="90" viewBox="0 0 236 90"><path d="M0 80 L40 62 L80 66 L120 44 L160 40 L200 20 L236 12" fill="none" stroke="#F5F3EE" stroke-width="3" stroke-linecap="round" /></svg><div class="e-ligne"></div><div class="e-ligne"></div><div class="e-ligne"></div>'
    return f'        <div class="ecran">{c}</div>'


MUR = """<template>
  <style>
/*COMMUN*/
    #m-monde { position: absolute; inset: 0; perspective: 1500px; perspective-origin: 50% 45%; overflow: hidden;
      -webkit-mask-image: radial-gradient(ellipse 80% 62% at 50% 50%, #000 40%, transparent 100%);
              mask-image: radial-gradient(ellipse 80% 62% at 50% 50%, #000 40%, transparent 100%); }
    #m-mur { position: absolute; left: -380px; top: 60px; width: 2000px; display: grid; grid-template-columns: repeat(5, 300px); gap: 64px; }
    .ecran { height: 560px; border-radius: 40px; background: #0E131C; border: 1.5px solid rgba(255,255,255,0.12); padding: 22px; overflow: hidden; }
    .ecran > i, .e-hero i { display: block; height: 14px; border-radius: 7px; background: rgba(245,243,238,0.55); margin-top: 16px; }
    .ecran > i.p, .e-hero i.p { height: 10px; background: rgba(245,243,238,0.22); }
    .e-nav { display: flex; justify-content: space-between; align-items: center; }
    .e-nav b { width: 70px; height: 16px; border-radius: 8px; background: #F5F3EE; }
    .e-nav i { width: 34px; height: 34px; border-radius: 50%; border: 2px solid rgba(245,243,238,0.4); }
    .e-hero { margin-top: 30px; }
    .btn { display: block; width: 150px; height: 44px; border-radius: 22px; background: #F5F3EE; margin-top: 24px; }
    .e-cartes { display: flex; gap: 12px; margin-top: 30px; }
    .e-cartes div { flex: 1; height: 150px; border-radius: 18px; background: rgba(245,243,238,0.08); border: 1.5px solid rgba(245,243,238,0.14); }
    .e-couv { height: 170px; border-radius: 22px; background: rgba(245,243,238,0.08); margin-top: 22px; }
    .e-champ { height: 54px; border-radius: 16px; border: 1.5px solid rgba(245,243,238,0.22); margin-top: 18px; }
    .e-moyens { display: flex; gap: 12px; margin-top: 18px; }
    .e-moyens div { flex: 1; height: 70px; border-radius: 16px; background: rgba(245,243,238,0.1); }
    .e-kpi { display: flex; gap: 12px; margin-top: 22px; }
    .e-kpi div { flex: 1; height: 90px; border-radius: 18px; background: rgba(245,243,238,0.08); }
    .ecran svg { display: block; margin-top: 22px; }
    .e-ligne { height: 46px; border-bottom: 1.5px solid rgba(245,243,238,0.12); }
  </style>
  <div id="root" data-composition-id="mur" data-width="1080" data-height="1920">
    <div id="m-monde" data-layout-ignore>
      <div id="m-mur">
@@TUILES@@
      </div>
    </div>
  </div>
  <script>
    (function () {
      const DEBUT = 36.3;
//COMMUN
      // Le mur de ta boutique : tes écrans à toi, aérés, qui glissent lentement dans l'autre sens
      tl.fromTo("#m-mur", { rotationY: 30, rotationX: 4, z: -260, transformOrigin: "50% 50%" }, { rotationY: 30, rotationX: 4, z: -260, duration: 0.01 }, 0);
      tl.fromTo("#m-mur", { x: 0, y: 0 }, { x: -520, y: -120, duration: 63.2, ease: "none" }, 0);
      tl.fromTo("#m-monde", { opacity: 0 }, { opacity: 0.55, duration: 1.1, ease: "power1.inOut" }, at(36.4));
      // La carte de l'Afrique a besoin de calme : le mur s'efface pendant qu'elle s'allume
      tl.fromTo("#m-monde", { opacity: 0.55 }, { immediateRender: false, opacity: 0.16, duration: 0.6, ease: "power1.inOut" }, at(43.1));
      tl.fromTo("#m-monde", { opacity: 0.16 }, { immediateRender: false, opacity: 0.55, duration: 0.8, ease: "power1.inOut" }, at(50.0));
      window.__timelines["mur"] = tl;
    })();
  </script>
</template>
"""

CAHIER = """<template>
  <style>
/*COMMUN*/
    #c-feuille { position: absolute; inset: 0; background: #04060B; }
    #c-feuille svg { position: absolute; left: 0; top: 0; }
  </style>
  <div id="root" data-composition-id="cahier" data-width="1080" data-height="1920">
    <div id="c-feuille" data-layout-ignore>
      <svg width="1080" height="1920" viewBox="0 0 1080 1920">
        <g id="c-lignes" stroke="rgba(245,243,238,0.07)" stroke-width="1.5">@@LIGNES@@</g>
        <path id="c-marge" d="M56 0 V1920" stroke="rgba(245,243,238,0.14)" stroke-width="1.5" />
      </svg>
    </div>
  </div>
  <script>
    (function () {
      const DEBUT = 64.3;
//COMMUN
      // La feuille de calcul : un cahier de comptes, sobre, qui couvre le mur le temps du calcul
      tl.fromTo("#c-feuille", { opacity: 0 }, { opacity: 1, duration: 0.6, ease: "power1.inOut" }, 0);
      tl.fromTo("#c-lignes", { y: 0 }, { y: -60, duration: 14.6, ease: "none" }, 0);
      tl.fromTo("#c-feuille", { opacity: 1 }, { immediateRender: false, opacity: 0, duration: 0.5, ease: "power1.inOut" }, at(78.35));
      window.__timelines["cahier"] = tl;
    })();
  </script>
</template>
"""

(ici / "scenes/vitrine.html").write_text(VITRINE.replace("@@TUILES@@", "\n".join(fiches)))
(ici / "scenes/mur.html").write_text(MUR.replace("@@TUILES@@", "\n".join(ecran((i * 3 + i // 5) % 4) for i in range(25))))
(ici / "scenes/cahier.html").write_text(CAHIER.replace("@@LIGNES@@", "".join(f'<path d="M0 {y} H1080" />' for y in range(80, 2000, 96))))
print("mondes écrits")
