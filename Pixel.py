from PIL import Image
import math
import JESConfig

class Pixel:
    """Provides access to pixels within a PIL image
    """

    def __init__(self, image=None, x=None, y=None):
        """Pixel constructor

        Parameters
        ----------
        image : PIL.Image
            image the pixel belongs to
        x : int
            column of the pixel
        y : int
            row of hhe pixel
        """
        self.image = image
        self.x = x
        self.y = y
        #self.color = color

    def __str__(self):
        """String for pixel

        Returns
        -------
        str
            user-readable pixel information
        """
        rgb = self.image.getpixel((self.x, self.y))
        return "Pixel red={} green={} blue={}".format(rgb[0], rgb[1], rgb[2])

    def __repr__(self):
        """Represetation of pixel

        Returns
        -------
        str
            string of pixel contents
        """
        return self.__str__()

    def getX(self):
        """Gets column containing pixel

        Returns
        -------
        int
           column containing the pixel
        """
        return self.x

    def getY(self):
        """Gets row containing pixel

        Returns
        -------
        int
           row containing the pixel
        """
        return self.y

    def getAlpha(self):
        """Return alpha level in pixel (NOT IMPLEMENTED)

        Returns
        -------
        int
            alpha level in pixel
        """
        return 255

    def getRed(self):
        """Return red level in pixel

        Returns
        -------
        int
            red level in pixel
        """
        rgb = self.image.getpixel((self.x, self.y))
        return rgb[0]

    def getGreen(self):
        """Return green level in pixel

        Returns
        -------
        int
            green level in pixel
        """
        rgb = self.image.getpixel((self.x, self.y))
        return rgb[1]

    def getBlue(self):
        """Return blue level in pixel

        Returns
        -------
        int
            blue level in pixel
        """
        rgb = self.image.getpixel((self.x, self.y))
        return rgb[2]

    def getAverage(self):
        """Return the average of the color values of this pixel

        Returns
        -------
        int
            rounded average of red, green, and blue pixel values
        """
        rgb = self.image.getpixel((self.x, self.y))
        return round((rgb[0] + rgb[1] + rgb[2]) / 3.0)
    
    def setAlpha(self, value):
        """Set alpha level in the pixel (NOT IMPLEMENTED)

        Parameters
        ----------
        value : int
            alpha level for pixel
        """
        # do nothing, as we have not implemented alpha values

    def setRed(self, value):
        """Set red level in the pixel

        Parameters
        ----------
        value : int
            red level for pixel
        """
        color = Color(self.image.getpixel((self.x, self.y)))
        color.setRed(round(value))
        self.image.putpixel((self.x, self.y), color.getRGB())

    def setGreen(self, value):
        """Set green level in the pixel

        Parameters
        ----------
        value : int
            green level for pixel
        """
        color = Color(self.image.getpixel((self.x, self.y)))
        color.setGreen(round(value))
        self.image.putpixel((self.x, self.y), color.getRGB())

    def setBlue(self, value):
        """Set blue level in the pixel

        Parameters
        ----------
        value : int
            blue level for pixel
        """
        color = Color(self.image.getpixel((self.x, self.y)))
        color.setBlue(round(value))
        self.image.putpixel((self.x, self.y), color.getRGB())

    def getColor(self):
        """Returns the color object for the pixel
        Returns
        -------
        Color
            color object for the pixel
        """
        return Color(self.image.getpixel((self.x, self.y)))

    def setColor(self, color):
        """Set the color of a pixel

        Parameters
        ----------
        color : Color
            color to assign to pixel
        """
        self.image.putpixel((self.x, self.y), color.getRGB())

    def setColorFrom(self, otherPixel):
        """Set color of this pixel using color value from otherPixel

        Parameters
        ----------
        otherPixel : Pixel
            pixel to get color values from
        """
        self.setColor(otherPixel.getColor())

    def updatePicture(self, alpha, red, green, blue):
        """Update the picture based on the passed color values for this pixel

        Parameters
        ----------
        alpha : int
            transparancy value (CURRENTLY IGNORED)
        red : int
            red color value
        green : int
            green color value
        blue : int
            blue color value
        """
        #self.setAlpha(alpha)
        self.setRed(red)
        self.setGreen(green)
        self.setBlue(blue)

