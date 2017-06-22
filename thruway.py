"""
thruway.py

Print the signs going north from New York City on the New York State Thruway. 
"""

import sys

#This format string consists of six lines of text.
#The sixth line is empty (i.e., consists of one newline character).

f = """\
+--------------+
| Albany   {:3} |
| Montreal {:3} |
| Buffalo  {:3} |
+--------------+
\
"""

a = 98   #miles to Albany

while a >= 38:
    print(f.format(a, a + 300, a + 360))
    a -= 10   #means a = a - 10

sys.exit(0)
