"""
validate.py

Keep prompting the user until he or she inputs an integer in the range 1 to 10
inclusive.
"""

import sys

while True:
    try:
        i = input("Please type an integer in the range 1 to 10 inclusive: ")
    except EOFError:
        print("I'll assume you wanted to type in 1.")
        i = "1"

    try:
        i = int(i)
    except ValueError:
        print("I'll assume you wanted to type in 1.")
        i = 1

    if 1 <= i and i <= 10:
        break;

    print("Sorry,", i, "is out of range.  Try again.")
    print()

print("Thank you. ", i, "is acceptable.")
sys.exit(0)
