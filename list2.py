"""
list2.py

Demonstrate a list of numbers.
"""

import sys

months = [
    31,   #January
    28,   #February
    31,   #March
    30,   #April
    31,   #May
    30,   #June
    31,   #July
    31,   #August
    30,   #September
    31,   #October
    30,   #November
    31    #December
]

n = len(months)   #Don't have to count them yourself.

print(f"A year has {n} months.")
print(f"The first month has {months[0]} days.")
print(f"The second month has {months[1]} days.")
print(f"The third month has {months[2]} days.")
print(f"The twelfth month has {months[11]} days.")

print(f"The last month has {months[-1]} days.")
print(f"The next-to-last month has {months[-2]} days.")
print(f"The third-to-last month has {months[-3]} days.")

sys.exit(0)
