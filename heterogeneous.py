"""
heterogeneous.py
 
This program demonstrates a list whose four items
are of four different data types.
"""

import sys

#movie[0] is a string.
#movie[1] is an int.
#movie[2] is a float.
#movie[3] is a list of strings.

movie = ["Dr. No", 1962, 59_500_000.00, ["Sean Connery", "Ursula Andress", "Joseph Wiseman", "Jack Lord"]]


print("""\
Name: {movie[0]}                          
Year: {movie[1]}                         
Box office: ${movie[2]:,.2f} 
Starring: """,
    end = "")                     

stars = movie[3]

for i, star in enumerate(stars):
    if i == len(stars) - 1:
        print(star)                  #the last star
    else:
        print(f"{star}, ", end = "") #the other stars

sys.exit(0)
