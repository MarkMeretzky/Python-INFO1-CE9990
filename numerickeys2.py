"""
numerickeys2.py

A list is simpler than a dictionary whose keys are consecutive integers.
"""

import sys

words = [
    None,   #dummy item
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
        print(f'Sorry, "{s}" is not an integer.')
        print("Try again.")
        print()
        continue   #Go back up to the word "while".

    try:
        if n == 0:
            raise IndexError
        word = words[n]
    except IndexError:
        print(f"Sorry, {s} is not an integer in the range 1 to 10.")
        print("Try again.")
        print()
        continue   #Go back up to the word "while".
    
    print(f'The word for {n} is "{word}".')
    print()
