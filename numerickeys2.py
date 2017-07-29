"""
numerickeys2.py

A list is simpler than a dictionary whose keys are consecutive integers.
"""

import sys

words = [
    None,
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten"
]

while True:
    try:
        s = input("Please type an integer from 1 to 10: ")
    except EOFError:
        sys.exit(0)

    try:
        n = int(s)
    except ValueError:
        print("Sorry, \"", s, "\" is not an integer.", sep = "")
        print("Try again.")
        print()
        continue   #Go back up tp the word "while".

    try:
        if n == 0:
            raise KeyError
        word = words[n]
    except KeyError:
        print("Sorry, \"", s, "\" is not an integer in the range 1 to 10.",
            sep = "")
        print("Try again.")
        print()
        continue   #Go back up to the word "while".
    
    print("The word for ", n, " is \"", word, "\".", sep = "")
    print()
