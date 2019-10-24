"""
person.py

Put some attributes into an initially empty object.
"""

import sys

class Person(object):   #The (object) is unnecessary: you get it anyway.
    pass


def myFunc(person):
    "Change some of the person's attributes."
    assert isinstance(person, Person)

    #If person has a hair color, overwrite it.  Otherwise, create it.
    person.hair = "black"

    #If person has an age, delete it.
    try:
        del person.age
    except AttributeError:  #Arrive here if person had no age.
        pass                #If person had no age, do nothing.

    try:
        favoriteSongs = person.favoriteSongs
    except AttributeError:
        person.favoriteSongs = [] #Arrive here if person has no favorite songs.
    person.favoriteSongs.append("Revolution")


mark = Person()
mark.lastName = "Meretzky"
mark.age = 64
mark.favoriteSongs = ["Help!", "Day Tripper", "Piggies"]

print("Before:")
for key, value in mark.__dict__.items():
    print(key, value)

myFunc(mark)
print()

print("After:")
for key, value in mark.__dict__.items():
    print(key, value)
        
sys.exit(0)
