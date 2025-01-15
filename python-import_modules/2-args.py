#!/usr/bin/python3
import sys

def no_of_argu(*args):
    return len(args)

def display_arguments():
    # Utiliser sys.argv pour obtenir les arguments passés
    args = sys.argv[1:]  # On exclut le nom du script, qui est sys.argv[0]
    num_args = no_of_argu(*args)

    # Affiche le nombre d'arguments et le type (argument ou arguments)
    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''} :")

        # Affiche chaque argument avec sa position
        for i, arg in enumerate(args, 1):s
            print(f"{i}: {arg}")

# Appel de la fonction
if __name__ == "__main__":
    display_arguments()
