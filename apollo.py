"""
apollo.py

Demonstrate three ways to loop through the characters of a string.
"""

import sys

s = "APOLLO"

i = 0
while i < len(s):
    print(s[i])
    i += 1

print()   #Skip a line (i.e., output a line consisting of one newline character).

for i in range(0, len(s)):   #Don't need to write the 0,
    print(s[i])

print()

for c in s:
    print(c)

sys.exit(0)
