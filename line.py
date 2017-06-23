"""
line.py

Output a horizontal line of X's.
"""

import sys

inner = 1
while inner <= 36:
    print("X", end = "")
    inner += 1

print()   #Output one newline character.
sys.exit(0)
