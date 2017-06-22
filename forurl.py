"""
forurl.py

Download the current weather for zipcode 10036.
imperial means fahrenheit, not celsius.
mode can be json, xml, or html.
See
https://openweathermap.org/current
"""

import sys
import urllib.request

url = "http://api.openweathermap.org/data/2.5/weather" \
    "?q=10036,US" \
    "&units=imperial" \
    "&mode=json" \
    "&APPID=532d313d6a9ec4ea93eb89696983e369"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

for line in lines:
    print(line)
    
lines.close()
sys.exit(0)
