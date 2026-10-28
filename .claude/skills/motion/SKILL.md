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

## Pièges techniques déjà rencontrés (à ne pas refaire)

- **Verre qui ne floute plus** : un `clip-path`, un `filter`, un `mask` ou une `opacity` < 1 sur un parent du verre l'empêche de flouter ce qui est derrière. Après une ouverture par `clip-path`, remets `clipPath: "none"`.
- **Tracés de cercle** : `pathLength="1"` est peu fiable sur un cercle fait d'arcs (le trait n'apparaît qu'à la fin). Utilise la longueur réelle (2 × π × r) en `stroke-dasharray` et `stroke-dashoffset`.
- **Ligne qui relie des icônes** : elle passe derrière les icônes (placée avant dans le DOM), centrée sur elles, à vitesse constante (`ease: "none"`), et chaque icône s'allume quand la ligne l'atteint (temps calculé, pas estimé).
- **Grandir une carte** : jamais `width`, `height`, `left`, `top` ; une découpe `clip-path: inset(...)` puis `none`.
- **Caméra dans un dessin** : animer la `viewBox` du SVG et une variable CSS d'épaisseur de trait (`--sw`) pour garder un trait constant.
- **Chiffres qui roulent** : une colonne 0 à 9 par chiffre (`yPercent: -chiffre × 10`), colonnes de 0,64 em ; masquer le montant tant qu'il n'a pas commencé à rouler (sinon « 00 000 »).
- **Lettres qui débordent des caches** : état caché à 130 %, sortie à −135 %.
- **Séquences d'Oba** : toujours sans le son d'origine (`-an`), étalonnées, recadrées dans une carte arrondie.
- **3D CSS** : chaque parent entre la scène (qui porte `perspective`) et l'objet doit avoir `transform-style: preserve-3d`, sinon tout s'aplatit (piliers restés à plat). Un `mask`, un `filter` ou une `opacity` < 1 sur un parent aplatit aussi.
- **Compteurs à tambours** : la face avant doit être à la profondeur zéro (cylindre reculé de son rayon), sinon la perspective grossit et rogne les chiffres ; le masque qui cache les faces voisines a besoin d'une marge latérale. Exemple : `productions/2026-10-28-le-calcul-boutique/scenes/_commun.js`.
- **Éléments cachés dans la frise d'un autre chapitre** : un décor de chapitre suivant (frise, ligne) doit être invisible avant son chapitre, sinon il traverse les cartes (ligne verticale vue par Oba sur 1Peu 1Peu).

## Vérifier puis rendre

```bash
npx hyperframes check --json          # zéro erreur
npx hyperframes snapshot --at <instants clés>   # regarde chaque image
npx hyperframes render --output renders/<slug>.mp4
```
Après le rendu : extrais 6 images au téléphone (`ffmpeg -ss T -i … -vf scale=540:-2`) et regarde-les avant de livrer.
