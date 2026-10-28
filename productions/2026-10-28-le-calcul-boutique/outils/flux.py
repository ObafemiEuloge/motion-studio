"""Génère scenes/flux.html : des notifications de paiement réparties en profondeur, qui avancent vers la caméra."""
import pathlib, random
ici = pathlib.Path(__file__).resolve().parent.parent
random.seed(7)
pills = []
for i in range(46):
    x, y = random.uniform(-260, 1100), random.uniform(-300, 2050)
    z = random.uniform(-2700, -1300)
    o = round(0.35 + 0.65 * (z + 2700) / 1400, 2)
    w1, w2 = random.choice([150, 180, 120, 200]), random.choice([90, 70, 110])
    pills.append((x, y, z, o, w1, w2))
html = []
for i, (x, y, z, o, w1, w2) in enumerate(pills):
    html.append(f'        <div class="pi" id="pi{i}" style="left:{x:.0f}px;top:{y:.0f}px;opacity:{o}"><span class="ic"></span><span class="tx"><i style="width:{w1}px"></i><i style="width:{w2}px"></i></span></div>')
js = ",".join(f"[{z:.0f}]" for (_, _, z, _, _, _) in pills)
s = """<template>
  <style>
/*COMMUN*/
    #x-monde { position: absolute; inset: 0; perspective: 1100px; perspective-origin: 50% 46%; overflow: hidden; }
    #x-espace { position: absolute; inset: 0; transform-style: preserve-3d; }
    .pi { position: absolute; width: 380px; height: 112px; border-radius: 56px; background: #0E141F; border: 1.5px solid rgba(255,255,255,0.14);
      display: flex; align-items: center; gap: 22px; padding: 0 26px; }
    .pi .ic { width: 64px; height: 64px; border-radius: 50%; border: 3px solid rgba(245,243,238,0.7); }
    .pi i { display: block; height: 14px; border-radius: 7px; background: rgba(245,243,238,0.6); }
    .pi i + i { margin-top: 14px; background: rgba(245,243,238,0.25); }
  </style>
  <div id="root" data-composition-id="flux" data-width="1080" data-height="1920">
    <div id="x-monde" data-layout-ignore>
      <div id="x-espace">
@@PILLS@@
      </div>
    </div>
  </div>
  <script>
    (function () {
      const DEBUT = 0;
      const Z = [@@Z@@];
//COMMUN
      // Les paiements avancent vers la caméra, chacun à sa profondeur : la parallaxe est réelle
      Z.forEach(([z], i) => tl.fromTo("#pi" + i, { z: z, rotationY: -8 }, { z: z + 1450, rotationY: -8, duration: 28.5, ease: "none" }, 0));
      tl.fromTo("#x-espace", { rotationZ: -6 }, { rotationZ: 4, duration: 28.5, ease: "none" }, 0);
      tl.fromTo("#x-monde", { opacity: 0.6 }, { opacity: 0.6, duration: 0.01 }, 0);
      // Sous la carte et sous le calcul, le flux se fait discret ; il revient derrière la signature
      tl.fromTo("#x-monde", { opacity: 0.6 }, { immediateRender: false, opacity: 0.22, duration: 0.6, ease: "power1.inOut" }, at(6.2));
      tl.fromTo("#x-monde", { opacity: 0.22 }, { immediateRender: false, opacity: 0.12, duration: 0.8, ease: "power1.inOut" }, at(9.4));
      tl.fromTo("#x-monde", { opacity: 0.12 }, { immediateRender: false, opacity: 0.6, duration: 0.8, ease: "power1.inOut" }, at(19.9));
      window.__timelines["flux"] = tl;
    })();
  </script>
</template>
"""
(ici / "scenes/flux.html").write_text(s.replace("@@PILLS@@", "\n".join(html)).replace("@@Z@@", js))
print("flux écrit")
