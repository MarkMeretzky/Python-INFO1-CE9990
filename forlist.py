"""
forlist.py

Loop through the items in a list.
"""

import sys

animals = [
    "monkey",  # 0
    "rooster", # 1
    "dog",     # 2
    "pig",     # 3
    "rat",     # 4
    "ox",      # 5
    "tiger",   # 6
    "hare",    # 7
    "dragon",  # 8
    "snake",   # 9
    "horse",   #10
    "sheep"    #11
]
n = len(animals)

i = 0
while i < n:
    print(animals[i])
    i += 1

print()   #Skip a line.

for i in range(0, n, 1):  #for i in range(n): would do the same thing
    print(animals[i])
    
print()   #Skip a line.

for animal in animals:
    print(animal)

sys.exit(0)
