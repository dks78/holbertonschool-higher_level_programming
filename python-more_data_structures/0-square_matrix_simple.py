#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Créer une nouvelle matrice vide
    new_matrix = []
    
    # Parcourir chaque ligne de la matrice
    for row in matrix:
        # Créer une nouvelle ligne avec les carrés des éléments de la ligne
        new_row = [x**2 for x in row]
        # Ajouter cette nouvelle ligne à la nouvelle matrice
        new_matrix.append(new_row)
    
    return new_matrix