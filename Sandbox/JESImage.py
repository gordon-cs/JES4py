from __future__ import print_function
from __future__ import division

from PIL import Image
import easygui as eg
#import tkinter

black          = (  0,   0,   0)
cyan           = (  0, 255, 255)
magenta        = (255,   0, 255)
yellow         = (255, 255,   0)
red            = (255,   0,   0)
green          = (  0, 255,   0)
blue           = (  0,   0, 255)
white          = (255, 255, 255)

# ----------------------------------------------------------------------------
# File functions
# ----------------------------------------------------------------------------

def pickAFile():
#    return eg.fileopenbox(title="pickAFile()", default="*.jpg",
#                          filetypes=["*.jpg","*.png","Image files"])
    return eg.fileopenbox(title="Pick A File")

# ----------------------------------------------------------------------------
# Picture functions
# ----------------------------------------------------------------------------

def makeEmptyPicture( width, height, acolor = white ):
    return Image.new( "RGB", (width, height), acolor )

def makePicture(file):
    return Image.open(file)

def show( picture ):
    picture.show()

def explore(picture):
    return True

def makeColor(r, g, b):
    return (r, g, b)

def pickAColor():
    return white

if __name__ == "__main__":
    pic1 = makeEmptyPicture(100, 100)
    show(pic1)

    c1 = makeColor(200, 0, 0)
    pic2 = makeEmptyPicture(100, 100, c1)
    explore(pic2)

    c2 = pickAColor()
    print(c2)

    file = pickAFile()
    print(file)

    pic3 = makePicture(file)
    show(pic3)
