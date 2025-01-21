#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):  # Ensure we don't exceed the list size
            if isinstance(my_list[i], int):  # Check if the element is an integer
                print("{:d}".format(my_list[i]), end="")  # Print integer without space
                count += 1
    except IndexError:
        raise
    print()
    return count