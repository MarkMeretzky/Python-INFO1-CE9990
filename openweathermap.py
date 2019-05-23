"""
openweathermap.py

Download the current weather for zipcode 10004.
10004 is the zipcode of 25 Broadway.
"imperial" means fahrenheit, not celsius.
mode can be json, xml, or html.
See
https://openweathermap.org/current
"""

import sys
import urllib.request
import json

url = "http://api.openweathermap.org/data/2.5/weather" \
    "?q=10004,US" \
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
    print("UnicodeError", unicodeError)
    sys.exit(1)

print(s)
print()

try:
    dictionary = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print("json.JSONDecodeError", jSONDecodeError)
    sys.exit(1)

print(dictionary)
print()

#json.dumps ("dump string") returns a pretty (i.e., nicely indented) string.
try:
    print(json.dumps(dictionary, indent = 4, sort_keys = True))
except TypeError as typeError:
    print("TypeError", typeError)
    sys.exit(1)
print()

try:
    main = dictionary["main"]               #main is a dictionary
except TypeError:
    print("dictionary is not a dictionary")
    sys.exit(1)
except KeyError:
    print("dictionary has no key named main")
    sys.exit(1)

try:
    temp = main["temp"]                     #temp is a float
except TypeError:
    print("main is not a dictionary")
    sys.exit(1)
except KeyError:
    print("main has no key named temp")
    sys.exit(1)

print(f"temperature = {temp}° Fahrenheit")

#Throw caution to the winds.
print(f'temperature = {dictionary["main"]["temp"]}° Fahrenheit')
sys.exit(0)
