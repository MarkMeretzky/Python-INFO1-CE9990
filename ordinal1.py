"""
ordinal1.py

Print the ordinal form of a number.
Steer the computer in one of four possible directions using if/elif/elif/else.
"""

import sys

n = input("Please type a positive whole number: ")
n = int(n)

lastDigit = n % 10
print("The ordinal form of", n, "is", n, end = "")

if lastDigit == 1:
    print("st", end = "")
elif lastDigit == 2:
    print("nd", end = "")
elif lastDigit == 3:
    print("rd", end = "")
else:
    print("th", end = "")   #all other numbers

print(".")
sys.exit(0)
