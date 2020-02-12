"""
onebigstring.py

Read an entire text file into one big string, and print it.
"""

import sys

#macOS
filename = "/Library/Frameworks/Python.framework/Versions/3.7/share/doc/python3.7/examples/Tools/demo/README"

#Microsoft Windows
#filename = r"C:\Users\Myname\AppData\Local\Programs\Python\Python37-32\Tools\demo\README"

try:
    fileObject = open(filename)
except FileNotFoundError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
except PermissionError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

oneBigString = fileObject.read()   #Read the entire file.
fileObject.close()
print(oneBigString, end = "") #Every line in the file already ends with a newline.
sys.exit(0)
