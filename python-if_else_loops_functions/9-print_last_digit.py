def print_last_digit(number):
    # Calculer le dernier chiffre en prenant la valeur absolue
    last_digit = abs(number) % 10
    
    # Afficher le dernier chiffre sans ajouter une nouvelle ligne
    print(last_digit, end="")  # Affiche sans sauter de ligne
    
    # Retourner le dernier chiffre pour répondre à la condition
    return last_digit