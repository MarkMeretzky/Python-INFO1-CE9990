"""
minidom.py

Download the current weather from OpenWeatherMap in XML format,
without using third-party software.
"""

import sys
import urllib.request
import xml.etree.ElementTree
import xml.dom.minidom

url = "http://api.openweathermap.org/data/2.5/weather" \
    "?q=10036,US" \
    "&units=imperial" \
    "&mode=xml" \
    "&APPID=532d313d6a9ec4ea93eb89696983e369"

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
    print(unicodeError)
    sys.exit(1)

print(s)
print()

#Pretty print the XML.
document = xml.dom.minidom.parseString(sequenceOfBytes)
prettyS = document.toprettyxml(indent = "\t")   #prettyS is a string.
print(prettyS)
print()

#Print the current temperature.
root = xml.etree.ElementTree.fromstring(s)
temperature = root.find("temperature")
value = temperature.get("value")
unit = temperature.get("unit")
print("The temperature is {}° {}.".format(value, unit))
sys.exit(0)
