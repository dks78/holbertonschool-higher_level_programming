#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Créer une nouvelle liste pour stocker les résultats
    result = []
    
    # Parcourir chaque élément de la liste d'origine
    for number in my_list:
        # Vérifier si le nombre est divisible par 2
        if number % 2 == 0:
            result.append(True)  # Ajouter True si divisible par 2
        else:
            result.append(False)  # Ajouter False sinon
    
    return result  # Retourner la nouvelle liste
