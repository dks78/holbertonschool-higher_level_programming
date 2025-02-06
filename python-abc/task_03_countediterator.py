#!/usr/bin/env python3
class  CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        try:
            # Essayer de récupérer l'élément suivant
            item = next(self.iterator)
            # Incrémenter le compteur
            self.counter += 1
            return item  # Retourner l'élément itéré
        except StopIteration:
            # Lever l'exception StopIteration quand l'itérateur est épuisé
            raise StopIteration("L'itérateur a épuisé tous les éléments.")

    def get_count(self):
        return self.counter    
# Exemple d'utilisation de CountedIterator

items = [10, 20, 30, 40]  # Liste d'exemple
iterator = CountedIterator(items)

