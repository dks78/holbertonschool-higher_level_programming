#!/usr/bin/python3
# 2-print_alphabet.py
# Brennan D Baraban <375@holbertonschool.com>
"""Print the alphabet in lowercase, not followed by a new line."""

for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        print("{}".format(chr(letter)), end="")
