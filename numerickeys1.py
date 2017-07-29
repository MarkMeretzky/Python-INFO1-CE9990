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
        s = input("Please type an integer from 1 to 10: ")
    except EOFError:
        sys.exit(0)

    try:
        n = int(s)
    except ValueError:
        print("Sorry,", s, "isn't an integer.  Try again.")
        print()
        continue   #Go back up tp the word "while".

    try:
        word = words[n]
    except KeyError:
        print("Sorry, \"", s, "\" is not an integer in the range 1 to 10.",
            sep = "")
        print()
        continue   #Go back up to the word "while".
    
    print("The word for ", n, " is \"", word, "\".", sep = "")
    print()
