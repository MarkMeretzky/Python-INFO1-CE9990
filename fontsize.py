"""
fontsize.py

Output an HTML stylesheet showing different font sizes.
"""

import sys

print("""\
<HTML>
<BODY>
<H1>Stylesheet</H1>
""")

for points in range(1, 13):
    print(f'''\
<P STYLE = "font-size: {points}pt;">
{points} point
<BR>
Pack my box with five dozen liquor jugs.
</P>
''')

print("""\
</BODY>
</HTML>
""")

sys.exit(0)
