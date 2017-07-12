"""
githubusers.py

Print the GitHub loginname of each person who owns a repository named
Python-INFO1-CE9990
starting with the most recently modified repository.
"""

import sys
import json
import urllib.request

url = "https://api.github.com/search/repositories" \
    "?utf8=%E2%9C%93" \
    "&q=Python-INFO1-CE9990" \
    "&type=Repositories" \
    "&s=updated" \
    "&o=desc"

headers = {
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
items.sort(key = lambda item: item["pushed_at"], reverse = True)

for item in items:                #item is a dictionary
    print(item["owner"]["login"]) #item["owner"] is a dictionary
    
sys.exit(0)
