"""
avenue.py

Find the closest street to any address on a Manhattan avenue.
"""

import sys
m = sys.maxsize   #an integer that's bigger than any possible building number

#List of avenues.  Each avenue is a list consisting of the avenue's name
#followed by a list of one or more rules.  (Most avenues have a list consisting
#of just a single rule.)  Each rule is a list consisting of the maximum building
#number to which the rule applies, followed by a divisor and addend.  The rules
#are tried in the order in which they are listed.  The last rule of an avenue
#must have an m.

avenues = [
    ["Broadway", [
        [754, 10, -38], #1 special case: negative street number if below 8th St.
        [858, 20, -29],
        [953, 20, -25],
        [m,   20, -31]
    ]],
    ["First Avenue",        [[m, 20,   3]]],
    ["Second Avenue",       [[m, 20,   3]]],
    ["Third Avenue",        [[m, 20,  10]]],
    ["Fourth Avenue",       [[m, 20,   8]]],
    ["Fifth Avenue",  [
        [ 200, 20,  13],
        [ 400, 20,  16],
        [ 600, 20,  18],
        [ 775, 20,  20],
        [1286, 10, -18],
        [1500, 20,  45],
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

while True:
    try:
        building = input("Please type the building number: ")
    except EOFError:
        sys.exit(0)

    try:
        building = int(building)
    except ValueError:
        print("Sorry,", building, "is not an integer.")
        continue

    print()
    for i, avenue in enumerate(avenues):
        print("{:2} {}".format(i, avenue[0]))
    print()

    try:
        i = input("Please type the avenue number: ")
    except EOFError:
        sys.exit(0)

    try:
        i = int(i)
    except ValueError:
        print("Sorry,", i, "is not an integer.")
        continue

    avenue = avenues[i]
    #avenue[0] is the name of the avenue, avenue[1] is a list of rules.

    for rule in avenue[1]:
        if building <= rule[0]:
            street = building // rule[1] + rule[2]
            break

    #Special case: Broadway numbers <= 754 are below 8th Street.
    if street < 0:
        print(building, avenue[0], "is below 8th Street.")
        continue

    print(building, avenue[0], "is at", street, end = "")
    last2digits = street % 100
    lastDigit = street % 10

    if 11 <= last2digits and last2digits <= 13:
        print("th", end = "")
    elif lastDigit == 1:
        print("st", end = "")
    elif lastDigit == 2:
        print("nd", end = "")
    elif lastDigit == 3:
        print("rd", end = "")
    else:
        print("th", end = "")

    print(" Street.")
    print()
