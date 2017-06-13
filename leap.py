"""
leap.py

Tell whether a given year is a leap year.
Steer the computer in one of four possible directions using if/elif/elif/else.
"""

import sys

year = input("Please type a year: ")
year = int(year)

if year % 400 == 0:
    print(year, "is a leap year.")
elif year % 100 == 0:
    print(year, "is not a leap year.")
elif year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

sys.exit(0)
