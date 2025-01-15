#!/usr/bin/python3
# 2-args.py
# Brennan D Baraban <375@holbertonschool.com>
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    count = len(sys.argv) - 1
    totale = 0
    for i in range(count):
        totale += int(sys.argv[i + 1])
print(totale)
