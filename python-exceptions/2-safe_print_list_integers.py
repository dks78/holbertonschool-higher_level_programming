#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(min(x, len(my_list))):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]),end="") 
                count += 1  # Incrémente le compteur des entiers imprimés
    except Exception as e:
        print("Error: ", e)
    print()
    return count 