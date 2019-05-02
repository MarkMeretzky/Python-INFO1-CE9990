"""
list3.py

Demonstrate a list of strings.
"""

import sys

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

n = len(months)

print(f"A year has {n} months.")
print(f"{months[0]} is the first month.")
print(f"{months[1]} is the second month.")
print(f"{months[2]} is the third month.")
print(f"{months[3]} is the cruelest month.")
print(f"{months[11]} is the twelfth month.")

print(f"{months[-1]} is the last month.")
print(f"{months[-2]} is the next-to-last month.")
print(f"{months[-3]} is the third-to-last month.")

sys.exit(0)
