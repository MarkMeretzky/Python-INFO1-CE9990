"""
asciichart.py

Output the ASCII codes of the uppercase letters in decimal (base 10),
octal (base 8), and uppercase hexadecimal (base 16).
"""

import sys

#The third argument will be printed in octal, left-padded with spaces if
#necessary to make it a total of 3 characters.
#The fourth argument will be printed in uppercase hexadecimal, left-padded with
#zeroes if necessary to make it a total of 2 characters.

f = "{}      {}   {:3o}  {:02X}"
print("  decimal octal hex")

for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    code = ord(c)   #the ASCII code of the character c.  ord stands for ordinal.
    print(f.format(c, code, code, code))

sys.exit(0)
