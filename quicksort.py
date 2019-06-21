"""
quicksort.py

A function that sorts a list or tuple.
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
    2017,
    1945
]


def quicksort(a):
    "Return a sorted list of the items in a."
    assert isinstance(a, list) or isinstance(a, tuple)

    if len(a) <= 1:
        return a             #a is already in order.

    pivot = a[len(a) // 2]   #the middle item
    smallValues  = [item for item in a if item <  pivot]
    mediumValues = [item for item in a if item == pivot]
    bigValues    = [item for item in a if item >  pivot]

    return quicksort(smallValues) + mediumValues + quicksort(bigValues)


for year in quicksort(years):
    print(year)

sys.exit(0)
