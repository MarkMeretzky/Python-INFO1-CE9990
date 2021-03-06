"""
numerickeys1.py

The keys of this dictionary are consecutive integers.
A list would be simpler than a dictionary in this case.
"""

import sys

words = {
     1: "one",
     2: "two",
     3: "three",
     4: "four",
     5: "five",
     6: "six",
     7: "seven",
     8: "eight",
     9: "nine",
    10: "ten"
}

while True:
    try:
        s = input("Please type an integer from 1 to 10 inclusive: ")
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
        word = words[n]
    except KeyError:
        print(f"Sorry, {s} is not an integer in the range 1 to 10 inclusive.")
        print("Try again.")
        print()
        continue   #Go back up to the word "while".
    
    print(f'The word for {n} is "{word}".')
    print()
