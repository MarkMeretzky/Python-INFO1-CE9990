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

    firstCharacter = word[0]
    rest = word[1:]   #the rest of the word, i.e., all but the first character
    pigLatin = rest + firstCharacter + "ay"
    print(pigLatin)
