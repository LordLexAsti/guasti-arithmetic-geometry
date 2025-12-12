#!/usr/bin/env python3
"""
Signature Angulaire - Théorie de Guasti
=======================================

Calcul de la signature angulaire d'un nombre entier.
La signature est l'ensemble des angles formés par les paires de diviseurs.

Auteur : Alexandre Guasti
Version : 1.0
"""

import math
from typing import List, Tuple


def diviseurs(n: int) -> List[int]:
    """
    Retourne la liste des diviseurs de n.
    
    Exemple:
        >>> diviseurs(12)
        [1, 2, 3, 4, 6, 12]
    """
    if n < 1:
        return []
    
    divs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    
    return sorted(divs)


def paires_diviseurs(n: int) -> List[Tuple[int, int]]:
    """
    Retourne les paires (a, b) telles que a * b = n et a <= b.
    
    Exemple:
        >>> paires_diviseurs(12)
        [(1, 12), (2, 6), (3, 4)]
    """
    paires = []
    for a in range(1, int(math.sqrt(n)) + 1):
        if n % a == 0:
            b = n // a
            paires.append((a, b))
    
    return paires


def signature_angulaire(n: int, en_degres: bool = True) -> List[float]:
    """
    Calcule la signature angulaire d'un nombre.
    
    Pour chaque paire (a, b) avec a * b = n, l'angle est arctan(b/a).
    
    Args:
        n: Le nombre entier
        en_degres: Si True, retourne les angles en degres (defaut)
        
    Returns:
        Liste des angles tries
        
    Exemple:
        >>> signature_angulaire(12)
        [53.13, 71.57, 85.24]  # environ
    """
    if n < 1:
        return []
    
    angles = []
    for a, b in paires_diviseurs(n):
        angle = math.atan2(b, a)
        if en_degres:
            angle = math.degrees(angle)
        angles.append(round(angle, 2))
    
    return sorted(angles)


def contient_45_degres(n: int, tolerance: float = 0.01) -> bool:
    """
    Verifie si la signature contient 45 degres (= carre parfait).
    
    Theoreme : n est un carre parfait <=> 45 degres dans signature(n)
    
    Exemple:
        >>> contient_45_degres(16)
        True
        >>> contient_45_degres(12)
        False
    """
    signature = signature_angulaire(n)
    return any(abs(angle - 45.0) < tolerance for angle in signature)


def est_premier_par_signature(n: int) -> bool:
    """
    Verifie si n est premier via sa signature.
    
    Un nombre premier n'a qu'une seule paire de diviseurs (1, n),
    donc sa signature ne contient qu'un seul angle.
    
    Exemple:
        >>> est_premier_par_signature(7)
        True
        >>> est_premier_par_signature(12)
        False
    """
    if n < 2:
        return False
    return len(signature_angulaire(n)) == 1


def angle_jumeaux(p: int) -> float:
    """
    Calcule l'angle forme par une paire de premiers jumeaux (p, p+2).
    
    Cet angle converge vers 45 degres quand p augmente.
    Vitesse : theta - 45 ~ 57.3 / p
    
    Exemple:
        >>> angle_jumeaux(3)   # jumeaux (3, 5)
        59.04
        >>> angle_jumeaux(71)  # jumeaux (71, 73)
        45.80
    """
    return round(math.degrees(math.atan2(p + 2, p)), 2)


def afficher_signature(n: int) -> None:
    """
    Affiche la signature d'un nombre de facon lisible.
    """
    paires = paires_diviseurs(n)
    signature = signature_angulaire(n)
    
    print(f"\n{'='*50}")
    print(f"SIGNATURE ANGULAIRE DE {n}")
    print(f"{'='*50}")
    print(f"Diviseurs : {diviseurs(n)}")
    print(f"Nombre de diviseurs (tau) : {len(diviseurs(n))}")
    print()
    
    print("Paires de diviseurs et angles :")
    for (a, b), angle in zip(paires, signature):
        marque = " <- 45 deg (carre parfait)" if abs(angle - 45.0) < 0.01 else ""
        print(f"  {n} = {a} x {b}  ->  theta = {angle} deg{marque}")
    
    print()
    print(f"Signature : {{{', '.join(f'{a} deg' for a in signature)}}}")
    
    # Diagnostics
    if contient_45_degres(n):
        k = int(math.sqrt(n))
        print(f"\n[OK] Contient 45 deg -> {n} est un carre parfait ({k}^2)")
    
    if est_premier_par_signature(n):
        print(f"\n[OK] Un seul angle -> {n} est un nombre premier")


# =============================================================================
# EXEMPLE D'UTILISATION
# =============================================================================

if __name__ == "__main__":
    print("DEMONSTRATION DE LA SIGNATURE ANGULAIRE")
    print("=" * 50)
    
    # Exemples varies
    exemples = [6, 7, 12, 16, 28, 36]
    
    for n in exemples:
        afficher_signature(n)
    
    # Convergence des jumeaux
    print("\n" + "=" * 50)
    print("CONVERGENCE DES PREMIERS JUMEAUX VERS 45 DEG")
    print("=" * 50)
    
    jumeaux = [3, 5, 11, 17, 29, 41, 59, 71, 101, 107]
    print(f"\n{'Premier p':<12} {'Angle':<12} {'Ecart a 45':<12}")
    print("-" * 36)
    
    for p in jumeaux:
        angle = angle_jumeaux(p)
        ecart = angle - 45.0
        print(f"{p:<12} {angle:<12} {ecart:+.2f} deg")
