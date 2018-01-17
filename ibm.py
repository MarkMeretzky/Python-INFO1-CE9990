"""
ibm.py

Produce exit status 0 if the last price of IBM was >= 168.00,
exit status 1 if it was < 168.00.
Produce exit status 2 if we could not get the price.

To avoid the SSL: CERTIFICATE_VERIFY_FAILED error on macOS, run
Applications -> Python 3.6 -> Install Certificates.command
"""

import sys
import urllib.request
import re   #regular expression

url = "https://finance.yahoo.com/quote/IBM"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(2)

for line in lines:
    try:
        s = line.decode("utf-8") #Convert sequence of bytes to string of chars.
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(2)

    #The stock price is the only 36-point text in this page.
    if "Fz(36px)" in s:
        #Remove the "Fz(36px)" and everything before it.
        s = re.sub(r".*Fz\(36px\)", "", s, count = 1)

        #Remove the rest of the tag that contained the "Fz(36px)",
        #and the following tag.
        s = re.sub(r"^[^>]*><[^>]*>", "", s, count = 1)

        #Remove everything after the price.
        s = re.sub(r"<.*", "", s, count = 1)

        try:
            price = float(s)
        except ValueError:
            lines.close()
            sys.exit(2)
        break #out of the for loop

lines.close()

#Uncomment this line if you want to print the price.
#print(price)

if price >= 168.00:
    sys.exit(0)   #success
else:
    sys.exit(1)   #failure
