"""
inout.py

Prompt the user for their age.
Then tell them how old they are in dog years. 
"""

import sys

try:
    years = input("How old are you? ")
except EOFError:
    sys.exit(0)

try:
    years = float(years)
except ValueError:
    print("Sorry,", years, "is not a number.")
    years = 0.0
    print("I'll assume your age is ", years, ".", sep = "")

dogYears = round(years / 7)
print("That's about", dogYears, "dog years!")
sys.exit(0)
