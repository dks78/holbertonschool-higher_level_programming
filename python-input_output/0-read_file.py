#!/usr/bin/python3
def read_file(filename=""):
    """Lit un fichier texte UTF-8 et affiche son contenu sur stdout."""
    with open(filename, "r", encoding="utf-8") as fichier:
        print(fichier.read(), end="")  # Lire et afficher le contenu
