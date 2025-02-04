#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Retourne True si l'objet est exactement une instance de la classe a_class,
    sans tenir compte des sous-classes.
    
    Arguments:
    obj : l'objet à vérifier
    a_class : la classe à comparer
    
    Retourne:
    True si obj est une instance exacte de a_class, sinon False.
    """
    return type(obj) == a_class
