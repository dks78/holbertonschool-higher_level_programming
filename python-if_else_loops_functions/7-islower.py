#!/usr/bin/python3
def islower(c):
    # Vérifie si le caractère c est entre 'a' (ord('a') = 97) et 'z' (ord('z') = 122)
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
