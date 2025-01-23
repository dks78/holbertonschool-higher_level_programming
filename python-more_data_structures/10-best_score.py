#!/usr/bin/python3
def best_score(a_dictionary):
    # Vérifier que le dictionnaire n'est pas None et qu'il contient des éléments
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)