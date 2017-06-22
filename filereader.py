"""
filereader.py

Read and print a text file, line by line.
"""

import sys

#macOS
filename = "/Library/Frameworks/Python.framework/Versions/3.6/share/doc/python3.6/examples/Tools/demo/beer.py"

#Microsoft Windows
#filename = "C:\\Users\Myname\\AppData\\Local\\Programs\\Python\\Python36-32\\Tools\\demo\\beer.py"

try:
    inputfile = open(filename)
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

for line in inputfile:
    print(line, end = "")

inputfile.close()
sys.exit(0)
