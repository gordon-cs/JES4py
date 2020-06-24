# this class is solely for the purpose of
# making makeLighter makeDarker work.
# both of these functions destructively modify a color
# and a color in java is a constant value so we have to put
# this python interface here
#
# Buck Scharfnorth (28 May 2008): Modified to no longer assume the value is 0-255
# and the gray Color constructor to allow only 1 color parameter (will
# take 2, but ignores the second)

# JRS -- 2020-06-23 -- TEMPORARY FUNCTION UNTIL PIXEL CLASS IS AVAILABLE
def PixelcorrectLevel(c):
    """Return pixel value in range [0..255]
    """
    return c % 256

import math
from tkinter import colorchooser
class Color:

    def __init__(self, r, g=None, b=None):
        if b == None:
            if isinstance(r, Color):
                self.color = r
            else:
                val = PixelcorrectLevel(r)
                self.color = (val, val, val)
        else:
            self.color = (PixelcorrectLevel(r), PixelcorrectLevel(g), PixelcorrectLevel(b))

    def __str__(self):
        return "color r=" + str(self.getRed()) + " g=" + str(self.getGreen()) + " b=" + str(self.getBlue())

    def __repr__(self):
        return "Color(" + str(self.getRed()) + ", " + str(self.getGreen()) + ", " + str(self.getBlue()) + ")"

    def __eq__(self, newcolor):
        return ((self.getRed() == newcolor.getRed()) and (self.getGreen() == newcolor.getGreen()) and (self.getBlue() == newcolor.getBlue()))

    def __ne__(self, newcolor):
        return (not self.__eq__(newcolor))

    # Added by BrianO
    def __add__(self, other):
        r = self.getRed() + other.getRed()
        g = self.getGreen() + other.getGreen()
        b = self.getBlue() + other.getBlue()

        return Color(PixelcorrectLevel(r), PixelcorrectLevel(g), PixelcorrectLevel(b))

    # Added by BrianO
    def __sub__(self, other):
        r = self.getRed() - other.getRed()
        g = self.getGreen() - other.getGreen()
        b = self.getBlue() - other.getBlue()

        return Color(PixelcorrectLevel(r), PixelcorrectLevel(g), PixelcorrectLevel(b))

    def setRGB(self, r, g, b):
        self.color = (PixelcorrectLevel(r), PixelcorrectLevel(g), PixelcorrectLevel(b))

    def getRGB(self):
        return self.color

    def getRed(self):
        return self.color[0]

    def getGreen(self):
        return self.color[1]

    def getBlue(self):
        return self.color[2]

    def distance(self, othercolor):
        r = pow((self.getRed() - othercolor.getRed()), 2)
        g = pow((self.getGreen() - othercolor.getGreen()), 2)
        b = pow((self.getBlue() - othercolor.getBlue()), 2)
        return math.sqrt(r + g + b)

    def makeDarker(self):
        return self.color.darker()

    def makeLighter(self):
        return self.color.brighter()


def pickAColor():
    # Dorn 5/8/2009:  Edited to be thread safe since this code is executed from an
    # interpreter JESThread and will result in an update to the main JES GUI due to
    # it being a modal dialog.
    tup = colorchooser.askcolor()
    return tup[0]
