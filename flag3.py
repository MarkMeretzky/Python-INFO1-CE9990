"""
tkflag.py

Draw the United States flag in color on a tkinter Canvas widget, with one star.
"""

import math
import tkinter

stripeHeight = 20           #height of each stripe

root = tkinter.Tk()
root.title("United States Flag")

#dimensions of entire flag, in pixels
height = 13 * stripeHeight  #13 stripes
width = int(height * 19/10) #Wikipedia says aspect ratio of flag is 10:19
root.geometry(f"{width}x{height}")
canvas = tkinter.Canvas(root, highlightthickness = 0, background = "white")

#7 red stripes
for i in range(7):
    canvas.create_rectangle(0, 2 * i * stripeHeight,
        width, (2 * i + 1) * stripeHeight, width = 0, fill = "red")

canvas.create_rectangle(0, 0, width * 2/5, 7 * stripeHeight,
    width = 0, fill = "blue")

#The star is inscribed in this imaginary circle.
xCenter = width / 5
yCenter = 3.5 * stripeHeight
radius = yCenter * 2/3

start = math.pi / 2      #First point of star points straight up.
delta = .4 * 2 * math.pi #Successive points are 144 degrees apart.

#The y values are subtracted because the y axis points downwards.
canvas.create_polygon(
    xCenter + radius * math.cos(start),
    yCenter - radius * math.sin(start),
    
    xCenter + radius * math.cos(start + 1 * delta),
    yCenter - radius * math.sin(start + 1 * delta),

    xCenter + radius * math.cos(start + 2 * delta),
    yCenter - radius * math.sin(start + 2 * delta),
    
    xCenter + radius * math.cos(start + 3 * delta),
    yCenter - radius * math.sin(start + 3 * delta),

    xCenter + radius * math.cos(start + 4 * delta),
    yCenter - radius * math.sin(start + 4 * delta),

    fill = "white"
)

canvas.pack(expand = tkinter.YES, fill = "both")
root.mainloop()
