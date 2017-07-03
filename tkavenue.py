"""
tkavenue.py

Input a binary file.  Since the file is not a text file, we cannot say
for line in lines:
"""

import sys
import tkinter

m = sys.maxsize   #an integer that's bigger than any possible building number

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


def findStreet(building, a):
    "Return the street closest to the given building number and avenue."
    assert isinstance(building, int) and isinstance(a, int)
    avenue = avenues[a]
    #avenue[0] is the name of the avenue, avenue[1] is a list of rules.

    for rule in avenue[1]:
        if building <= rule[0]:
            street = building // rule[1] + rule[2]
            return street


def ordinal(i):
    "Return the ordinal form of the positive integer."
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

    
def buttonPress():
    """
    Get the building number and avenue, and display the corresponding street
    in the Text widget.
    """
    try:
        a = avenueNames.index(avenueName.get())
    except ValueError as valueError:
        print(valueError)
        sys.exit(1)

    try:
        building = int(numberEntry.get())
    except ValueType as valueError:
        print(valueError)
        sys.exit(1)
    
    street = findStreet(building, a)
 
    s = str(building) + " " + avenueName.get() + " is "
    if street < 0:
        s += "below 8th Street"
    else:
        s += "at " + ordinal(street) + " Street"

    answerText.delete("1.0", tkinter.END)
    answerText.insert("1.0", s + ".")


root = tkinter.Tk()
root.title("Manhattan Avenues")
root.geometry("330x80")

#root contains a grid of 3 rows and 3 columns.

numberLabel = tkinter.Label(root, text = "Building number", width = 15)
numberLabel.grid(row = 0, column = 0)

avenueLabel = tkinter.Label(root, text = "Avenue", width = 15)
avenueLabel.grid(row = 0, column = 1)

numberEntry = tkinter.Entry(root, width = 8)
numberEntry.grid(row = 1, column = 0)

#Make a list of the names of the avenues.
avenueNames = []
for avenue in avenues:
    avenueNames.append(avenue[0])

avenueName = tkinter.StringVar(root)   #Avenue the user selects from the menu
avenueName.set(avenues[0][0])          #Menu displays this default choice.
avenueMenu = tkinter.OptionMenu(root, avenueName, *avenueNames)
avenueMenu.grid(row = 1, column = 1)

button = tkinter.Button(root, text = "Go", command = buttonPress)
button.grid(row = 1, column = 2)

answerText = tkinter.Text(root, width = 45,
    height = 1, borderwidth = 2, relief = "groove")
answerText.grid(row = 2, column = 0, columnspan = 3)

root.mainloop()
