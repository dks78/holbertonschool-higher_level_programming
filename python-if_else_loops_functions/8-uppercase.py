#!/usr/bin/python3
def uppercase(str):
    result = ""  # Variable pour accumuler le résultat
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # Si c'est une minuscule
            result += chr(ord(char) - 32)  # Convertir en majuscule
        else:
            result += char  # Sinon, garder le caractère inchangé
    print("{}".format(result))  # Afficher le résultat final
