#!/usr/bin/python3
def text_indentation(text):
    for i in text:
        if i == "." or i == "?" or i == ":" or i == ",":
            print(i, end="\n")
            print()
        else:
            print(i, end="")