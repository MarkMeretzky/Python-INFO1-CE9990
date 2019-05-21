"""
githubusers.py

Print the GitHub loginname of each person who owns a repository named
Python-INFO1-CE9990
starting with the most recently modified repository.
"""

import sys
import json
import urllib.request

url = (
    "https://api.github.com/search/users"
    "?utf8=%E2%9C%93"
    "&q=WS19PB02-"
    "&type=organizations"
)

headers = {    #a dictionary
    "Accept": "application/vnd.github.preview+json"
}
request = urllib.request.Request(url, headers = headers)

try:
    infile = urllib.request.urlopen(request)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = infile.read()
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8")
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

try:
    dictionary = json.loads(s)
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)

items = dictionary["items"]       #items is a list
print(f"""\
dictionary["incomplete_results"] = {dictionary["incomplete_results"]}
dictionary["total_count"] = {dictionary["total_count"]}
type(dictionary["items"]) = {type(items)}
len(dictionary["items"]) = {len(items)}
""")

items.sort(key = lambda item: item["html_url"])   #alphabetical order

for i, item in enumerate(items, start = 1): #i is an int, items is a dictionary
    print(i, item["html_url"])
    
sys.exit(0)
