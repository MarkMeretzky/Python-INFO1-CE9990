"""
apollo.py

Demonstrate two ways to loop through the characters of a string.
"""

import sys

s = "APOLLO"

for i in range(len(s)):
    print(s[i])

print()   #Skip a line, i.e., output a line consisting of one newline character.

for c in s:
    print(c)

sys.exit(0)
