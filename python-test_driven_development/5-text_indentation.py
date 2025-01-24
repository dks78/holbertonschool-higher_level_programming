#!/usr/bin/python3
"""
module : function to indation text

"""
def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these characters: '.', '?', ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.

    Examples:
    >>> text_indentation("Hello. How are you? I'm fine: thanks!")
    Hello.
    
    How are you?
    
    I'm fine:
    
    thanks!
    
    >>> text_indentation("")
    
    >>> text_indentation("No special chars here")
    No special chars here
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        # Si on trouve un des caractères qui nécessite un saut de ligne
        if text[i] in ".?:":
            print(text[i], end="\n")  # Ajouter un seul saut de ligne après le caractère
            i += 1
            # Ignorer les espaces blancs après le caractère spécial
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")  # Imprimer les caractères normalement
            i += 1