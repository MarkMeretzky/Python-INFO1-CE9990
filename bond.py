"""
bond.py

Read a text input file into a list.
Each line in the file will be a separate list item.
"""

import sys

if sys.platform.startswith("darwin"):    #macOS Sierra 10.12.5
    filename = "/Users/myname/Desktop/bond.txt"
elif sys.platform.startswith("win32"):   #Microsoft Windows 7 Home Premium
    filename = "C:\\Users\\Myname\\Desktop\\bond.txt"
else:
    print("Unknown platform", sys.platform)
    sys.exit(1)

try:
    infile = open(filename)
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

lines = infile.readlines() #lines is a list of strings
infile.close()

for line in lines:
    print(line, end = "")  #end="" because each line already ends with a newline

print()
lines.sort()               #into alphabetical order

for line in lines:
    print(line, end = "")

sys.exit(0)
