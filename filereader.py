"""
filereader.py

Read and print a text file, line by line.
"""

import sys

#macOS
filename = "/Library/Frameworks/Python.framework/Versions/3.8/share/doc/python3.8/examples/Tools/demo/README"

#Microsoft Windows
#filename = r"C:\Users\Myname\AppData\Local\Programs\Python\Python37-32\Tools\demo\README"

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
