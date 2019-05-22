"""
elementtree.py

Download the current weather from OpenWeatherMap in XML format,
without using third-party software.
"""

import sys
import urllib.request
import xml.etree.ElementTree
import xml.dom.minidom

url = (
    "http://api.openweathermap.org/data/2.5/weather"
    "?q=10004,US"
    "&units=imperial"
    "&mode=xml"
    "&APPID=532d313d6a9ec4ea93eb89696983e369"
)

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as unicodeError:
    print("UnicodeError", unicodeError)
    sys.exit(1)

print(s)
print()

#Pretty print the XML.

try:
    document = xml.dom.minidom.parseString(s)
except xml.parsers.expat.ExpatError as error:
    print("xml.parsers.expat.ExpatError", error)
    sys.exit(1)

prettyS = document.toprettyxml(indent = "\t")   #prettyS is a string.
print(prettyS)
print()

#Print the current temperature.

try:
    root = xml.etree.ElementTree.fromstring(s)
except xml.etree.ElementTree.ParseError as error:
    print("xml.etree.ElementTree.ParseError", error)
    sys.exit(1)

temperature = root.find("temperature")
if temperature == None:
    print("Couldn't find temperature.")
    sys.exit(1)

value = temperature.get("value")
if value == None:
    print("Couldn't find value of temperature.")
    sys.exit(1)

unit = temperature.get("unit")
if unit == None:
    print("Couldn't find unit of temperature.")
    sys.exit(1)

print(f"The temperature is {value}° {unit}.")
sys.exit(0)
