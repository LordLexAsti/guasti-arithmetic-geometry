import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# --- CONNEXION TRIADIA ---
def connect_to_core():
    try:
        current_path = Path(__file__).resolve()
        sibling_path = current_path.parent.parent.parent / "guasti-transform"
        if sibling_path.exists() and str(sibling_path) not in sys.path:
            sys.path.insert(0, str(sibling_path))
            import guasti_transform
            return True
    except Exception:
        pass
    return False

HAS_CORE = connect_to_core()

class GrilleGuasti:
    """
    La Grille de Guasti (Définition Officielle v1.2).
    Ce n'est PAS une table de Pythagore (i*j).
    C'est une projection de divisibilité alignée sur l'axe des entiers.
    
    - Colonnes (j) : Les Entiers Naturels (0 à N)
    - Lignes (i)   : Les Tables de diviseurs (Table de 1, Table de 2...)
    - Cellule (i,j): Active si i divise j.
    """
    
    def __init__(self, taille=100):
        self.N = taille
        self.grid = self._build_grid()
        
    def _build_grid(self):
        """
        Construit la matrice de divisibilité.
        """
        # Matrice (N+1)x(N+1). 
        grid = np.zeros((self.N + 1, self.N + 1), dtype=int)

        # Logique de construction Guasti :
        # Pour chaque table 'i' (ligne), on marque les multiples 'j' (colonne)
        for i in range(1, self.N + 1):
            # j commence à i, et avance par pas de i (i, 2i, 3i...)
            grid[i, i::i] = np.arange(i, self.N + 1, i)
                
        return grid

    def analyser_colonne(self, n):
        """
        Scan vertical de la colonne n.
        Révèle la structure intime du nombre (ses diviseurs).
        """
        if n > self.N:
            raise ValueError(f"Hors limite (N={self.N})")
            
        # Récupération de la colonne
        col_data = self.grid[:, n]
        diviseurs = np.where(col_data > 0)[0]
        
        # Calcul de la Signature Angulaire sur ce Crible
        # Point (x, y) = (n, diviseur)
        # Angle theta = arctan(diviseur / n)
        angles = []
        for div in diviseurs:
            theta = np.degrees(np.arctan2(div, n))
            angles.append(round(theta, 2))
            
        return {
            "n": n,
            "diviseurs": list(diviseurs),
            "signature": angles,
            "est_premier": len(diviseurs) == 2, # Uniquement 1 et n
            "densite_verticale": len(diviseurs) / n
        }

    def afficher(self):
        """Visualisation du Crible de Guasti."""
        plt.figure(figsize=(12, 10))
        grid_visu = np.ma.masked_where(self.grid == 0, self.grid)
        plt.imshow(grid_visu[1:, 1:], aspect='auto', interpolation='nearest', 
                   cmap='viridis', origin='upper')
        plt.title(f"Grille
