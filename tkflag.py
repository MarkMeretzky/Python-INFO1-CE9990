"""
tkflag.py

Draw the United States flag in color on a tkinter Canvas widget.
"""
import tkinter              #in Python2, the t was uppercase

#dimensions of entire flag, in pixels
stripeHeight = 20           #height of each stripe
height = 13 * stripeHeight  #13 stripes
width = int(height * 19/10) #Wikipedia says aspect ratio of flag is 10:19

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title("United States Flag")
root.geometry(str(width) + "x" + str(height))

#highlightthickness = 0 allows the canvas to occupy the entire root.
canvas = tkinter.Canvas(root, highlightthickness = 0)

y = 0
while y < height:

    x = 0
    while x < width:

        if x < width * 2/5 and y < 7 * stripeHeight:
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = "blue")
        elif y % (2 * stripeHeight) < stripeHeight:
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = "red")                                     
        else:
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = "white")

        x += 1
    y += 1

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

#If the flag had buttons, checkboxes, etc.,
#the mainloop would let them respond to touches.
root.mainloop()
