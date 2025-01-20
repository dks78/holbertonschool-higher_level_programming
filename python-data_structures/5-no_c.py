#!/usr/bin/python3
def no_c(my_string):
    new_string = ""  # Nouvelle variable pour stocker le résultat
    for i in range(len(my_string)):  # Boucle pour parcourir chaque caractère de la chaîne
        # Si le caractère n'est pas 'c' ni 'C', on l'ajoute à la nouvelle chaîne
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += my_string[i]  # Ajoute le caractère à la nouvelle chaîne
    
    return new_string