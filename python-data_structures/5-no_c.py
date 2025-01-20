def no_c(my_string):
    # Crée une chaîne vide pour stocker le résultat
    result = ""
    
    # Parcours chaque caractère de la chaîne
    for char in my_string:
        # Si le caractère n'est pas 'c' ou 'C', on l'ajoute à result
        if char != 'c' and char != 'C':
            result += char
    
    # Retourne la chaîne modifiée
    return result
