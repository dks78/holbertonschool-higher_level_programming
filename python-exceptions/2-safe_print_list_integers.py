#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        if x > len(my_list):  # Si x est plus grand que la longueur de la liste
            raise IndexError("list index out of range")  # Lancer une exception manuellement
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError as e:
        print(f"\n{e}")  # Afficher le message d'erreur IndexError
    print()
    return count