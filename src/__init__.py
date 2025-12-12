"""
Guasti Arithmetic Geometry
==========================

Une approche geometrique de la theorie des nombres.

Modules :
    - grille : Construction de la Grille de Guasti
    - signature : Calcul des signatures angulaires
    - palimpseste : Melange des grilles

Auteur : Alexandre Guasti
"""

__version__ = "1.2.0"
__author__ = "Alexandre Guasti"

# Imports des modules
from .grille import GrilleGuasti
from .signature import (
    diviseurs,
    paires_diviseurs,
    signature_angulaire,
    contient_45_degres,
    est_premier_par_signature,
    angle_jumeaux
)
from .palimpseste import (
    construire_grille_guasti,
    construire_tableau_pythagore,
    palimpseste_additif,
    palimpseste_multiplicatif,
    palimpseste_pgcd,
    palimpseste_difference,
    analyser_palimpsestes
)
