#!/usr/bin/python3
import sys

def no_of_argu():
    return len(sys.argv) - 1  # Exclure le nom du script (sys.argv[0])

def display_arguments():
    num_args = no_of_argu()

    # Affiche le nombre d'arguments
    if num_args == 0:
        print("Number of argument(s): .")
    else:
        print(f"Number of argument(s): {num_args} argument{'s' if num_args > 1 else ''} :")

        # Affiche chaque argument avec sa position
        for i in range(1, num_args + 1):  # Les arguments commencent à l'index 1
            print(f"{i}: {sys.argv[i]}")

# Le code ne doit pas être exécuté si ce fichier est importé
if __name__ == "__main__":
    display_arguments()
