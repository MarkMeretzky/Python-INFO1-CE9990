"""
powers.py

Print the powers of 2 less than a million. 
"""

import sys
import math   #for log

#One million is a seven-digit number.
#We're printing numbers smaller than a million, so we need only six digits.
f = "2 ** {:2} = {:6}"

i = 0
p = 1

while p < 1000000:
    print(f.format(i, p))
    i += 1
    p = p * 2   #or p *= 2

print()   #skip a line (i.e., output a line consisting only of one newline)
print("The log of 10000000 to the base 2 is", math.log(1000000, 2))
sys.exit(0)
