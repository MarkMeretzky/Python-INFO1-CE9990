"""
tkflag.py

Draw the United States flag in color on a tkinter Canvas widget.
"""

import tkinter              #in Python2, the t was uppercase

stripeHeight = 20           #height of each stripe

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title("United States Flag")

#dimensions of entire flag, in pixels
height = 13 * stripeHeight  #13 stripes
width = int(height * 19/10) #Wikipedia says aspect ratio of flag is 10:19
root.geometry(f"{width}x{height}")

#highlightthickness = 0 allows the canvas to occupy the entire root.
canvas = tkinter.Canvas(root, highlightthickness = 0, background = "white")

#7 red stripes
for i in range(7):
    canvas.create_rectangle(0, 2 * i * stripeHeight,
        width, (2 * i + 1) * stripeHeight, width = 0, fill = "red")

canvas.create_rectangle(0, 0, width * 2/5, 7 * stripeHeight,
    width = 0, fill = "blue")

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

#If the flag had buttons, checkboxes, etc.,
#the mainloop would let them respond to touches.
root.mainloop()
