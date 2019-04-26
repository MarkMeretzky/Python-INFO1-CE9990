"""
smallest.py

What is the smallest positive number of type float?
"""

import sys
import math

x = 1.0
while x > 0:
    mantissa, exponent = math.frexp(x)
    print(f"{x:23} = {mantissa} * 2 ** {exponent:5}")
    x /= 2   #means x = x / 2, in other words, halve the size of x

print()
print(f"sys.float_info.min = {sys.float_info.min}")
print(f"sys.float_info.min_exp = {sys.float_info.min_exp}")
sys.exit(0)
