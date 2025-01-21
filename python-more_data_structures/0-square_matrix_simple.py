#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Initialisation de la nouvelle matrice vide
    new_matrix = []
    
    # Parcours de chaque ligne de la matrice d'origine
    for row in matrix:
        # Création d'une nouvelle ligne vide pour stocker les carrés
        new_row = []
        
        # Parcours de chaque élément de la ligne
        for element in row:
            # Calcul du carré de l'élément
            squared_element = element ** 2
            # Ajout du carré à la nouvelle ligne
            new_row.append(squared_element)
        
        # Ajout de la nouvelle ligne à la nouvelle matrice
        new_matrix.append(new_row)
    
    # Retour de la nouvelle matrice
    return new_matrix