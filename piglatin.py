"""
piglatin.py

Translate the input word from English to Pig Latin.
"""

import sys

while True:

    try:
        word = input("Please type a word: ")
    except EOFError:
        sys.exit(0)

    firstLetter = word[0]
    rest = word[1:]
    pigLatin = rest + firstLetter + "ay"
    print(pigLatin)
