"""
image.py

Input a binary file.  Since the file is not a text file, we cannot say
for line in lines:
"""

import sys
import imghdr   #image header
import tkinter

#macOS
filename = "/Users/myname/Desktop/escalus.gif"
#Microsoft Windows
#filename = r"C:\Users\Myname\Desktop\escalus.gif"

try:
    binaryFile = open(filename, "rb")   #read binary
except FileNotFoundError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
except PermissionError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

sequenceOfBytes = binaryFile.read()     #not string of characters
binaryFile.close()
print(f"The image is of type {imghdr.what(None, h = sequenceOfBytes)}.")
print(f"len(sequenceOfBytes) = {len(sequenceOfBytes):,}")

root = tkinter.Tk()

try:
    #The following statement cannot come before the tkinter.Tk().
    photoImage = tkinter.PhotoImage(data = sequenceOfBytes)
except tkinter.TclError as error:
    print(error, file = sys.stderr) #"couldn't recognize image data" when image is jpg.
    sys.exit(1)

root.geometry("720x480")
root.title("Prince Escalus")

label = tkinter.Label(root, image = photoImage)
label.pack()

root.mainloop()
