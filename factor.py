"""
factor.py

Output the prime factors of an integer, one per line, in increasing order.
For example, the factors of 60 are 2, 2, 3, 5.
"""

import sys

n = input("Please type an integer: ")
n = int(n)

factor = 2
while factor <= n:

    while n % factor == 0: #while factor actually does divide n
        print(factor)
        n = n / factor     #or n /= factor

    factor += 1

sys.exit(0)
