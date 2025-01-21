#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Vérifie si value est un entier et tente de l'imprimer
        print("{:d}".format(value))  # Si value est un entier, il sera imprimé
        return True  # Retourne True si l'entier a été imprimé avec succès
    except (ValueError, TypeError):  # Si ce n'est pas un entier, une exception est levée
        return False
         
        