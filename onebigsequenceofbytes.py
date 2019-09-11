"""
onebigsequenceofbytes.py

Read an entire text file into one big sequence of bytes.
Convert the sequence of bytes to a string of characters, and print it.
"""

import sys
import urllib.request

url = "http://oit2.scps.nyu.edu/~meretzkm/python/string/romeo.txt"

try:
    fileObject = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(f"status = {fileObject.status}")
print(f"msg = {fileObject.msg}")
sequenceOfBytes = fileObject.read()
fileObject.close()

try:
    s = sequenceOfBytes.decode("utf-8") #Convert sequence of bytes to string of characters.
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(s, end = "")
sys.exit(0)
