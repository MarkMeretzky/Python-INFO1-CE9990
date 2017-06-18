"""
validate.py

Keep prompting the user until he or she inputs an integer in the range 1 to 10
inclusive.
"""

import sys

while True:
    try:
        s = input("Please type an integer in the range 1 to 10 inclusive: ")
    except EOFError:
        sys.exit(1)

    try:
        f = float(s)
    except ValueError:
        print("Sorry,", s, "is not a number.")
        continue

    i = int(f)
    if i != f:
        print("Sorry,", s, "is not an integer.");
        continue

    if 1 <= i and i <= 10:
        break

    print("Sorry,", i, "is not in the range 1 to 10 inclusive.")

print("Thank you. ", i, "is acceptable.")
sys.exit(0)
