"""
countcalls.py

This function can count how many times it's been called.
It increments the value of a global variable.
"""

import sys

count = 0

def counter():
    global count
    count += 1
    print("This is call number ", count, ".", sep = "")

counter()
counter()
counter()
sys.exit(0)
