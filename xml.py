"""
xml.py

Download the current weather from OpenWeatherMap in XML format.
"""

import sys
import urllib.parse
import urllib.request
import lxml.etree

query = {                              #query is a dictionary
    "q":     "10004,US",
    "units": "imperial",
    "mode":  "xml",
    "APPID": "532d313d6a9ec4ea93eb89696983e369"
}

params = urllib.parse.urlencode(query) #params is a string
url = f"http://api.openweathermap.org/data/2.5/weather?{params}"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as error:
    print(unicodeError, file = sys.stderr)
    sys.exit(1)

print(s)
print()

#Create an XML tree and pretty print it.
try:
    root = lxml.etree.fromstring(sequenceOfBytes)
except lxml.etree.XMLSyntaxError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

prettySequenceOfBytes = lxml.etree.tostring(root, pretty_print = True)

try:
    prettyS = prettySequenceOfBytes.decode("utf-8")   #prettyS is a string.
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
    
print(prettyS)
print()

#Print the current temperature.

temperature = root.find("temperature")
if temperature == None:
    print("Couldn't find temperature.", file = sys.stderr)
    sys.exit(1)

value = temperature.get("value")
if value == None:
    print("Couldn't find value of temperature.", file = sys.stderr)
    sys.exit(1)

unit = temperature.get("unit")
if unit == None:
    print("Couldn't find unit of temperature.", file = sys.stderr)
    sys.exit(1)

print(f"The temperature is {value}° {unit}.")
sys.exit(0)
