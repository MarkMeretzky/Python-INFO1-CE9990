"""
tkavenue.py

Add a tkinter GUI to the Manhattan address algorithm.
"""

import sys
import tkinter

#Each avenue has a list of one or more rules.  The last rule in an avenue's list must have a building number of m, which is 
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

    
def buttonPress():   #Called when the button is pressed.
    """
    Get the building number and avenue number,
    and display the corresponding street in the Text widget.
    """
    #Delete everything from the start of the Text ("1.0")
    #to the end of the Text (tkinter.END).
    answerText.delete("1.0", tkinter.END)

    try:
        #numberEntry.get() is the string typed into the Entry.
        buildingNumber = int(numberEntry.get())
    except ValueError:
        answerText.insert("1.0", numberEntry.get() + " is not an integer")
        return

    if buildingNumber <= 0:
        answerText.insert("1.0", "Building number must be positive.")
        return
    
    try:
        #avenueName.get() is the string selected from the OptionsMenu.
        avenueNumber = avenueNames.index(avenueName.get())
    except ValueError:
        answerText.insert("1.0", "Couldn't find " + avenueName.get())
        return

    street = findStreet(buildingNumber, avenueNumber)
    s = str(buildingNumber) + " " + avenueName.get() + " is "

    if street == None:
        s += "not found"
    elif street < 0:
        s += "below 8th Street"  #special case: only on Broadway
    else:
        s += "at " + ordinal(street) + " Street"

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
avenueNames = []   #Start with an empty list.
for avenue in avenues:
    #avenue is a list of two items: a name and a list of rules.
    #avenue[0] is the name.
    #avenue[1] is the list of rules.
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
