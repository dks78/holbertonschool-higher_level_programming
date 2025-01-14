#!/usr/bin/python3

def uppercase(str):
    for char in str:  # Parcourt chaque caractère de la chaîne
        if ord('a') <= ord(char) <= ord('z'):  # Si c'est une minuscule
            print(chr(ord(char) - 32), end="")  # Convertir en majuscule
        else:
            print(char, end="")  # Si ce n'est pas une minuscule, on l'imprime tel quel
    print()  # Ajouter une nouvelle ligne après la chaîne imprimée
