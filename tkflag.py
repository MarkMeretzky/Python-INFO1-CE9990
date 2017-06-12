"""
tkflag.py

Draw the United States flag in color on a tkinter Canvas.
"""
import tkinter              #in Python2, the t was uppercase

root = tkinter.Tk()         #The root will contain everything we draw.
root.title("United States Flag")

#dimensions of entire flag, in pixels
stripeHeight = 20           #height of each stripe, in pixels
height = 13 * stripeHeight  #13 stripes
width = int(height * 19/10) #Wikipedia says aspect ratio of flag is 10:19
root.geometry(str(width) + "x" + str(height))

#highlightthickness = 0 will allow the canvas to occupy the entire root.
canvas = tkinter.Canvas(root, highlightthickness = 0, background = "white")

#seven red stripes
stripe = 0
while stripe < 7:
    y = stripeHeight * (2 * stripe)
    while y < stripeHeight * (2 * stripe + 1):
        x = 0
        while x < width:
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = "red")
            x += 1
        y += 1
    stripe += 1

#blue rectangle
y = 0
while y < 7 * stripeHeight:
    x = 0
    while x < width * 2/5:
        canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = "blue")
        x += 1
    y += 1

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

#If the flag had buttons, checkboxes, etc.,
#this would let them respond to touches.
root.mainloop()
