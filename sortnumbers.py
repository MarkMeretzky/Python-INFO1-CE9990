"""
sortnumbers.py

Sort a list of numbers in increasing order.
"""

import sys

years = [
    1492,
    1776,
    1066,
    1812,
    1984,
    2001,
     476,
    2019,
    1945
]

years.sort()

for year in years:
    print(f"{year:4}")

sys.exit(0)
