#!/usr/bin/env python3
class SwimMixin:
    def swim(self):
        print("The creature swims!")
        
class FlyMixin:
    def fly(self):
        print("The creature flies!")
        
class Dragon(SwimMixin,FlyMixin):
    def roar(self):
        print("The dragon roars!")


dragon = Dragon()

# Appeler les méthodes héritées des mixins et la méthode spécifique à Dragon
dragon.swim()   # Affiche : "The creature swims!"
dragon.fly()    # Affiche : "The creature flies!"
dragon.roar() 