"""
powers.py

Print the powers of 2 less than a million.
One million is a seven-digit number.
We're printing numbers smaller than a million, so we need only 6 digits.
"""

import sys
import math   #for log

i = 0
p = 1

while p < 1_000_000:   #Test at the top of the loop.
    print(f"2 ** {i:2} = {p:6}")
    i += 1   #means i = i + 1
    p *= 2   #means p = p * 2

print()   #Skip a line (i.e., output a line consisting only of one newline).
print(f"The log to the base 2 of {1_000_000:,} is {math.log(1_000_000, 2)}")
sys.exit(0)
