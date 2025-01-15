#!/usr/bin/python3
from add_0 import add  # Importer la fonction add depuis add_0

a = 1  # Définir la valeur de a
b = 2  # Définir la valeur de b

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
