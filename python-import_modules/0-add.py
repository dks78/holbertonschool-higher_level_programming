#!/usr/bin/python3
from add_0 import add  # Importer la fonction add depuis add_0

a = 1  # Déclarer la valeur de a
b = 2  # Déclarer la valeur de b

# Protéger le code principal avec if __name__ == "__main__":
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))  # Afficher le résultat
