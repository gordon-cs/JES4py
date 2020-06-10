# From https://steemit.com/python/@makerhacks/building-an-image-viewer-in-python

import os
from PIL import Image
import glob
import tkinter
from PIL import ImageTk


# process the interaction
def event_action(event):
    print(repr(event))
    event.widget.quit()


# clicks
def clicked(event):
    event_action(event)


# keys
def key_press(event):
    event_action(event)


# set up the gui
window = tkinter.Tk()
window.bind("<Button>", clicked)
window.bind("<Key>", key_press)

# get the list of images
files = []
#files += glob.glob("/home/chrisg/Pictures/*.jpg")
files += glob.glob("/home/senning/f*.png")
#files += glob.glob("/home/chrisg/Pictures/*.gif")
files.sort(key=os.path.getmtime, reverse=True)

# for each file, display the picture
for file in files:
    print(file)
    window.title(file)
    picture = Image.open(file)
    tk_picture = ImageTk.PhotoImage(picture)
    picture_width = picture.size[0]
    picture_height = picture.size[1]
    window.geometry("{}x{}+100+100".format(picture_width, picture_height))
    image_widget = tkinter.Label(window, image=tk_picture)
    image_widget.place(x=0, y=0, width=picture_width, height=picture_height)

    # wait for events
    window.mainloop()
