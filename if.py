"""
if.py

Demonstrate the if statement.
"""

import sys

trump = input("How many electoral votes did Trump get? ")
trump = int(trump)

clinton = input("How many electoral votes did Clinton get? ")
clinton = int(clinton)

print()   #Skip a line.

if trump == clinton:
    print("They're tied.  Please inform the House of Representatives")
    print("that the Electoral College is hung.")

if trump != clinton:
    print("There's a clear winner.")
    print("Thank you, electorate.")

sys.exit(0)
