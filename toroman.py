"""
toroman1.py

Convert an integer to a Roman numeral.
"""

import sys

ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands = ["", "M", "MM", "MMM", "MMMM"]

def toRoman(n):
    "Convert one integer to a Roman numeral."
    assert isinstance(n, int) and 1 <= n and n <= 4999
    
    d = f"{n:04}"   #d is a string of 4 digits
    
    i = int(d[-1])  #the rightmost digit
    s = ones[i]
    
    i = int(d[-2])  #the next-to-rightmost digit
    s = tens[i] + s
    
    i = int(d[-3])
    s = hundreds[i] + s
    
    i = int(d[-4])
    s = thousands[i] + s

    return s

while True:
    while True:
        try:
            s = input("Please type an int in the range 1 to 4999 inclusive, or return to stop: ")
        except EOFError:
            sys.exit(0)
            
        try:
            n = int(s)
        except ValueError:
            print(f'Sorry, "{s}" is not an integer.')
            sys.exit(1)
        
        n = getInt("")
        if 1 <= n <= 4999:
            break
        print(f"Sorry, {n} is out of range.")

    romanNumeral = toRoman(n)
    print(f"{n} = {romanNumeral}")
    print()
