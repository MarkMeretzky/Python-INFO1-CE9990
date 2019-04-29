"""
else.py

Demonstrate the if/else statement.
"""

import sys

trump = input("How many electoral votes did Trump get? ")
trump = int(trump)

clinton = input("How many electoral votes did Clinton get? ")
clinton = int(clinton)

print()   #Skip a line.

if trump == clinton:
    print("They're tied.")
    print("Please inform the House of Representatives that the Electoral College is hung.")
else:
    print("There's a clear winner.")
    print("Thank you, electorate.")

sys.exit(0)
