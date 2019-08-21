"""
for.py

Output the integers from 0 to 9 inclusive, one per line,
using a while loop and a for loop.
"""

import sys

i = 0
while i < 10:
    print(i)
    i += 1   #or i = i + 1

print()   #Skip a line.

for i in range(0, 10, 1):   #range(0, 10) or range(10) would do the same thing
    print(i)

sys.exit(0)
