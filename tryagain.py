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
print(f"Thank you for typing in the float number {f}.")

mantissa, exponent = math.frexp(f)
dig = sys.float_info.mant_dig   #number of binary digits in the mantissa

paragraph=f"""\
It is stored internally as the pair of integers {mantissa * 2**dig:.0f} and {exponent}.
{f} = ({mantissa * 2 ** dig:.0f} / (2 ** {dig})) * (2 ** {exponent}) = {mantissa} * {2 ** exponent}
The fraction {mantissa * 2 ** dig:.0f} / (2 ** {dig}) is the mantissa.
The number {exponent} is the exponent."""

print(paragraph)
sys.exit(0)
