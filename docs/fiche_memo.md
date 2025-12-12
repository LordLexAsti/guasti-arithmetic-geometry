# Théorie de Guasti — Fiche Mémo
## L'essentiel en une page

---

## 🏠 LA GRILLE DE GUASTI

**Principe :** Un tableau où chaque nombre "habite" dans sa propre colonne.
```
         C1   C2   C3   C4   C5   C6
    L1 [  1 ][  2 ][  3 ][  4 ][  5 ][  6 ]   <- Tous presents
    L2 [    ][  2 ][    ][  4 ][    ][  6 ]   <- Nombres pairs
    L3 [    ][    ][  3 ][    ][    ][  6 ]   <- Multiples de 3
    L4 [    ][    ][    ][  4 ][    ][    ]
    L5 [    ][    ][    ][    ][  5 ][    ]
    L6 [    ][    ][    ][    ][    ][  6 ]
```

**Règle d'or :** Le nombre k est en colonne k, aux lignes qui le divisent.

---

## 🔑 LES 3 LECTURES CLÉS

| Ce qu'on regarde | Ce qu'on apprend |
|------------------|------------------|
| Hauteur de colonne | Nombre de diviseurs |
| Colonne à 2 cases | C'est un **PREMIER** |
| Signature contient 45° | C'est un **CARRÉ PARFAIT** |

---

## 📐 LA SIGNATURE ANGULAIRE

Pour chaque façon d'écrire `n = a × b`, on calcule `angle = arctan(b/a)`

**Exemple : 12 = 1×12 = 2×6 = 3×4**
```
12 = 1 × 12  →  angle = 85.2°
12 = 2 × 6   →  angle = 71.6°
12 = 3 × 4   →  angle = 53.1°

Signature de 12 = {53.1°, 71.6°, 85.2°}
```

**Le 45° magique :** Quand a = b (carré parfait), l'angle est exactement 45°.

---

## 🔄 LA TRANSFORMÉE DE GUASTI
```
     NOMBRE  ───────►  TRANSFORMÉE  ───────►  SIGNATURE
       12                  T_G               {53°, 72°, 85°}
```

**Propriétés clés :**
- Un seul angle → Nombre Premier
- Contient 45° → Carré Parfait
- Beaucoup d'angles → Nombre très composé

---

## 📜 LE PALIMPSESTE ARITHMÉTIQUE

Mélanger Guasti (G) et Pythagore (P) révèle des structures cachées :

| Mélange | Diagonale | Structure révélée |
|---------|-----------|-------------------|
| G + P | n(n+1) | Nombres oblongs |
| G × P | n³ | Cubes parfaits |
| PGCD(G,P) | = G | Guasti est le noyau |

**Hiérarchie des puissances :**
```
Guasti     →  n¹  (entiers)
Pythagore  →  n²  (carrés)
G × P      →  n³  (cubes)
```

---

## 🎯 EN UN MOT

> **La Grille de Guasti donne des "lunettes géométriques" pour voir les nombres autrement.**

---

*Alexandre Guasti — Décembre 2025*
