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
    except KeyboardInterrupt:
        sys.exit(1)

    try:
        i = int(s)
    except ValueError:
        print(f"Sorry, {s} is not an integer.")
        continue   #Go back up to the word while.

    if 1 <= i and i <= 10: #Test in the middle of the loop.
        break              #Break out of the loop.

    print(f"Sorry, {i} is not in the range 1 to 10 inclusive.")

print(f"Thank you.  {i} is acceptable.")
sys.exit(0)
