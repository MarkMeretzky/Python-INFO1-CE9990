"""
octave.py

Print the lengths of a set of 13 organ pipes spanning one octave.
Shortest pipe is 100 inches long.
"""

import sys

#factor is the number which, when multiplied by itself 12 times, gives you 2.
#Parentheses perform the division before the exponentiation.
factor = 2 ** (1/12)

i = 0
length = 100   #of shortest pipe

while True:
    #Print 5 digits to the right of the decimal point.
    #(Can't manufacture the pipes to any greater level of precision.)
    print("{:2}   {:.5f} inches".format(i, length))
    if length >= 200:
        break
    i += 1
    length *= factor

sys.exit(0)
