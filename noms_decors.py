def creer_lst_decors(path:str, listdir) -> tuple:
    """
    Création de tableaux contenant les noms des decors de la terre et de la mer.
    
    Args:
        path : le chemin vers le dossier contenant les decors.
    Returns:
        tuple: Tuple contenant 2 listes contenant les décors.
    """
    print(path)
    decors_mer = listdir(path + "/mer")
    decors_terre = listdir(path + "/terre")
    return [decors[:-4] for decors in decors_mer], [decors[:-4] for decors in decors_terre]
