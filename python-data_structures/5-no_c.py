def no_c(my_string):
    result = ""
    
    # Parcours chaque caractère de la chaîne
    for char in my_string:
        # Si le caractère n'est pas 'c' ou 'C', on l'ajoute à result
        if char.lower() != 'c':
            result += char
    
    # Retourne la chaîne modifiée
    return result
