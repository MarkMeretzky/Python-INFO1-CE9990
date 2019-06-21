#!/usr/bin/env python3
"""
This gateway is
/home/m/meretzkm/public_html/cgi-bin/pythoncal.cgi
It outputs a page of HTML containing a calendar and is executed from the form
/home/m/meretzkm/public_html/python/cgi/cgi.html
The URL of this form is
http://oit2.scps.nyu.edu/~meretzkm/python/cgi/cgi.html
"""

import sys
import os   #operating system

#os.environ is a dictionary.

print(f"""\
Content-type: text/html

<HTML>
<HEAD>
<TITLE>Calendar</TITLE>
</HEAD>

<BODY>
<H1>Calendar</H1>

<H2>{len(os.environ)} environment variables</H2>

<OL>""")

for key, value in sorted(os.environ.items()):
    print(f"<LI><CODE>{key} = {value}</CODE></LI>")

print("""</OL>
""")

try:
    s = os.environ["CONTENT_LENGTH"]
except KeyError:
    print("No environment variable named CONTENT_LENGTH.")
    print("</BODY>")
    print("</HTML>")
    sys.exit(1)

try:
    content_length = int(s)
except ValueError:
    print(f'Environment variable CONTENT_LENGTH contains non-integer "{s}".')
    print("</BODY>")
    print("</HTML>")
    sys.exit(1)

line = sys.stdin.read(content_length) #Read this number of bytes.

print(f"""\
<H2>{content_length} bytes of standard input</H2>

<PRE>{line}</PRE>
""")

#Create a dictionary of the values that the user entered into the form.
dictionary = dict(field.split("=") for field in line.split("&"))

print(f"""\
<H2>{len(dictionary)} values entered into the form</H2>

<OL>""")

for key, value in sorted(dictionary.items()):
    print(f"<LI><CODE>{key} = {value}</CODE></LI>")

print("""\
</OL>

<H2>Calendar</H2>

<PRE>""")

command = f'/usr/bin/cal {dictionary["month"]} "{dictionary["year"]}"'

sys.stdout.flush()      #Make sure the Content-type: has already been output.
os.system(command)

if "date" in dictionary:
    print()
    sys.stdout.flush()  #Make sure the above newline has already been output.
    os.system("/usr/bin/date")

print("""\
</PRE>
</BODY>
</HTML>""")

sys.exit(0)
