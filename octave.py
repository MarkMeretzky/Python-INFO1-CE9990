"""
octave.py

Print the lengths of a set of 13 organ pipes spanning one octave.
Shortest pipe is 100 inches long.
"""

import sys

#Print 5 digits to the right of the decimal point.
#(Can't manufacture the pipes to any greater level of precision.)
f = "{:2}   {:.5f} inches"

#factor is the number which, when multiplied by itself 12 times, gives you 2.
#Division must come before exponentiation.
factor = 2 ** (1/12)

i = 0
length = 100   #of shortest pipe

while True:
    print(f.format(i, length))
    if length >= 200:
        break
    i += 1
    length *= factor

sys.exit(0)
