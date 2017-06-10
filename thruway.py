"""
thruway.py

Print the signs you see as you drive north on the New York State Thruway. 
"""

import sys

a = 98

#This is a format string.
f = """\
+--------------+
| Albany   {:3} |
| Montreal {:3} |
| Buffalo  {:3} |
+--------------+
\
"""

while a >= 38:
    print(f.format(a, a + 300, a + 360))
    a = a - 10   #or a -= 10

sys.exit(0)
