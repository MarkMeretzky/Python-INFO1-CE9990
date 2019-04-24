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
    print(f"Sorry, {years} is not a number.")
    years = 0.0
    printf(f"I'll assume your age is {years} years.")

dogYears = round(years / 7)
print(f"That's about {dogYears} dog years!")
sys.exit(0)
