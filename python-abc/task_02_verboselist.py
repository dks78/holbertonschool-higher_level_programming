#!/usr/bin/env python3
class VerboseList(list):
    def append(self,item):
        print(f"Added {[item]} to the list")
        super().append(item)
    def extend(self, iterable):
        print(f"Extended the list with [{len(iterable)}] items.")  # Affiche le nombre d'éléments ajoutés
        super().extend(iterable)  # Ajoute les éléments à la liste
    def remove(self,item):
        print(f"Removed {[item]} from the list.")
        super().remove(item)
    def pop(self, index=-1):
        item = super().pop(index)  # Supprime l'élément et récupère sa valeur
        print(f"Popped {[item]} from the list.")  # Affiche le message
        return item  # Retourne l'élément supprimé (comme le fait la méthode pop())
