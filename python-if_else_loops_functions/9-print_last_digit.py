# 9-print_last_digit.py
def print_last_digit(number):
    last_digit = abs(number) % 10  # Utiliser abs pour obtenir la valeur absolue
    print(last_digit, end="")  # Afficher la dernière valeur sans sauter de ligne
