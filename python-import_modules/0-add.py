#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add  # Importer la fonction add depuis add_0

    a = 1  # Définir la valeur de a
    b = 2  # Définir la valeur de b

    print("{} + {} = {}".format(a, b, add(a, b)))
