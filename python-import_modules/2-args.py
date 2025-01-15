#!/usr/bin/python3
# 2-args.py
# Brennan D Baraban <375@holbertonschool.com>

#le fichier n'est pas importe donc  __name__  est égale au name
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    #sys.argv est égale a systéme argument
    count = len(sys.argv) - 1#contera le nombre de commande placer a l'intéreieur du terminale 
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
