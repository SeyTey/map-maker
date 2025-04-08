import PIL.Image
try:
    from cree_dico import cree_dico
except ImportError:
    from deps.cree_dico import cree_dico

class Map:
    def __init__(self, grille=None):
        """
        Initialise la carte avec une grille donnée.
        Args:
            grille: La grille représentant la carte.
        """
        if grille is None:
            # Crée une grille vide de 10x10
            self.grille = [[None for _ in range(10)] for _ in range(10)]
        else:
            self.grille = grille
        self.dim = len(self.grille), len(self.grille[0])
        import os
        self.tuiles = cree_dico('deps/tuiles')

    def dump_img(self):
        """
        Renvoie une image représentant la carte.
        """
        x,y = len(self.grille), len(self.grille[0])
        image = PIL.Image.new('RGB', (x*32, y*32), color=(255, 255, 255))
        for i in range(x):
            for j in range(y):
                tuile = self.grille[i][j]
                if tuile is not None:
                    image.paste(PIL.Image.open(self.tuiles[tuile]), (i*32, j*32))
                else:
                    # Créer une case blanche si aucune tuile n'est spécifiée
                    white_square = PIL.Image.new('RGB', (32, 32), color=(255, 255, 255))
                    image.paste(white_square, (i*32, j*32))
        image.save('map.png')
        return image
    

