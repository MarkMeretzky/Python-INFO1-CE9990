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

print(f"""\
Name: {movie[0]}                          
Year: {movie[1]}                         
Box office: ${movie[2]:,.2f} 
Starring: """,
    end = "")                     

stars = movie[3]

for star in stars[:-1]:   #all but the last star
    print(star, end = ", ")
  
print(stars[-1])          #the last star
sys.exit(0)
