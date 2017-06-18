"""
monkey2.py

Demonstrate a list as an alternative to a long chain of if/elif/else.
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
n = len(animals)

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

    remainder = year % n   #remainder is an integer in the range 0 to n-1 inclusive
    animal = animals[remainder]
    print(year, " was the year of the ", animal, ".", sep = "")
