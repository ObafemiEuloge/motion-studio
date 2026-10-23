---
name: motion
description: Construit et rend la vidéo HyperFrames d'Oba à partir du storyboard, dans la charte verre et Apple du studio. À utiliser après le storyboard et la voix.
---

# Motion

Lis d'abord le skill `/hyperframes` (contrat de rendu) puis `brand/DESIGN.md`. Le dossier de production est une copie de `templates/base/`.

## Base

- `templates/base/index.html` contient déjà : variables de couleur, polices, le plan d'interfaces 3D (`#world`), le style des cartes de verre, des caches et des pastilles. Garde ces classes, ne réinvente pas le style.
- Une scène par sous-composition dans `compositions/` quand le film dépasse 10 s (le root ne garde que les hôtes de scènes, l'audio et le monde de fond).
- GSAP local (`assets/js/gsap.min.js`). Jamais de CDN : le rendu se fait sans réseau.
- Polices : `@font-face` vers `assets/fonts/`.

## Mouvement (valeurs du studio)

| Action | Valeur |
|---|---|
| Texte qui arrive | depuis un cache : `yPercent 110 → 0`, 0,7 à 0,85 s, `expo.out`, lignes à 80 ms d'écart |
| Texte qui part | `yPercent 0 → -110`, 0,36 à 0,4 s, `power3.in` |
| Carte de verre qui arrive | `y +1250 → 0`, 1,1 s, `expo.out` |
| Pastilles | `y 26 → 0` + opacité, 0,6 s, `expo.out`, 70 ms d'écart |
| Trait | `scaleX 0 → 1` depuis la gauche, 0,7 à 0,8 s, `expo.out` |
| Plan d'interfaces | défilement linéaire continu, `rotationX 56`, `rotationZ -20` |
| Reflet sur le verre | une fois par film, 1,3 s, `power2.inOut` |
| Chiffre qui compte | 0,9 à 1,4 s, `power3.out`, valeur finale arrondie et tenue |

Interdits techniques : animer `letter-spacing`, `width`, `top`, `left` ; un `transform` CSS sur un élément que GSAP anime ; `filter: blur` sur les titres ; tout halo ou dégradé de fond (voir `DESIGN.md`).

## Interfaces réelles

Pour montrer une application, utilise une capture réelle (`npx hyperframes capture <url> --json` pour un site public comme mescentimes.cloud) ou reconstruis l'écran en HTML avec de vraies données plausibles en FCFA. Jamais de faux logo de client.

## Vérifier puis rendre

```bash
npx hyperframes check --json          # zéro erreur
npx hyperframes snapshot --at <instants clés>   # regarde chaque image
npx hyperframes render --output renders/<slug>.mp4
```
Après le rendu : extrais 6 images au téléphone (`ffmpeg -ss T -i … -vf scale=540:-2`) et regarde-les avant de livrer.
