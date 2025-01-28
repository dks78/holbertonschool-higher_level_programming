"""
Ce module contient des fonctions et des classes pour gérer des formes géométriques,
y compris la définition de carrés et de calculs associés.

Les fonctions dans ce module permettent de calculer des propriétés géométriques comme l'aire,
le périmètre, etc.
"""

def aire_carre(cote):
    """
    Calcule l'aire d'un carré.

    Arguments:
    cote (float): La longueur du côté du carré.

    Retour:
    float: L'aire du carré, c'est-à-dire cote^2.
    
    Exemple:
    >>> aire_carre(5)
    25
    """
    return cote ** 2

def perimetre_carre(cote):
    """
    Calcule le périmètre d'un carré.

    Arguments:
    cote (float): La longueur du côté du carré.

    Retour:
    float: Le périmètre du carré, c'est-à-dire 4 * cote.

    Exemple:
    >>> perimetre_carre(5)
    20
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
        
        Exemple:
        >>> s = Square(5)
        >>> s.aire()
        25
        """
        return self.cote ** 2

    def perimetre(self):
        """
        Calcule le périmètre du carré.

        Retour:
        float: Le périmètre du carré.
        
        Exemple:
        >>> s = Square(5)
        >>> s.perimetre()
        20
        """
        return 4 * self.cote
