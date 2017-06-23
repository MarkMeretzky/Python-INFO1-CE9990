"""
ibm.py

Produce exit status 0 if the last price of IBM was >= 154,
exit status 1 if it was < 154.
Produce exit status 2 if we could not get the price.

To avoid the SSL: CERTIFICATE_VERIFY_FAILED error on macOS, run
Applications -> Python 3.6 -> Install Certificates.command
"""

import sys
import urllib.request

#For the l1 code, see http://www.jarloo.com/yahoo_finance/
url = "http://finance.yahoo.com/d/quotes.csv?s=IBM&f=l1"

try:
    u = urllib.request.urlopen(url)
except urllib.error.URLError:
    sys.exit(2)

line = u.readline()
u.close()
#print(line)

try:
    price = float(line)
except ValueError:
    sys.exit(2)

if price >= 154:
    sys.exit(0)   #success
else:
    sys.exit(1)   #failure
