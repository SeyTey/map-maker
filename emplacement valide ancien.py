import os

def emplacement_valide(grille:list, i:int, j:int, nom_tuile:str):
    """
    Permet de vérifier si un emplacement est valide en fonction de la tuile.

    Args:
        grille: Grille du MapMaker.
        i : Indice i à vérifier.
        j : Indice j à vérifier.
        nom_tuile : Nom de la nouvelle tuile à vérifier.
    Returns:
        bool : True ou False en fonction de si la nouvelle tuile est plaçable ou non.
    """
    # direction de la case suivante ainsi que l'indice de la case à vérifier
    # Exemple : (1, 0, 2, 0) représente la case i + 1, j + 0 et la 3ème lettre de cette tuile
    # et le 0 représente le haut de la nouvelle tuile à placer "nom_tuile".
    cases_adjacentes = ((0, -1, 1, 3), (-1, 0, 2, 0), (0, 1, 3, 1), (1, 0, 0, 2))
    nb = 0
    for dx, dy, ind_tuile, ind_nv_tuile in cases_adjacentes:
        # On vérifie si on est pas en dehors de la grille.
        if 0 <= i + dx < len(grille) and 0 <= j + dy < len(grille[0]) and grille[i + dx][j + dy] != None:
                if grille[i + dx][j + dy][ind_tuile] == nom_tuile[ind_nv_tuile]:
                    nb += 1
        else:
            nb += 1
    if nb == 4:
        return True
    return False


def main():
    grille = [['SSSS', 'SSSS', 'SSSS', 'SSSS', None],
              ['SSSS', 'SHGS', 'SHRH', 'SHFH', None],
              ['SSSS', None, 'RMPP', 'FMMM', 'PPMM'],
              ['SSSS', 'GRGS', None, None, None],
              [None, None, None, None, None]]
    i = 2
    j = 1
    nom_tuile = 'GPGS'
    print(emplacement_valide(grille, i, j, nom_tuile))

main()