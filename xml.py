"""
xml.py

Download the current weather from OpenWeatherMap in XML format.
"""

import sys
import urllib.request
import lxml.etree

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

#Create an XML tree and pretty print it.
root = lxml.etree.fromstring(sequenceOfBytes)
prettySequenceOfBytes = lxml.etree.tostring(root, pretty_print = True)

try:
    prettyS = prettySequenceOfBytes.decode("utf-8")   #prettyS is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)
    
print(prettyS)
print()

#Print the current temperature.
temperature = root.find("temperature")
value = temperature.get("value")
unit = temperature.get("unit")
print("The temperature is {}° {}.".format(value, unit))
sys.exit(0)
