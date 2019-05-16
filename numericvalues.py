"""
numericvalues.py

A dictionary with numeric values.
"""

import sys

numbers = {
    "one":    1,
    "two":    2,
    "three":  3,
    "four":   4,
    "five":   5,
    "six":    6,
    "seven":  7,
    "eight":  8,
    "nine":   9,
    "ten":   10
}

while True:
    try:
        word = input("Please type the word for a number from one to ten: ")
    except EOFError:
        sys.exit(0)

    try:
        number = numbers[word]   #number is an int
    except KeyError:
        print(f'Sorry, "{word}" is not a number in the range one to ten.')
        print()
        continue   #Go back up to the word "while".
    
    print(f"The word {word} is the number {number}.")
    print()
