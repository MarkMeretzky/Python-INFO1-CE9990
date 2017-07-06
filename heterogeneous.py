"""
heterogeneous.py
 
This program demonstrates a list whose four items
are of four different data types.
"""

import sys

movie = ["Dr. No", 1962, 59_500_000.00, ["Sean Connery", "Ursula Andress", "Joseph Wiseman", "Jack Lord"]]

print("Name:", movie[0])                          #movie[0] is a string.
print("Year:", movie[1])                          #movie[1] is an int.
print("Box office:", "${:,.2f}".format(movie[2])) #movie[2] is a float.
print("Starring: ", end = "")                     #movie[3] is a list of strings.

stars = movie[3]

for i, star in enumerate(stars):
    if i == len(stars) - 1:
        print(star)             #the last star
    else:
        print(star, end = ", ") #the other stars

sys.exit(0)
