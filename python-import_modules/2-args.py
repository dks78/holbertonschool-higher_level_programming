#!/usr/bin/python3
def no_of_argu(*args):
    return len(args)

def display_arguments(*args):
    # Récupère le nombre d'arguments
    num_args = no_of_argu(*args)

    # Affiche le nombre d'arguments et le type (argument ou arguments)
   
    print(f"{num_args } arguments :")
    

    print(args[0],": Hello")
    print(args[1],": Welcome")
    print(args[2],": To ")
    print(args[3],": The ")
    print(args[4],": Best")
    print(args[5],": School")

# Variables
a = 1
b = 3

# Appel de la fonction avec plusieurs arguments
display_arguments(1, 2, 3, 4, 5, 6)
