"""
powers.py

Print the powers of 2 less than a million. 
"""

import sys
import math   #for log

i = 0
p = 1

while p < 1000000:
    #One million is a seven-digit number.
    #We're printing numbers smaller than a million, so we need only six digits.
    print(f"2 ** {i:2} = {p:6}")
    i += 1   #means i = i + 1
    p *= 2   #means p = p * 2

print()   #skip a line (i.e., output a line consisting only of one newline)
print(f"The log to the base 2 of 1000000 is{math.log(1000000, 2)})
sys.exit(0)
