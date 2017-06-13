"""
fontsize.py

Output an HTML stylesheet showing different font sizes.
"""

import sys

print("<HTML>")
print("<BODY>")
print("<H1>Stylesheet</H1>")
print()

points = 1

while points < 13:
    print("<P STYLE = \"font-size: ", points, "pt;\">", sep = "")
    print(points, "point")
    print("<BR>")
    print("Pack my box with five dozen liquor jugs.")
    print("</P>")
    print()
    points += 1

print("</BODY>")
print("</HTML>")
sys.exit(0)
