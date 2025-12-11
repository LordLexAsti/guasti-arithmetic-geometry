# 📖 Nomenclature Guasti : Définition Structurelle

> **"La Grille n'est pas une table de multiplication, c'est une carte de divisibilité."**

### 1. La Grille de Guasti (Définition Officielle)
Un espace 2D organisé par divisibilité :
* **Axe Horizontal (Colonnes $j$) :** La suite des entiers naturels ($0, 1, 2, 3 \dots$).
* **Axe Vertical (Lignes $i$) :** Les tables de diviseurs (Table de 1, Table de 2 $\dots$).
* **La Règle :** La case $(i, j)$ est active **si et seulement si** $i$ divise $j$.

### 2. La Diagonale d'Identité
Contrairement à une table de Pythagore où la diagonale porte les carrés ($n^2$), la diagonale de la Grille de Guasti porte les entiers eux-mêmes ($n$).
* C'est la frontière du crible : aucun diviseur ne peut être plus grand que le nombre lui-même.
* Au-delà de cette ligne (angle > 45° dans ce repère), c'est le "vide arithmétique".

### 3. Le Scanner Vertical (La Colonne)
Regarder une colonne $n$ de haut en bas, c'est lire instantanément la structure intime du nombre :
* Les points allumés sont la liste exacte des diviseurs de $n$.
* **Critère de Primalité Visuel :** Une colonne qui ne contient que deux points correspond à un **Nombre Premier**.

### 4. La Signature Angulaire (Rectifiée)
Dans ce repère :
* L'angle $\theta$ d'un point est donné par $\arctan(\text{Diviseur} / \text{Nombre})$.
* Toutes les signatures sont comprises entre 0° et 45° (la diagonale).
