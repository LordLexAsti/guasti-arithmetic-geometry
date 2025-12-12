#!/usr/bin/env python3
"""
Palimpseste Arithmetique - Theorie de Guasti
============================================

Melange de la Grille de Guasti et du Tableau Pythagoricien.
Revele des structures emergentes : cubes, oblongs, triangulaires.

Auteur : Alexandre Guasti
Version : 1.0
"""

import numpy as np
from math import gcd
from typing import Dict


def construire_grille_guasti(taille: int) -> np.ndarray:
    """
    Construit la Grille de Guasti.
    
    Regle : G[i, j] = j si i divise j, sinon 0
    """
    grille = np.zeros((taille + 1, taille + 1), dtype=int)
    for j in range(1, taille + 1):
        for i in range(1, taille + 1):
            if j % i == 0:
                grille[i, j] = j
    return grille


def construire_tableau_pythagore(taille: int) -> np.ndarray:
    """
    Construit le Tableau Pythagoricien (table de multiplication).
    
    Regle : P[i, j] = i * j
    """
    tableau = np.zeros((taille + 1, taille + 1), dtype=int)
    for i in range(1, taille + 1):
        for j in range(1, taille + 1):
            tableau[i, j] = i * j
    return tableau


# =============================================================================
# TYPES DE PALIMPSESTES
# =============================================================================

def palimpseste_additif(taille: int) -> np.ndarray:
    """
    Palimpseste G + P
    
    Diagonale : n + n^2 = n(n+1) -> Nombres OBLONGS
    """
    G = construire_grille_guasti(taille)
    P = construire_tableau_pythagore(taille)
    return G + P


def palimpseste_multiplicatif(taille: int) -> np.ndarray:
    """
    Palimpseste G * P
    
    Diagonale : n * n^2 = n^3 -> CUBES parfaits
    Ligne 1 : j * j = j^2 -> CARRES parfaits
    """
    G = construire_grille_guasti(taille)
    P = construire_tableau_pythagore(taille)
    return G * P


def palimpseste_pgcd(taille: int) -> np.ndarray:
    """
    Palimpseste PGCD(G, P)
    
    Resultat : IDENTIQUE a la Grille de Guasti !
    gcd(j, i*j) = j
    
    Guasti est le "noyau irreductible" de Pythagore.
    """
    G = construire_grille_guasti(taille)
    P = construire_tableau_pythagore(taille)
    
    resultat = np.zeros_like(G)
    for i in range(1, taille + 1):
        for j in range(1, taille + 1):
            if G[i, j] > 0 and P[i, j] > 0:
                resultat[i, j] = gcd(int(G[i, j]), int(P[i, j]))
    
    return resultat


def palimpseste_difference(taille: int) -> np.ndarray:
    """
    Palimpseste |G - P|
    
    Ligne 1 : tout a 0 (coincidence parfaite)
    Diagonale : |n - n^2| = n^2 - n = n(n-1)
    """
    G = construire_grille_guasti(taille)
    P = construire_tableau_pythagore(taille)
    return np.abs(G.astype(int) - P.astype(int))


def palimpseste_ratio(taille: int) -> np.ndarray:
    """
    Palimpseste P // G (division entiere)
    
    Resultat : P[i,j] / G[i,j] = i (numero de ligne)
    """
    G = construire_grille_guasti(taille)
    P = construire_tableau_pythagore(taille)
    
    resultat = np.zeros_like(G)
    for i in range(1, taille + 1):
        for j in range(1, taille + 1):
            if G[i, j] > 0:
                resultat[i, j] = P[i, j] // G[i, j]
    
    return resultat


# =============================================================================
# ANALYSE
# =============================================================================

def extraire_diagonale(grille: np.ndarray, taille: int) -> list:
    """Extrait la diagonale d'une grille."""
    return [grille[i, i] for i in range(1, taille + 1)]


