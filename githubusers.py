"""
githubusers.py

Print the GitHub loginname of each person who owns an organization whose name includes
SF19PB1-
starting with the most recently modified repository.
"""

import sys
import json
import urllib.parse
import urllib.request

query = {
    "q":    "SF19PB1-",
    "type": "organizations"
}

params = urllib.parse.urlencode(query)
url = f"https://api.github.com/search/users?{params}"

headers = {    #a dictionary
    "Accept": "application/vnd.github.preview+json"
}
request = urllib.request.Request(url, headers = headers)

try:
    infile = urllib.request.urlopen(request)
except urllib.error.URLError as error:
    print(error)
    sys.exit(1, file = sys.stderr)

sequenceOfBytes = infile.read()
infile.close()

try:
    s = sequenceOfBytes.decode("utf-8")
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

try:
    dictionary = json.loads(s)
except json.JSONDecodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

items = dictionary["items"]       #items is a list
print(f"""\
dictionary["incomplete_results"] = {dictionary["incomplete_results"]}
dictionary["total_count"] = {dictionary["total_count"]}
type(dictionary["items"]) = {type(items)}
len(dictionary["items"]) = {len(items)}
""")

items.sort(key = lambda item: item["html_url"])   #alphabetical order

for i, item in enumerate(items, start = 1): #i is an int, item is a dictionary
    print(i, item["html_url"])
    
sys.exit(0)
