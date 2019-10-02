"""
toroman1.py

Convert an integer to a Roman numeral.
"""

import sys

thousands = ["", "M", "MM", "MMM", "MMMM"]
hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

def toRoman(n):
    "Convert one integer to a Roman numeral."
    assert isinstance(n, int) and 1 <= n <= 4999
    
    d = f"{n:04}"    #d is a string of 4 digits.
    
    i = int(d[0])    #d[0] is the leftmost digit.
    s = thousands[i]
    
    i = int(d[1])    #d[1] is the next-to-leftmost digit.
    s += hundreds[i] #or s = s + hundreds[i]
    
    i = int(d[2])    #d[2] is the third-from-leftmost digit.
    s += tens[i]
    
    i = int(d[3])    #d[3] is the fourth-from-leftmost digit.
    s += ones[i]

    return s

while True:
    while True:
        try:
            s = input("Please type an int in the range 1 to 4999 inclusive, or return to stop: ")
        except EOFError:
            sys.exit(0)
            
        if not s:   #The user pressed return without typing anything.
            sys.exit(0)
            
        try:
            n = int(s)
        except ValueError:
            print(f'Sorry, "{s}" is not an integer.')
            sys.exit(1)
        
        if 1 <= n <= 4999:
            break
        print(f"Sorry, {n} is out of range.")

    romanNumeral = toRoman(n)
    print(f"{n} = {romanNumeral}")
    print()
