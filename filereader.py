"""
filereader.py

Read and print a text file, line by line.
"""

import sys

#macOS
filename = "/Library/Frameworks/Python.framework/Versions/3.7/share/doc/python3.7/examples/Tools/demo/beer.py"

#Microsoft Windows
#filename = "C:\\Users\\Myname\\AppData\\Local\\Programs\\Python\\Python37-32\\Tools\\demo\\beer.py"

try:
    lines = open(filename) #lines is something you can loop through with a for loop
except FileNotFoundError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
except PermissionError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

for line in lines:
    print(line, end = "")   #The line already ends with a newline.  Don't need another newline.

lines.close()
sys.exit(0)
