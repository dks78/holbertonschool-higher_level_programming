#!/usr/bin/env python3

class Fish:
    """
    Classe représentant un Poisson.
    Cette classe contient des méthodes pour simuler le comportement d'un poisson.
    """
    def swim(self):
        """
        Simule l'action de nager du poisson.
        """
        print("The fish is swimming")
    
    def habitat(self):
        """
        Affiche où vit le poisson (dans l'eau).
        """
        print("The fish lives in water")

class Bird:
    """
    Classe représentant un Oiseau.
    Cette classe contient des méthodes pour simuler le comportement d'un oiseau.
    """
    def fly(self):
        """
        Simule l'action de voler de l'oiseau.
        """
        print("The bird is flying")
    
    def habitat(self):
        """
        Affiche où vit l'oiseau (dans le ciel).
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    Classe représentant un Poisson Volant.
    Cette classe hérite à la fois de Fish et Bird et surcharge les méthodes
    pour simuler un poisson qui peut voler et nager.
    """
    def fly(self):
        """
        Simule l'action de voler du poisson volant.
        Appelle la méthode fly de la classe Bird et affiche un message supplémentaire.
        """
        Bird.fly(self)  # Appel de la méthode fly de la classe Bird
        print("The flying fish is soaring!")
        
    def swim(self):
        """
        Simule l'action de nager du poisson volant.
        Appelle la méthode swim de la classe Fish et affiche un message supplémentaire.
        """
        Fish.swim(self)  # Appel de la méthode swim de la classe Fish
        print("The flying fish is swimming!")
    
    def habitat(self):
        """
        Affiche où vit le poisson volant.
        Indique que le poisson volant vit à la fois dans l'eau et dans le ciel.
        """
        print("The flying fish lives both in water and the sky!")

# Instancier un objet de FlyingFish
# Devrait afficher le message concernant l'habitat
