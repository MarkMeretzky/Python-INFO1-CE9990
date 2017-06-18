"""
list1.py

Demonstrate how they programmed before they invented lists.
"""

import sys

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

n = 12   #have to count them yourself

sum = january + february + march + april + may + june + july \
    + august + september + october + november + december

average = sum / n

print("A year has", n, "months.")
print("A year has", sum, "days.")
print("The average month has", average, "days.")

sys.exit(0)
