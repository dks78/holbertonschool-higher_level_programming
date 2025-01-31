#!/usr/bin/python3

from rectangle import Rectangle

# Création de deux instances de Rectangle
rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 6)

# Test des méthodes area et perimeter
print("Aire de rect1:", rect1.area())  # Devrait afficher 20
print("Périmètre de rect1:", rect1.perimeter())  # Devrait afficher 18

print("Aire de rect2:", rect2.area())  # Devrait afficher 18
print("Périmètre de rect2:", rect2.perimeter())  # Devrait afficher 18

# Test de la méthode bigger_or_equal
plus_grand = Rectangle.bigger_or_equal(rect1, rect2)
print("Le plus grand rectangle est:", plus_grand)

# Vérification du nombre d'instances
print("Nombre d'instances:", Rectangle.get_number_of_instances())

# Suppression d'une instance
del rect1
print("Nombre d'instances après suppression:", Rectangle.get_number_of_instances())
