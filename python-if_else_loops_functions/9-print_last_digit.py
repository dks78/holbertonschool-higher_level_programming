# 9-print_last_digit.py
def print_last_digit(number):
    last_digit = abs(number) % 10  # Calculer le dernier chiffre
    print(last_digit, end="")  # Afficher le dernier chiffre sans sauter de ligne
    return last_digit  # Retourner le dernier chiffre
