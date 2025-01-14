#!/usr/bin/env python3
# Importer la fonction 'print_last_digit' depuis '9-print_last_digit.py'
print_last_digit = __import__('9-print_last_digit').print_last_digit

# Appeler 'print_last_digit' avec différents nombres pour tester la fonction
print_last_digit(98)    # Cela devrait imprimer "8"
print_last_digit(0)     # Cela devrait imprimer "0"
r = print_last_digit(-1024)  # Cela devrait imprimer "4"
print(r)  # Cela imprimera 'None' car 'print_last_digit' ne retourne rien, mais juste imprime
