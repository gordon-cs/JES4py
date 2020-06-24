from PIL import Image
import math
class Pixel:

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        #self.color = color

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def __str__(self):
        pix = self.image.getpixel((self.x,self.y))
        output = "Pixel red={} green={} blue={}".format(pix[0], pix[1], pix[2])
        return output

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImage(self):
        return self.image

    def getRed(self):
        col = self.image.getpixel((self.x,self.y))
        return col[0]

    def getGreen(self):
        col = self.image.getpixel((self.x,self.y))
        return col[1]

    def getBlue(self):
        col = self.image.getpixel((self.x,self.y))
        return col[2]

    def setRed(self, value):
        col = self.image.getpixel((self.x,self.y))
        self.image.putpixel((self.x, self.y),(value, col[1], col[2]))

    def setGreen(self, value):
        col = self.image.getpixel((self.x,self.y))
        self.image.putpixel((self.x, self.y), (col[0], value, col[2]))

    def setBlue(self, value):
        col = self.image.getpixel((self.x,self.y))
        self.image.putpixel((self.x, self.y), (col[0], col[1], value))

    def getColor(self):
        pix = self.image.getpixel((self.x,self.y))
        col = Color(pix[0],pix[1], pix[2])
        return col

    def setColor(self, color):
            col = (color.getRed(), color.getGreen(), color.getBlue())
            self.image.putpixel((self.x, self.y), col)

    def correctLevel(self, level):
        return level%256

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
class Color:

    def __init__(self, r, g=None, b=None):
        if b == None:
            if isinstance(r, Color):
                self.color = r
            else:
                val = Pixel.correctLevel(r)
                self.color = (val, val, val)
        else:
            self.color = (Pixel.correctLevel(Pixel, r), Pixel.correctLevel(Pixel, g), Pixel.correctLevel(Pixel, b))

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

        return Color(Pixel.correctLevel(r), Pixel.correctLevel(g), Pixel.correctLevel(b))

    # Added by BrianO
    def __sub__(self, other):
        r = self.getRed() - other.getRed()
        g = self.getGreen() - other.getGreen()
        b = self.getBlue() - other.getBlue()

        return Color(Pixel.correctLevel(r), Pixel.correctLevel(g), Pixel.correctLevel(b))

    def setRGB(self, r, g, b):
        self.color = (Pixel.correctLevel(r), Pixel.correctLevel(g), Pixel.correctLevel(b))

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

