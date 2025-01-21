#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    # Vérification si les listes sont assez longues
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
    
    # Itération jusqu'à la longueur maximale des deux listes
    for i in range(list_length):
        # Si on est hors des limites des listes, ajouter 0 et passer à l'itération suivante
        if i >= len(my_list_1) or i >= len(my_list_2):
            result.append(0)
            continue
        
        # Vérifier si les éléments à cet index sont des nombres (int ou float)
        if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
            # Vérifier si la division par zéro est tentée
            if my_list_2[i] == 0:
                print("division by 0")
                result.append(0)  # Ajouter 0 au résultat si division par zéro
            else:
                result.append(my_list_1[i] / my_list_2[i])  # Effectuer la division
        else:
            print("wrong type")
            result.append(0)  # Ajouter 0 si le type est incorrect
    
    return result
