"""
sparse2.py

Use a dictionary instead of a sparse list.
"""

import sys

buildings = {
     14: "The Con Ed Building",
     23: "The Met Life Tower",
     34: "The Empire State Building",
     42: "Grand Central Terminal",
     49: "The RCA Building",
     59: "The Plaza",
     72: "The Dakota",
     82: "The Met",
     88: "The Guggenheim",
    100: "Mount Sinai"
}

while True:
    try:
        st = int(input("Please type a street number (e.g., 42): "))
    except:  #if user did not type a valid int
        sys.exit(0)

    try:
        b = buildings[st]
    except KeyError:
        b = "Nothing famous"

    print(f"{b} is on that street.")
    print()
