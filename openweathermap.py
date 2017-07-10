"""
openweathermap.py

Download the current weather for zipcode 10036.
10036 is the zipcode of 11 West 42nd Street.
"imperial" means fahrenheit, not celsius.
mode can be json, xml, or html.
See
https://openweathermap.org/current
"""

import sys
import urllib.request
import json

url = "http://api.openweathermap.org/data/2.5/weather" \
    "?q=10036,US" \
    "&units=imperial" \
    "&mode=json" \
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

try:
    dictionary = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)

print(dictionary)
print()

#json.dumps ("dump string") returns a pretty (i.e., nicely indented) string.
try:
    print(json.dumps(dictionary, indent = 4, sort_keys = True))
except TypeError as typeError:
    print(typeError)
    sys.exit(1)
print()

main = dictionary["main"]               #main is a dictionary
temp = main["temp"]                     #temp is a float
print("temperature = {}° Fahrenheit".format(temp))

print("temperature = {}° Fahrenheit".format(dictionary["main"]["temp"]))
sys.exit(0)
