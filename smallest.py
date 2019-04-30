"""
smallest.py

What is the smallest positive number of type float?
"""

import sys

x = 1.0

while True:
    print(f"{x:23}")
    if x == 0:
        break
    x /= 2   #means x = x / 2, in other words, halve the value of x

sys.exit(0)
