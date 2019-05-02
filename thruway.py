"""
thruway.py

Print the signs going north from New York City on the New York State Thruway.
The string consists of six lines of text.  The last line is empty.
"""

import sys

for a in range(108, 38, -10):
    print(f"""\
+--------------+
| Albany   {a:3} |
| Montreal {a + 220:3} |
| Buffalo  {a + 280:3} |
+--------------+
""")

sys.exit(0)
