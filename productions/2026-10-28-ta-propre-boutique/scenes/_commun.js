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
