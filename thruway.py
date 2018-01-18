"""
thruway.py

Print the signs going north from New York City on the New York State Thruway. 
"""

import sys

#This format string consists of five lines of text.

f = """\
+--------------+
| Albany   {:3} |
| Montreal {:3} |
| Buffalo  {:3} |
+--------------+
"""

a = 108   #miles to Albany

while a >= 48:
    print(f.format(a, a + 220, a + 280))
    a -= 10   #means a = a - 10

sys.exit(0)
