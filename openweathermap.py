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
    print(error, file = sys.stderr)
    sys.exit(1)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(s)
print()

try:
    bigDictionary = json.loads(s)          #bigDictionary is a dict
except json.JSONDecodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(bigDictionary)
print()

#json.dumps ("dump string") returns a pretty (i.e., nicely indented) string.
try:
    s = json.dumps(bigDictionary, indent = 4, sort_keys = True)
except TypeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(s)
print()

try:
    main = bigDictionary["main"]            #main is a dict
except TypeError:
    print("bigDictionary is not a dictionary", file = sys.stderr)
    sys.exit(1)
except KeyError:
    print("bigDictionary has no key named main", file = sys.stderr)
    sys.exit(1)

try:
    temp = main["temp"]                     #temp is a float
except TypeError:
    print("main is not a dictionary", file = sys.stderr)
    sys.exit(1)
except KeyError:
    print("main has no key named temp", file = sys.stderr)
    sys.exit(1)

print(f"temperature = {temp}° Fahrenheit")

#Throw caution to the wind.
print(f'temperature = {bigDictionary["main"]["temp"]}° Fahrenheit')  #bigDictionary["main"] is a dict
print(f'description = {bigDictionary["weather"][0]["description"]}') #bigDictionary["weather"] is a list
sys.exit(0)
