"""
tryagain.py

Have the user type in a number.
Make them try again and again until they get it right.
"""

import sys
import math

while True:
    try:
        s = input("Please type a number: ")
    except EOFError:
        sys.exit(1)

    try:
        f = float(s)
    except ValueError:
        print(f"Sorry, \"{s}\" is not a number.  Try again.")
    else:       #If no exception was raised by the float function,
        break   #abandon the loop.

#Arrive here when the loop is finished.
print()   #Skip a line.
print(f"Thank you for typing in the number {f}.")

mantissa, exponent = math.frexp(f)
print(f"Its mantissa is {mantissa} and its exponent is {exponent}.")
print(f"{f} = {mantissa} * 2 ** {exponent} = {mantissa} * {2 ** exponent}")
sys.exit(0)