def analyser_palimpsestes(taille: int = 20) -> Dict:
    """
    Analyse les differents palimpsestes et leurs structures emergentes.
    """
    resultats = {}
    
    # Palimpseste additif
    P_add = palimpseste_additif(taille)
    diag_add = extraire_diagonale(P_add, taille)
    oblongs = [n * (n + 1) for n in range(1, taille + 1)]
    resultats['additif'] = {
        'diagonale': diag_add,
        'formule': 'n + n^2 = n(n+1)',
        'nom': 'Nombres oblongs',
        'verification': diag_add == oblongs
    }
    
    # Palimpseste multiplicatif
    P_mult = palimpseste_multiplicatif(taille)
    diag_mult = extraire_diagonale(P_mult, taille)
    cubes = [n ** 3 for n in range(1, taille + 1)]
    ligne1_mult = [P_mult[1, j] for j in range(1, taille + 1)]
    carres = [j ** 2 for j in range(1, taille + 1)]
    resultats['multiplicatif'] = {
        'diagonale': diag_mult,
        'formule_diag': 'n * n^2 = n^3',
        'nom_diag': 'Cubes parfaits',
        'verification_diag': diag_mult == cubes,
        'ligne1': ligne1_mult,
        'formule_L1': 'j * j = j^2',
        'nom_L1': 'Carres parfaits',
        'verification_L1': ligne1_mult == carres
    }
    
    # Palimpseste PGCD
    G = construire_grille_guasti(taille)
    P_pgcd = palimpseste_pgcd(taille)
    resultats['pgcd'] = {
        'egal_guasti': np.array_equal(P_pgcd, G),
        'interpretation': 'Guasti est le noyau irreductible de Pythagore'
    }
    
    # Palimpseste difference
    P_diff = palimpseste_difference(taille)
    ligne1_diff = [P_diff[1, j] for j in range(1, taille + 1)]
    resultats['difference'] = {
        'ligne1': ligne1_diff,
        'ligne1_nulle': all(v == 0 for v in ligne1_diff),
        'interpretation': 'La ligne 1 est le pont entre G et P'
    }
    
    return resultats


def afficher_analyse() -> None:
    """Affiche l'analyse des palimpsestes."""
    print("=" * 60)
    print("ANALYSE DES PALIMPSESTES ARITHMETIQUES")
    print("=" * 60)
    
    resultats = analyser_palimpsestes(15)
    
    print("\n1. PALIMPSESTE ADDITIF (G + P)")
    print("-" * 40)
    r = resultats['additif']
    print(f"   Diagonale : {r['diagonale'][:10]}...")
    print(f"   Formule : {r['formule']}")
    print(f"   Structure : {r['nom']}")
    print(f"   Verifie : {r['verification']}")
    
    print("\n2. PALIMPSESTE MULTIPLICATIF (G * P)")
    print("-" * 40)
    r = resultats['multiplicatif']
    print(f"   Diagonale : {r['diagonale'][:10]}...")
    print(f"   Formule : {r['formule_diag']}")
    print(f"   Structure : {r['nom_diag']}")
    print(f"   Verifie : {r['verification_diag']}")
    print()
    print(f"   Ligne 1 : {r['ligne1'][:10]}...")
    print(f"   Formule : {r['formule_L1']}")
    print(f"   Structure : {r['nom_L1']}")
    print(f"   Verifie : {r['verification_L1']}")
    
    print("\n3. PALIMPSESTE PGCD")
    print("-" * 40)
    r = resultats['pgcd']
    print(f"   PGCD(G, P) = G : {r['egal_guasti']}")
    print(f"   -> {r['interpretation']}")
    
    print("\n4. PALIMPSESTE DIFFERENCE (|G - P|)")
    print("-" * 40)
    r = resultats['difference']
    print(f"   Ligne 1 toute nulle : {r['ligne1_nulle']}")
    print(f"   -> {r['interpretation']}")
    
    print("\n" + "=" * 60)
    print("HIERARCHIE DES PUISSANCES")
    print("=" * 60)
    print("""
    Diagonale de Guasti     :  1, 2, 3, 4, 5...    = n^1
    Diagonale de Pythagore  :  1, 4, 9, 16, 25...  = n^2
    Diagonale de G * P      :  1, 8, 27, 64, 125.. = n^3
    
    -> Le palimpseste multiplicatif "monte d'une dimension" !
    """)


if __name__ == "__main__":
    afficher_analyse()
