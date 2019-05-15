"""
onebigstring.py

Read an entire text file into one big string, and print it.
"""

import sys

#macOS
filename = "/Library/Frameworks/Python.framework/Versions/3.7/share/doc/python3.7/examples/Tools/demo/beer.py"

#Microsoft Windows
#filename = "C:\\Users\\Myname\\AppData\\Local\\Programs\\Python\\Python37-32\\Tools\\demo\\beer.py"

try:
    fileObject = open(filename)
except FileNotFoundError:
    print(f"Sorry, could not find file \"{filename}\".")
    sys.exit(1)
except PermissionError:
    print(f"Sorry, no permission to open file \"{filename}\".")
    sys.exit(1)

oneBigString = fileObject.read()   #Read the entire file.
fileObject.close()
print(oneBigString)
sys.exit(0)