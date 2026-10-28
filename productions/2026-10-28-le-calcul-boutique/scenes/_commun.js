      // Outils communs : temps du film -> temps de la scène, chiffres qui roulent
      const at = (g) => +(g - DEBUT).toFixed(3);
      const rouleaux = {};
      document.querySelectorAll("#root .roule").forEach((el) => {
        const txt = el.textContent; el.textContent = ""; const rails = [];
        for (const ch of txt) {
          if (/[0-9]/.test(ch)) {
            const col = document.createElement("span"); col.className = "col";
            const rail = document.createElement("span");
            for (let d = 0; d < 10; d++) { const s = document.createElement("span"); s.textContent = d; rail.appendChild(s); }
            col.appendChild(rail); el.appendChild(col); rails.push({ rail, d: +ch });
          } else { const s = document.createElement("span"); s.className = ch === " " ? "sep" : ""; s.textContent = ch === " " ? " " : ch; el.appendChild(s); }
        }
        rouleaux[el.id] = rails;
      });
      const tl = gsap.timeline({ paused: true });
      const pose = (id, chiffres) => rouleaux[id].forEach((r, i) => tl.fromTo(r.rail, { yPercent: -chiffres[i] * 10 }, { yPercent: -chiffres[i] * 10, duration: 0.01 }, 0));
      const roule = (id, de, vers, t, dur, dec) => rouleaux[id].forEach((r, i) => {
        if (de[i] === vers[i]) return;
        tl.fromTo(r.rail, { yPercent: -de[i] * 10 }, { immediateRender: false, yPercent: -vers[i] * 10, duration: dur || 1.0, ease: "expo.out" }, t + i * (dec === undefined ? 0.05 : dec));
      });
      const chiffres = (id) => rouleaux[id].map((r) => r.d);
      const zeros = (id) => rouleaux[id].map(() => 0);
      // Entrée et sortie de texte par cache
      const entre = (sel, t, dec) => tl.fromTo(sel, { yPercent: 130 }, { immediateRender: false, yPercent: 0, duration: 0.8, ease: "expo.out", stagger: dec === undefined ? 0.08 : dec }, t);
      const sort = (sel, t) => tl.fromTo(sel, { yPercent: 0 }, { immediateRender: false, yPercent: -135, duration: 0.38, ease: "power3.in", stagger: 0.04 }, t);
      const cache = (sel) => tl.fromTo(sel, { yPercent: 130 }, { yPercent: 130, duration: 0.01 }, 0);
      // Compteurs à tambours 3D : chaque chiffre est un cylindre de dix faces (rayon 1,54 em)
      const tambours = {};
      document.querySelectorAll("#root .tambours").forEach((el) => {
        // les dix faces d'un cylindre se superposent par construction : le contrôle de mise en page ne doit pas les compter
        el.setAttribute("data-layout-ignore", "");
        const txt = el.textContent; el.textContent = ""; const cyls = [];
        for (const ch of txt) {
          if (/[0-9]/.test(ch)) {
            const t = document.createElement("span"); t.className = "tb";
            const c = document.createElement("span"); c.className = "cyl";
            for (let d = 0; d < 10; d++) { const f = document.createElement("span"); f.className = "fa"; f.textContent = d;
              f.style.transform = `rotateX(${-36 * d}deg) translateZ(1.54em)`; c.appendChild(f); }
            t.appendChild(c); el.appendChild(t); cyls.push({ cyl: c, d: +ch });
          } else { const s = document.createElement("span"); s.className = ch === " " ? "sep" : "sym"; s.textContent = ch === " " ? "\u00A0" : ch; el.appendChild(s); }
        }
        tambours[el.id] = cyls;
      });
      const posTambour = (id, ch) => tambours[id].forEach((c, i) => tl.fromTo(c.cyl, { rotationX: 36 * ch[i] }, { rotationX: 36 * ch[i], duration: 0.01 }, 0));
      const tourne = (id, de, vers, t, dur, dec, tours) => tambours[id].forEach((c, i) => {
        tl.fromTo(c.cyl, { rotationX: 36 * de[i] }, { immediateRender: false, rotationX: 36 * vers[i] + 360 * (tours === undefined ? 1 : tours), duration: dur || 1.4, ease: "power3.out" }, t + i * (dec === undefined ? 0.06 : dec));
      });
      const chiffresT = (id) => tambours[id].map((c) => c.d);
