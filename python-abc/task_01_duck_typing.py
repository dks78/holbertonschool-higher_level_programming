
#!/usr/bin/env python3
import math
from abc import ABC,abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire"""
        pass    
    
    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer l'aire"""
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi* self.radius
class Rectangle(Shape):
    def __init__(self,width,height):
            self.width = width
            self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
def shape_info(shape):
    # Appel des méthodes area() et perimeter() sur l'instance passée en argument
    print(f"Aire: {shape.area()}")
    print(f"Périmètre: {shape.perimeter()}")