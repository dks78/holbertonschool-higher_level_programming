#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Récupérer le dernier chiffre correctement, en tenant compte des nombres négatifs
if number < 0:
    LastNumber = -(-number % 10)  # Gère le dernier chiffre signé pour les négatifs
else:
    LastNumber = number % 10

# Affichage en fonction des consignes
if LastNumber > 5:
    print(f"Last digit of {number} is {LastNumber} and is greater than 5")
elif LastNumber == 0:
    print(f"Last digit of {number} is {LastNumber} and is 0")
else:
    print(f"Last digit of {number} is {LastNumber} and is less than 6 and not 0")
