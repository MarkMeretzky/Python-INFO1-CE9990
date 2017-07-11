#!/usr/bin/env python3
"""
This gateway is
/home/m/meretzkm/public_html/cgi-bin/pythoncal.cgi.
It outputs a page of HTML containing a calendar and is executed from the form
/home/m/meretzkm/public_html/python/cgi/cgi.html
The URL of this form is
http://oit2.scps.nyu.edu/~meretzkm/python/cgi/cgi.html
"""

import sys
import os   #operating system

envHeader = """\
Content-type: text/html

<HTML>
<HEAD>
<TITLE>Calendar</TITLE>
</HEAD>

<BODY>
<H1>Calendar</H1>

<H2>{} environment variables</H2>

<PRE>"""

print(envHeader.format(len(os.environ)))   #os.environ is a dictionary.

for key in sorted(os.environ.keys()):
    print(key, "=", os.environ[key])

print("""</PRE>
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
    print("Environment variable CONTENT_LENGTH contains non-integer \"", s,
        "\".", sep = "")
    print("</BODY>")
    print("</HTML>")
    sys.exit(1)

line = sys.stdin.read(content_length)      #Read this number of bytes.

stdinHeader = """\
<H2>{} bytes of standard input</H2>

<PRE>{}</PRE>
"""

print(stdinHeader.format(content_length, line))

dictionary = {}                            #Start with an empty dictionary.
fields = line.split("&")
for field in fields:
    (key, value) = field.split("=")        #multiple assignment
    dictionary[key] = value

valuesHeader = """\
<H2>{} values entered into the form</H2>

<PRE>"""

print(valuesHeader.format(len(dictionary)))

for key in sorted(dictionary.keys()):
    print(key, "=", dictionary[key])

calHeader = """\
</PRE>

<H2>Calendar</H2>

<PRE>"""

print(calHeader)

command = \
    "/usr/bin/cal {} \"{}\"".format(dictionary["month"], dictionary["year"])

sys.stdout.flush()      #Make sure Content-type: has already been output.
os.system(command)

if "date" in dictionary:
    print("<BR>")
    sys.stdout.flush()  #Make sure the above <BR> has already been output.
    os.system("/usr/bin/date")

footer = """\
</PRE>
</BODY>
</HTML>"""

print(footer)
sys.exit(0)
