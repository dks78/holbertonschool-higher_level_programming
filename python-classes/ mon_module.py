"""
Module: geometric_shapes

Ce module contient des classes et des fonctions pour manipuler des formes géométriques simples,
comme le carré. Il permet de calculer des propriétés géométriques telles que l'aire et le périmètre.
"""

def aire_carre(cote):
    """
    Calcule l'aire d'un carré.

    Arguments:
    cote (float): La longueur du côté du carré.

    Retour:
    float: L'aire du carré, c'est-à-dire cote^2.
    """
    return cote ** 2

def perimetre_carre(cote):
    """
    Calcule le périmètre d'un carré.

    Arguments:
    cote (float): La longueur du côté du carré.

    Retour:
    float: Le périmètre du carré, c'est-à-dire 4 * cote.
    """
    return 4 * cote

class Square:
    """
    Représente un carré.

    Cette classe permet de créer un carré en spécifiant la longueur du côté.
    Elle contient des méthodes pour calculer l'aire et le périmètre du carré.
    """

    def __init__(self, cote):
        """
        Initialise un carré avec un côté donné.

        Arguments:
        cote (float): La longueur du côté du carré.
        """
        self.cote = cote

    def aire(self):
        """
        Calcule l'aire du carré.

        Retour:
        float: L'aire du carré.
        """
        return self.cote ** 2

    def perimetre(self):
        """
        Calcule le périmètre du carré.

        Retour:
        float: Le périmètre du carré.
        """
        return 4 * self.cote
