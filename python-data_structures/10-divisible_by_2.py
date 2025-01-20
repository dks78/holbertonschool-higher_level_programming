#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Retourne une liste de booléens indiquant si chaque élément 
    de la liste est divisible par 2.

    Args:
        my_list (list): Liste d'entiers.

    Returns:
        list: Nouvelle liste de booléens.
    """
    result = []
    for number in my_list:
        if number % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
