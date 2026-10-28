"""Carte de l'Afrique en points (trame régulière), pour la scène « boutique ».

Écrit outils/carte.json : la liste des points de la trame et les 17 points allumés.
Contour simplifié à la main (longitude, latitude), assez précis pour une trame de 20 px.
Usage : python3 outils/carte.py
"""
import json
import pathlib

ici = pathlib.Path(__file__).resolve().parent

AFRIQUE = [
    (-5.9, 35.8), (-1.0, 35.1), (3.0, 36.8), (10.2, 37.2), (11.1, 33.2), (15.2, 32.3), (19.9, 31.0), (25.0, 31.6),
    (29.9, 31.2), (32.3, 31.3), (32.6, 29.9), (34.0, 26.6), (35.5, 23.9), (37.2, 19.6), (39.4, 15.6), (43.3, 12.6),
    (44.8, 10.4), (51.2, 11.8), (51.0, 10.4), (48.5, 5.0), (45.3, 2.0), (42.5, -0.6), (40.2, -2.5), (39.7, -4.1),
    (39.3, -6.8), (40.5, -10.5), (40.6, -15.0), (36.9, -17.9), (35.5, -22.0), (35.5, -24.0), (32.6, -26.0),
    (32.9, -28.5), (31.0, -29.9), (27.9, -33.0), (25.6, -33.9), (20.0, -34.8), (18.4, -34.2), (18.0, -32.0),
    (16.5, -28.6), (14.5, -22.9), (11.8, -17.3), (13.5, -12.3), (13.2, -8.8), (12.3, -6.0), (11.8, -4.8),
    (8.8, -0.7), (9.5, 1.0), (9.7, 4.0), (8.5, 4.5), (6.0, 4.3), (3.4, 6.4), (1.2, 6.1), (-2.1, 4.7), (-4.0, 5.3),
    (-7.5, 4.4), (-10.8, 6.3), (-13.2, 8.5), (-15.0, 10.8), (-16.7, 12.4), (-17.5, 14.7), (-16.5, 16.0),
    (-16.0, 18.1), (-16.9, 21.3), (-15.0, 24.0), (-14.0, 26.0), (-12.0, 27.5), (-9.8, 29.5), (-9.6, 30.4),
    (-9.8, 31.5), (-8.5, 33.3), (-6.8, 34.0),
]
MADAGASCAR = [(49.3, -12.0), (50.4, -15.5), (49.4, -17.9), (48.0, -22.0), (47.1, -24.8), (45.2, -25.6),
              (43.7, -23.5), (44.3, -20.0), (44.0, -17.0), (46.3, -15.7), (48.3, -13.4)]
# 17 points allumés : des pays d'Afrique de l'Ouest, du Centre et de l'Est (jamais nommés à l'écran)
ALLUMES = [(-16.5, 14.6), (-8.0, 12.6), (-12.0, 10.4), (-5.0, 6.8), (-1.5, 12.4), (1.2, 8.0), (2.4, 9.4),
           (2.6, 13.6), (7.5, 9.1), (12.0, 5.5), (11.5, -0.6), (15.2, -1.2), (23.0, -3.0), (32.4, 1.4),
           (37.5, 0.4), (35.0, -6.0), (27.5, -14.0)]

K, X0, Y0, PAS = 10.8, 162.0, 470.0, 20


def proj(lon, lat):
    return X0 + (lon + 18) * K, Y0 + (37 - lat) * K


def dedans(x, y, poly):
    c = False
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[i - 1]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


polys = [[proj(*p) for p in AFRIQUE], [proj(*p) for p in MADAGASCAR]]
points = []
for gy in range(int(Y0), int(Y0 + 800), PAS):
    for gx in range(int(X0) - 20, int(X0 + 780), PAS):
        if any(dedans(gx, gy, p) for p in polys):
            points.append((gx, gy))
allumes = []
for lon, lat in ALLUMES:
    x, y = proj(lon, lat)
    i = min(range(len(points)), key=lambda k: (points[k][0] - x) ** 2 + (points[k][1] - y) ** 2)
    if i not in allumes:
        allumes.append(i)
(ici / "carte.json").write_text(json.dumps({"points": points, "allumes": allumes}))
print(len(points), "points,", len(allumes), "allumés")
