"""
inout.py

Prompt the user for their age.
Then tell them how old they are in dog years. 
"""

import sys

try:
    years = input("How old are you? ")
except EOFError:
    print("I'll assume you're a newborn.")
    years = 0.0

try:
    years = float(years)
except ValueError:
    print("I'll assume you're a neonate.")
    years = 0.0

dogYears = round(years / 7)
print("That's about", dogYears, "dog years!")
sys.exit(0)
