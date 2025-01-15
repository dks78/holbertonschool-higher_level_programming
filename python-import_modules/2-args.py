#!/usr/bin/python3
def no_of_argu(*args):
    return len(args)

def display_arguments(*args):
    # Récupère le nombre d'arguments
    num_args = no_of_argu(*args)

    # Affiche le nombre d'arguments et le type (argument ou arguments)
   
    print(f"{num_args } arguments :")
    
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")

# Variables
a = 1
b = 3

# Appel de la fonction avec plusieurs arguments
display_arguments("Hello", "Welcome", "To", "The", "Best", "School")
