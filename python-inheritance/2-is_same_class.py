#!/usr/bin/python3
"""
Module is_same_class
Ce module définit une classe MyListt_sorted().
"""


def is_same_class(obj, a_class):

    """
    Retourne True si l'objet est exactement,
    sans tenir compte des sous-classes.

    Arguments:
    obj : l'objet à vérifier
    a_class : la classe à comparer

    Retourne:
    True si obj est une instance exacte de a_class, sinon False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
