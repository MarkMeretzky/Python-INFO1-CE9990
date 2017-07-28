"""
attributes.py

Put some attributes into an initially empty object.
"""

import sys

class tabulaRasa:
    pass


def myFunc(person):
    "Change some of the person's attributes."
    assert isinstance(person, tabulaRasa)

    if "age" in person.__dict__: #person.__dict__ is a dictionary.
        del person.age           #Delete an attribute if it's there.
    if not "hair" in person.__dict__:
        person.hair = "black"    #Add an attribute if not already there.
    return person


person = tabulaRasa()
person.name = "Joe"
person.age = 62
person.favoriteSongs = ["Help!", "Day Tripper", "Piggies"]

print("Before:")
for key, value in person.__dict__.items():
    print(key, value)

myFunc(person)
print()

print("After:")
for key, value in person.__dict__.items():
        print(key, value)
        
sys.exit(0)
