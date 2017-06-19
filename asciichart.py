"""
asciichart.py

Print the printable ASCII characters (the ones in the range 32 to 126 inclusive)
and their code numbers in decimal, octal, and hexadecimal.

format string:
Print the character whose code number is the first argument.
The second argument will be printed in decimal, left padded with spaces if
necessary to make it a total of 3 characters.
The third argument will be printed in octal, left-padded with spaces if
necessary to make it a total of 3 characters.
The fourth argument will be printed in uppercase hexadecimal, left-padded with
zeroes if necessary to make it a total of 2 characters.
"""

import sys

print("  decimal octal hex")
i = 32

while i <= 126:
    print("{:c}     {:3}   {:3o}  {:02X}".format(i, i, i, i))
    i += 1

sys.exit(0)
