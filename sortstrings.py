"""
sortstrings.py

Sort a list of strings in alphabetical order.
"""

import sys

animals = [
    "monkey",  # 0
    "rooster", # 1
    "dog",     # 2
    "pig",     # 3
    "rat",     # 4
    "ox",      # 5
    "tiger",   # 6
    "hare",    # 7
    "dragon",  # 8
    "snake",   # 9
    "horse",   #10
    "sheep"    #11
]

animals.sort()

for animal in animals:
    print(animal)

sys.exit(0)
