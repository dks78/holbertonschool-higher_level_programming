#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):  # j commence à i+1 pour éviter les doublons
        if i == 8 and j == 9:  # Vérifie si c'est la dernière combinaison
            print(f"{i}{j}")  # Imprime sans virgule pour la dernière combinaison
        else:
            print(f"{i}{j}, ", end="")