"""
ordinal2.py

Print the ordinal form of a number.
Steer the computer in one of five possible directions using if/elif/elif/elif/else.
"""

import sys

try:
    n = input("Please type a positive whole number: ")
except EOFError:
    sys.exit(1)

try:
    n = int(n)
except ValueError:
    print(f"Sorry {n} is not a whole number.")
    sys.exit(1)

if n <= 0:
    print(f"Sorry, {n} is not a positive whole number.")
    sys.exit(1)

lastDigit = n % 10
last2Digits = n % 100

if 11 <= last2Digits and last2Digits <= 13: #or if 11 <= last2Digits <= 13:
    suffix = "th"
elif lastDigit == 1:
    suffix = "st"
elif lastDigit == 2:
    suffix = "nd"
elif lastDigit == 3:
    suffix = "rd"
else:
    suffix = "th"   #all other numbers

print(f"The ordinal form of {n} is {n}{suffix}.")
sys.exit(0)
