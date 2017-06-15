"""
asciichart.py

Print the printable ASCII characters and their code numbers. 
"""

import sys

#format string:
#The second argument will be printed in decimal, left padded with spaces if
#necessary to make it a total of 3 characters.
#The third argument will be printed in octal, left-padded with spaces if
#necessary to make it a total of 3 characters.
#The fourth argument will be printed in uppercase hexadecimal, left-padded with
#zeroes if necessary to make it a total of 2 characters.

f = "{}     {:3}   {:3o}  {:02X}"
print("  decimal octal hex")

i = 32

while i <= 126:
    #c is the one-character string consisting of the character whose code is i.
    c = chr(i)
    print(f.format(c, i, i, i))
    i += 1

sys.exit(0)
