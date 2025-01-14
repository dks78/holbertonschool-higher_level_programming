#!/usr/bin/env python3

def fizzbuzz():
    for i in range(1, 101):  # Parcours des nombres de 1 à 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")  # Si divisible par 3 et 5
        elif i % 3 == 0:
            print("Fizz", end=" ")  # Si divisible uniquement par 3
        elif i % 5 == 0:
            print("Buzz", end=" ")  # Si divisible uniquement par 5
        else:
            print(i, end=" ")  # Si ce n'est pas un multiple de 3 ou 5, imprimer le nombre  # Ajoute un retour à la ligne à la fin
