"""
ibm.py

Produce exit status 0 if the last price of IBM was >= 168.00,
exit status 1 if it was < 168.00.
Produce exit status 2 if we could not get the price.

To avoid the SSL: CERTIFICATE_VERIFY_FAILED error on macOS, run
Applications -> Python 3.7 -> Install Certificates.command
"""

import sys
import urllib.request
import re   #regular expression

url = "https://finance.yahoo.com/quote/IBM"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(2)

sequenceOfBytes = infile.read()  #Read the entire file into a sequence of bytes.
infile.close()

#Convert the sequence of bytes into a string of characters.
#The string may contain more than one line of text, so we need re.DOTALL.
try:
    s = sequenceOfBytes.decode("utf-8")
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(2)

#The stock price is the only 36-point text in this web page.
if not "Fz(36px)" in s:
    sys.exit(2)

#Remove the "Fz(36px)" and everything before it.
s = re.sub(r".*Fz\(36px\)", "", s, count = 1, flags = re.DOTALL)

#Remove the rest of the tag that contained the "Fz(36px)".
s = re.sub(r"[^>]*>", "", s, count = 1)

#Remove everything after the price.
s = re.sub(r"<.*", "", s, count = 1, flags = re.DOTALL)

try:
    price = float(s)
except ValueError:
    sys.exit(2)

#Uncomment this line to print the price with 2 digits to right of decimal point.
#The first "f" stands for "formatted string"; the second "f" for "float".
#print(f"{price:.2f}")

if price >= 168.00:
    sys.exit(0)   #success
else:
    sys.exit(1)   #failure
