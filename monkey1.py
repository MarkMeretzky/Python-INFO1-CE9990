"""
monkey1.py

Demonstrate how they programmed before they invented lists.
"""

import sys

while True:
    try:
        year = input("Please type a year: ")
    except EOFError:
        sys.exit(0)

    try:
        year = int(year)
    except ValueError:
        print("Sorry,", year, "is not an integer.")
        continue

    remainder = year % 12   #remainder is an integer in the range 0 to 11 inclusive

    if remainder == 0:
        animal = "monkey"
    elif remainder == 1:
        animal = "rooster"
    elif remainder == 2:
        animal = "dog"
    elif remainder == 3:
        animal = "pig"
    elif remainder == 4:
        animal = "rat"
    elif remainder == 5:
        animal = "ox"
    elif remainder == 6:
        animal = "tiger"
    elif remainder == 7:
        animal = "hare"
    elif remainder == 8:
        animal = "dragon"
    elif remainder == 9:
        animal = "snake"
    elif remainder == 10:
        animal = "horse"
    elif remainder == 11:
        animal = "sheep"
    else:
        print("bad remainder", remainder)
        sys.exit(1)

    print(year, " was the year of the ", animal, ".", sep = "")
