"""
beer.py

Output the lyrics to "A Hundred Bottles of Beer on the Wall. 
"""

import sys

b = 100

while b > 0:
    print(b , "bottles of beer on the wall,")
    print(b , "bottles of beer on the wall--")
    print("If one of those bottles should happen to fall,")
    print(b - 1, "bottles of beer on he wall.")
    print()
    b -= 1

sys.exit(0)
