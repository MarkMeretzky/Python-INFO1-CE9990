"""
bond.py

Read a text input file into a list.
Each line in the file will be a separate list item.
"""

import sys

if sys.platform.startswith("darwin"):    #macOS Mojave 10.14.6
    filename = "/Users/myname/Desktop/bond.txt"
elif sys.platform.startswith("win32"):   #Microsoft Windows 7 Home Premium
    filename = r"C:\Users\Myname\Desktop\bond.txt"
else:
    print(f"Unknown platform {sys.platform}")
    sys.exit(1)

try:
    infile = open(filename)
except FileNotFoundError:
    print(f'Sorry, could not find file "{filename}".')
    sys.exit(1)
except PermissionError:
    print(f'Sorry, no permission to open file "{filename}".')
    sys.exit(1)

lines = infile.readlines()   #lines is a list of strings
infile.close()

sortedLines = sorted(lines, key = lambda line: line[5:]) #alphabetical order by movie name

for line, sortedLine in zip(lines, sortedLines):
    print(f"{line:36} {sortedLine}")

sys.exit(0)
