#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Essaye de diviser a par b
    except ZeroDivisionError:
        print("Cannot divide by {}".format(None)) # Affiche un message d'erreur si b est 0
        return None  # Retourne None pour signaler l'échec de l'opération
    return result