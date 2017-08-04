"""
recursion.py

Print the integers from 1 to 10 inclusive using a recursive function.
"""

import sys

def upTo10(i):
    "Print the integers from i to 10 inclusive."
    if i <= 10:
        print(i)
        upTo10(i + 1)   #prints the integers from i+1 to 10 inclusive


upTo10(1)
sys.exit(0)
