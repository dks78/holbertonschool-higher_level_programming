#!/usr/bin/python3
def print_square(size):
    for i in range(size):
    # Loop to print pattern
        for j in range(size):
            print('#' , end=' ')
        print()
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")