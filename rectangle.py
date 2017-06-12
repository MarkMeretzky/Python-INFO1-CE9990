"""
rectangle.py

Output a rectangle of X's.
"""

import sys

outer = 1
while outer <= 5:
    
    inner = 1
    while inner <= 36:
        print("X", end = "")
        inner += 1

    print()
    outer += 1

sys.exit(0)
