#!/usr/bin/env python3

def fizzbuzz():
    for i in range(1, 101):  # Boucle sur les nombres de 1 à 100
        if i % 3 == 0 and i % 5 == 0:  # Si divisible par 3 et 5
            print("FizzBuzz", end=" ")  # Afficher "FizzBuzz" suivi d'un espace
        elif i % 3 == 0:  # Si divisible uniquement par 3
            print("Fizz", end=" ")  # Afficher "Fizz" suivi d'un espace
        elif i % 5 == 0:  # Si divisible uniquement par 5
            print("Buzz", end=" ")  # Afficher "Buzz" suivi d'un espace
        else:  # Sinon afficher le nombre
            print(i, end=" ")