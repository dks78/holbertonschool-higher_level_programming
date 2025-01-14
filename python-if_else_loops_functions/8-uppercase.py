#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # Vérifier si le caractère est une minuscule
            print(chr(ord(char) - 32), end="")  # Convertir en majuscule et afficher
        else:
            print(char, end="")  # Si c'est déjà une majuscule ou un autre caractère, afficher tel quel
    print()  # Ajouter une nouvelle ligne après la chaîne imprimée
