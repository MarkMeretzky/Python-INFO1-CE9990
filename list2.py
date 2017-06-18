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

n = len(months)   #don't have to count them yourself

print("The first month has", months[0], "days.")
print("The second month has", months[1], "days.")
print("The third month has", months[2], "days.")
print("The twelfth month has", months[11], "days.")
print("The last month has", months[-1], "days.")
print("The next-to-last month has", months[-2], "days.")
print()

sum = 0
i = 0
while i < n:
    sum += months[i]   #means sum = sum + months[i]
    i += 1            #means i = i + 1

average = sum / n

print("A year has", n, "months.")
print("A year has", sum, "days.")
print("The average month has", average, "days.")

sys.exit(0)
