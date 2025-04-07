import modules.fltk as fltk,modules.fltk_addons as addons
from modules.tiles_converter import creation_plateau
from modules.terrain import Terrain
from solveur.solveur import solveur
from solveur.astar import solveur_optimal
from solveur.bfs import solveur_bfs
addons.init(fltk)
import os

def mainloop():
    #Variables à définir
    global width, height
    width = 600
    height = 600
    end = False
    solve = True
        
    dim_plateau = 40
    plateau = Terrain(creation_plateau(dim_plateau, 10))
    plateau.display().save('map.png')


    fltk.cree_fenetre(width, height, redimension=True)


    def num_to_hex(blue):
        hex_str = hex(min(255, blue))[2:].upper().zfill(2)
        return f"#FF00{hex_str}"

    def draw_arrow(coord, vect):
        l, w = fltk.hauteur_fenetre(), fltk.largeur_fenetre()
        coord = max(1, coord[0]), max(1, coord[1])
        unit = (l//dim_plateau, w//dim_plateau)
        norme = ((vect[0])**2*unit[0] + (vect[1])**2)**0.5
        couleur = num_to_hex(int(norme))
        x, y = coord[0] + vect[0] * unit[0], coord[1] + vect[1] * unit[1]
        c = coord[1], coord[0], y, x
        fltk.cercle(c[0], c[1], 5, couleur='blue', remplissage='blue')
        fltk.ligne(c[0], c[1], c[2], c[3], couleur=couleur, epaisseur=5) 
        fltk.fleche(c[0], c[1], c[2], c[3], couleur=couleur, epaisseur=5)
        return c[3], c[2]
    

    def draw_path(intermediate):
        coord = plateau.start
        for i, vect in enumerate(intermediate):
            coord = draw_arrow(coord, vect)



    if solve:
        # solution = solveur_optimal(plateau.grid)
        # solution = solveur(plateau.grid, plateau.start)
        solution = solveur_bfs(plateau.grid, plateau.start, plateau.end)

    def draw():
        l, w = fltk.hauteur_fenetre(), fltk.largeur_fenetre()
        fltk.image(w//2, l//2, 'map.png', ancrage='center', hauteur=l, largeur=w)
        if solve:
            if not solution[0]:
                fltk.texte(w//2, l//2, "Aucune solution trouvée", ancrage='center',couleur='red')
            coord = plateau.start
            draw_path(solution[1])

    draw()

    while not end:
        fltk.mise_a_jour()

        ev = fltk.donne_ev()

        if ev is None: continue
        elif ev[0] =="Quitte":
            fltk.ferme_fenetre()
            break

        elif ev[0] == "ClicGauche":
            objects = addons.liste_objets_survoles()
        elif ev[0] == 'Redimension':
            fltk.efface_tout()
            draw()


mainloop()