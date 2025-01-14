# 9-print_last_digit.py
def print_last_digit(number):
    last_digit = abs(number) % 10  # Calculer le dernier chiffre
    print("{}".format(last_digit), end="")
    return last_digit  # Retourner le dernier chiffre
