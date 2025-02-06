#!/usr/bin/env python3
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Méthode abstraite que les sous-classes doivent implémenter"""
        pass
class Dog(Animal):
    
     def sound(self):
        """Méthode abstraite que les sous-classes doivent implémenter"""
        return "Bark"
class Cat(Animal):
     def sound(self):
        return "Meow"
    
    