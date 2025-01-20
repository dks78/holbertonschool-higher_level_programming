#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Vérification du premier élément pour tuple_a
    first_a = tuple_a[0] if len(tuple_a) > 0 else 0
    first_b = tuple_b[0] if len(tuple_b) > 0 else 0
    
    # Vérification du deuxième élément pour tuple_a
    second_a = tuple_a[1] if len(tuple_a) > 1 else 0
    second_b = tuple_b[1] if len(tuple_b) > 1 else 0
    
    # Addition des premiers éléments
    result_first = first_a + first_b
    # Addition des deuxièmes éléments
    result_second = second_a + second_b
    
    # Retourner le nouveau tuple avec les résultats
    return (result_first, result_second)
