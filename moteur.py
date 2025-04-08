import deps.modules.fltk as fltk,deps.modules.fltk_addons as addons
from deps.map import Map

addons.init(fltk)
import os

def mainloop():
    #Variables à définir
    global w, h
    w = 600
    h = 600
    end = False
    
    fltk.cree_fenetre(w, h, redimension=True)
    map = Map()
    map.dump_img()

    def load_image():
        """
        Charge une image à partir d'un chemin donné.
        
        Args:
            path (str): le chemin vers l'image à charger.
        
        Returns:
            fltk.Image: l'image chargée.
        """
        fltk.image(w//2, h//2, 'deps/map.png', ancrage='center', hauteur=h, largeur=w)

    load_image()

    while not end:
        fltk.mise_a_jour()

        ev = fltk.donne_ev()

        if ev is None: continue
        elif ev[0] =="Quitte":
            fltk.ferme_fenetre()
            end = True
            break

        elif ev[0] == "ClicGauche":
            objects = addons.liste_objets_survoles()
        elif ev[0] == 'Redimension':
            fltk.efface_tout()
            load_image()



mainloop()