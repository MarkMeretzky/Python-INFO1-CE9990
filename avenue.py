"""
tkavenue.py

Find the closest street to any address on a Manhattan avenue.
"""

import sys
import tkinter

#Each avenue has a list of one or more rules.  The last rule in an avenue's list
#must have a building number of m, which is an integer bigger than any possible
#building number.
m = sys.maxsize

avenues = [
    ["Broadway", [
        [754, 10, -38], #special case: negative street number if below 8th St.
        [858, 20, -29],
        [953, 20, -25],
        [m,   20, -31]
    ]],
    ["First Avenue",        [[m, 20,   3]]],
    ["Second Avenue",       [[m, 20,   3]]],
    ["Third Avenue",        [[m, 20,  10]]],
    ["Fourth Avenue",       [[m, 20,   8]]],
    ["Fifth Avenue",  [
        [ 108, 20,  11],
        [ 199, 20,  13],
        [ 399, 20,  16],
        [ 599, 20,  18],
        [ 774, 20,  20],
        [1286, 10, -18],   #110th Street
        [1499, 20,  45],
        [   m, 20,  24]
    ]],
    ["Sixth Avenue",        [[m, 20,  -12]]],
    ["Seventh Avenue", [
        [1800, 20, 12],
        [m,    20, 20]
    ]],
    ["Eighth Avenue",       [[m, 20,   9]]],
    ["Ninth Avenue",        [[m, 20,  13]]],
    ["Tenth Avenue",        [[m, 20,  13]]],
    ["Eleventh Avenue",     [[m, 20,  15]]],
    ["Amsterdam Avenue",    [[m, 20,  59]]],
    ["Central Park West",   [[m, 10,  60]]],
    ["Columbus Avenue",     [[m, 20,  59]]],
    ["Convent Avenue",      [[m, 20, 127]]],
    ["Edgecombe Avenue",    [[m, 20, 134]]],
    ["Lenox Avenue",        [[m, 20, 110]]],
    ["Lexington Avenue",    [[m, 20,  22]]],
    ["Madison Avenue",      [[m, 20,  27]]],
    ["Park Avenue",         [[m, 20,  34]]],
    ["Park Avenue South",   [[m, 20,   8]]],
    ["Riverside Drive", [
        [567, 10, 73],
        [m,   10, 78]
    ]],
    ["St. Nicholas Avenue", [[m, 20, 110]]],
    ["Vanderbilt Avenue",   [[m, 20,  42]]],
    ["West End Avenue",     [[m, 20,  59]]],
    ["York Avenue",         [[m, 20,   4]]]
]

n = len(avenues)


def findStreet(buildingNumber, avenueNumber):
    """
    Return the street closest to the given building number and avenue,
    or None if not found.
    """
    assert isinstance(buildingNumber, int) and isinstance(avenueNumber, int)
    #avenues[avenueNumber] is a list of two items: a name and a list of rules.
    #avenues[avenueNumber][0] is the name.
    #avenues[avenueNumber][1] is the list of rules.

    for rule in avenues[avenueNumber][1]:
        if buildingNumber <= rule[0]:
            return buildingNumber // rule[1] + rule[2]


def ordinal(i):
    "Return the ordinal form of a positive integer."
    assert isinstance(i, int) and i > 0
    
    lastDigit = i % 10
    last2Digits = i % 100
    s = str(i)

    if 11 <= last2Digits and last2Digits <= 13:
        s += "th"
    elif lastDigit == 1:
        s += "st"
    elif lastDigit == 2:
        s += "nd"
    elif lastDigit == 3:
        s += "rd"
    else:
        s += "th"

    return s


while True:
    try:
        s = input("Please type the building number: ")
    except EOFError:
        sys.exit(0)

    try:
        buildingNumber = int(s)
    except ValueError:
        print(f'Sorry, "{s}" is not an integer.')
        print()
        continue

    if buildingNumber <= 0:
        print("Sorry, building number must be positive.")
        print()
        continue

    print()
    for i, avenue in enumerate(avenues):
        print(f"{i:2} {avenue[0]}")
    print()

    try:
        s = input("Please type the avenue number: ")
    except EOFError:
        sys.exit(0)

    try:
        avenueNumber = int(s)
    except ValueError:
        print(f'Sorry, "{s}" is not an integer.')
        print()
        continue

    if avenueNumber < 0 or avenueNumber >= n:
        print(f"Sorry, {avenueNumber} is out of range.")
        print()
        continue

    street = findStreet(buildingNumber, avenueNumber)
    s = f"{buildingNumber} {avenues[avenueNumber][0]} is "

    if street == None:
        s += "not found"
    elif street < 0:
        s += "below 8th Street"  #special case: only on Broadway
    else:
        s += f"at {ordinal(street)} Street"

    print(f"{s}.")
    print()
