#!/usr/bin/python3
# 0_add.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    
    from calculator_1  import add , sub , mul , div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
