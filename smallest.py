"""
smallest.py

What is the smallest positive number of type float?
"""

import sys

x = 1.0
while x > 0:
    print(f"{x:23}")
    x /= 2   #means x = x / 2, in other words, halve the size of x

sys.exit(0)
