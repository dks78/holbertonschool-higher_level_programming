#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    # Vérification si les listes sont trop courtes
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
    
    # Parcours des indices jusqu'à la longueur spécifiée
    for i in range(list_length):
        try:
            # Vérification de la division par zéro et du type des éléments
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] == 0:
                    print("division by 0")
                    result.append(0)  # Division par zéro
                else:
                    result.append(my_list_1[i] / my_list_2[i])  # Division correcte
            else:
                print("wrong type")
                result.append(0)  # Mauvais type de données
        except IndexError:
            # Si un indice dépasse la longueur des listes
            print("out of range")
            result.append(0)  # Ajouter 0 dans le cas d'une exception (hors de portée)
        except Exception as e:
            # Si une autre exception se produit
            print(f"Error: {e}")
            result.append(0)

    return result
