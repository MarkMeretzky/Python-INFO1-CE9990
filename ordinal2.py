"""
ordinal2.py

Print the ordinal form of a number.
Steer the computer in one of five possible directions using if/elif/elif/else.
"""

import sys

try:
    n = input("Please type a positive whole number: ")
except EOFError:
    sys.exit(1)

try:
    n = int(n)
except ValueError:
    print("Sorry,", n, "is not a whole number.")
    sys.exit(1)

if n <= 0:
    print("Sorry,", n, "is not a positive whole number.")
    sys.exit(1)

lastDigit = n % 10
last2Digits = n % 100
print("The ordinal form of", n, "is", n, end = "")

if 11 <= last2Digits and last2Digits <= 13:
    print("th", end = "")
elif lastDigit == 1:
    print("st", end = "")
elif lastDigit == 2:
    print("nd", end = "")
elif lastDigit == 3:
    print("rd", end = "")
else:
    print("th", end = "")   #all other numbers

print(".")
sys.exit(0)