class Color:
    """Class for storing and doing computations with colors and RGB values

    Has getters and setters for the red, green, and blue portions of
    the over all color as well as giving the user capabilities to
    compare color values.  Currently makeLighter and makeDarker do not
    work properly
    """

    wrapColorLevels = False

    def __init__(self, r, g=None, b=None):
        """Initalize a color object

        Parameters
        ----------
        r : list, tuple, Color or int
            If r is a list or a tuple then r contains the RGB values,
            if r is a Color object then use its color list for RGB values,
            if r is an int then use it for all colors (graylevel)
        g : int
            green level (if not provided then r is used)
        b : int
            blue level (if not provided then r is used)
        """
        self.wrapColorLevels = JESConfig.CONFIG_WRAPPIXELVALUES != '0'

        if b == None or g == None:
            if isinstance(r, tuple):
                self.color = list(r)
            elif isinstance(r, list):
                self.color = r
            elif isinstance(r, Color):
                self.color = r.color
            else:
                val = self.correctLevel(r)
                self.color = [val, val, val]
        else:
            self.color = [self.correctLevel(r),
                          self.correctLevel(g),
                          self.correctLevel(b)]

    def __str__(self):
        """String for Color

        Returns
        -------
        str
            user-readable color information
        """
        return "color r={} g={} b={}".format(self.color[0], self.color[1], self.color[2])
    
    def __repr__(self):
        """Represetation of color

        Returns
        -------
        str
            string of color contents
        """
        return self.__str__()
    
    def __eq__(self, newColor):
        return (self.color == newColor.color)

    def __ne__(self, newColor):
        return (not self.__eq__(newColor))

    # Added by BrianO
    def __add__(self, otherColor):
        if isinstance(otherColor, Color):
            r = self.correctLevel(self.color[0] + otherColor.color[0])
            g = self.correctLevel(self.color[1] + otherColor.color[1])
            b = self.correctLevel(self.color[2] + otherColor.color[2])
        return Color(r, g, b)

    # Added by BrianO
    def __sub__(self, otherColor):
        r = self.correctLevel(self.color[0] - otherColor.color[0])
        g = self.correctLevel(self.color[1] - otherColor.color[1])
        b = self.correctLevel(self.color[2] - otherColor.color[2])
        return Color(r, g, b)

    def setRGB(self, r, g, b):
        self.color = [self.correctLevel(r), self.correctLevel(g),
                      self.correctLevel(b)]

    def getRGB(self):
        red = self.correctLevel(self.color[0])
        green = self.correctLevel(self.color[1])
        blue = self.correctLevel(self.color[2])
        return (red,green,blue)

    def setRed(self, value):
        self.color[0] = self.correctLevel(value)

    def setGreen(self, value):
        self.color[1] = self.correctLevel(value)

    def setBlue(self, value):
        self.color[2] = self.correctLevel(value)

    def getRed(self):
        return self.color[0]

    def getGreen(self):
        return self.color[1]

    def getBlue(self):
        return self.color[2]

    def distance(self, otherColor):
        if isinstance(otherColor, Color):
            r = pow((self.color[0] - otherColor.color[0]), 2)
            g = pow((self.color[1] - otherColor.color[1]), 2)
            b = pow((self.color[2] - otherColor.color[2]), 2)
            return math.sqrt(r + g + b)
        else:
            print("distance() expects a Color object")
            return

    def scaleColor(self, scaleFactor):
        r = self.correctLevel(self.color[0] * scaleFactor)
        g = self.correctLevel(self.color[1] * scaleFactor)
        b = self.correctLevel(self.color[2] * scaleFactor)
        return Color(r, g, b)

    def makeDarker(self):
        return self.scaleColor(0.8)

    def makeLighter(self):
        return self.scaleColor(1.25)

    def correctLevel(self, level):
        """Map color to [0..255] according to the wrapColorLevels setting

        Parameters
        ----------
        level : int
            nonnegative integer representing a color value

        Returns
        -------
        int
            corrected color level
        """
        if self.wrapColorLevels:
            level = round(level) % 256
        elif level < 0:
            level = 0
        elif level > 255:
            level = 255
        return level

    def setWrapLevels(self, doWrap):
        """Changes Pixel's behavior for dealing with levels outside [0..255]

        Parameters
        ----------
        doWrap : boolean
            true to cause color level wrapping, false for level truncation
        """
        self.wrapColorLevels = doWrap

    def getWrapLevels(self):
        """Return Pixel's behavior for dealing with levels outside [0..255]

        Returns
        -------
        boolean
            true means levels are wrapped, false means levels are truncated
        """
        return self.wrapColorLevels

