#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i],end="")
            count += 1
        print()
    except IndexError as e :
        print()
        False
        # Message d'erreur si l'indice est hors de la liste

    return count