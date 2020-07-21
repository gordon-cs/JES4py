from jes4py import Config
import math
import wx

class Pixel:
    """Provides access to pixels within an PIL image

    Attributes
    ----------
    wrapLevels : boolean
        Indicates whether levels outside the range 0-255 are clamped
        or wrapped around (saturating or modular arithmetic).
        False to clamp levels, true to modulo them.
    """

    wrapLevels = False

    def __init__(self, image=None, x=None, y=None):
        """Pixel constructor

        Parameters
        ----------
        image : PIL.Image
            image the pixel belongs to
        x : int
            column of the pixel
        y : int
            row of the pixel
        """
        self.wrapLevels = Config.getConfigVal("CONFIG_WRAPPIXELVALUES")
        self.image = image
        self.x = x
        self.y = y
        #self.color = color

    def __str__(self):
        """Return string with pixel contents

        Returns
        -------
        str
            user-readable pixel information
        """
        rgb = self.image.getpixel((self.x, self.y))
        return "Pixel red={} green={} blue={}".format(rgb[0], rgb[1], rgb[2])

    def __repr__(self):
        """Return string representation of pixel

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
        value = 0
        # do nothing, as we have not implemented alpha values

    def setRed(self, value):
        """Set red level in the pixel

        Parameters
        ----------
        value : int
            red level for pixel
        """
        value = Pixel.correctLevel(value)
        color = Color(self.image.getpixel((self.x, self.y)))
        newColor = (value, color.getGreen(), color.getBlue())
        self.image.putpixel((self.x, self.y), newColor)

    def setGreen(self, value):
        """Set green level in the pixel

        Parameters
        ----------
        value : int
            green level for pixel
        """
        value = Pixel.correctLevel(value)
        color = Color(self.image.getpixel((self.x, self.y)))
        newColor = (color.getRed(), value, color.getBlue())
        self.image.putpixel((self.x, self.y), newColor)

    def setBlue(self, value):
        """Set blue level in the pixel

        Parameters
        ----------
        value : int
            blue level for pixel
        """
        value = Pixel.correctLevel(value)
        color = Color(self.image.getpixel((self.x, self.y)))
        newColor = (color.getRed(), color.getGreen(), value)
        self.image.putpixel((self.x, self.y), newColor)

    def colorDistance(self, testColor):
        """Computes the Euclidean distance norm between this pixel and a color

        Parameters
        ----------
        testColor : Color
            the color to compute the distance to

        Returns
        -------
        float
            the Euclidean distance between the two colors
        """
        r = pow((self.getRed() - testColor.getRed()), 2)
        g = pow((self.getGreen() - testColor.getGreen()), 2)
        b = pow((self.getBlue() - testColor.getBlue()), 2)
        return math.sqrt(r + g + b)

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

    #def updatePicture(self, alpha, red, green, blue):
        """Update the picture based on the passed color values for this pixel

        **** 2020-06-28 WHAT IS THIS FUNCTION SUPPOSED TO DO? ****

        Parameters
        ----------
        alpha : int
            transparency value (CURRENTLY IGNORED)
        red : int
            red color value
        green : int
            green color value
        blue : int
            blue color value
        """
        #self.setAlpha(alpha)
        #self.setRed(red)
        #self.setGreen(green)
        #self.setBlue(blue)

    @classmethod
    def correctLevel(cls, level):
        """Map color to [0..255] according to the wrapLevels setting

        Parameters
        ----------
        level : int
            nonnegative integer representing a color value

        Returns
        -------
        int
            corrected color level
        """
        level = int(level)
        if cls.wrapLevels:
            return level % 256
        elif level < 0:
            return 0
        elif level > 255:
            return 255
        return level

    @classmethod
    def setWrapLevels(cls, doWrap):
        """Changes Pixel's behavior for dealing with levels outside [0..255]

        Parameters
        ----------
        doWrap : boolean
            true to cause color level wrapping, false for level truncation
        """
        cls.wrapLevels = doWrap

    @classmethod
    def getWrapLevels(cls):
        """Return Pixel's behavior for dealing with levels outside [0..255]

        Returns
        -------
        boolean
            true means levels are wrapped, false means levels are truncated
        """
        return cls.wrapLevels




class Color:
    """Class for storing and doing computations with colors and RGB values

    Has getters and setters for the red, green, and blue portions of
    the over all color as well as giving the user capabilities to
    compare color values.
    """

    def __init__(self, r, g=None, b=None):
        """Initialize a color object

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

        if b == None or g == None:
            if isinstance(r, tuple):
                self.color = r
            elif isinstance(r, list):
                self.color = tuple(r)
            elif isinstance(r, Color):
                self.color = r.getRGB()
            else:
                val = Pixel.correctLevel(r)
                self.color = (val, val, val)
        else:
            r = Pixel.correctLevel(r)
            g = Pixel.correctLevel(g)
            b = Pixel.correctLevel(b)
            self.color = (r, g, b)

    def __str__(self):
        """String for Color

        Returns
        -------
        str
            user-readable color information
        """
        return "color r={} g={} b={}".format(self.color[0], self.color[1], self.color[2])
    
    def __repr__(self):
        """Representation of color

        Returns
        -------
        str
            string of color contents
        """
        return "Color({}, {}, {})".format(self.color[0], self.color[1], self.color[2])
    
    def __eq__(self, otherColor):
        """Test for equality between two color objects

        Parameters
        ----------
        otherColor : Color
            color to compare

        Returns
        -------
        boolean
            True if colors are the same, False otherwise
        """
        return (self.color == otherColor.color)

    def __ne__(self, otherColor):
        """Test for inequality between two color objects

        Parameters
        ----------
        otherColor : Color
            color to compare

        Returns
        -------
        boolean
            True if colors are not the same, False otherwise
        """
        return (not self.__eq__(otherColor))

    def __add__(self, otherColor):
        """Sum of this color and otherColor

        Parameters
        ----------
        otherColor : Color
            the color to add
        
        Returns
        -------
        Color
            the sum of the two colors, mapped to [0..255]
        """
        if isinstance(otherColor, Color):
            r = Pixel.correctLevel(self.color[0] + otherColor.color[0])
            g = Pixel.correctLevel(self.color[1] + otherColor.color[1])
            b = Pixel.correctLevel(self.color[2] + otherColor.color[2])
        return Color(r, g, b)

    def __sub__(self, otherColor):
        """Difference of this color and otherColor
        
        Parameters
        ----------
        otherColor : Color
            the color to subtract
        
        Returns
        -------
        Color
            the difference of the two colors, mapped to [0..255]
        """
        r = Pixel.correctLevel(self.color[0] - otherColor.color[0])
        g = Pixel.correctLevel(self.color[1] - otherColor.color[1])
        b = Pixel.correctLevel(self.color[2] - otherColor.color[2])
        return Color(r, g, b)

    def setRGB(self, r, g, b):
        """Sets this color's red, green, blue color values
    
        Parameters
        ----------
        r, g, b : int or float
            the red, green, and blue values
        """
        r = Pixel.correctLevel(r)
        g = Pixel.correctLevel(g)
        b = Pixel.correctLevel(b)
        self.color = (r, g, b)

    def getRGB(self):
        """Returns the colors RGB values in a tuple 

        Returns
        -------
        tuple of int
            tuple of red, green, and blue values
        """
        return self.color

    def getRed(self):
        """Returns the color's red value

        Returns
        -------
        int
            the red value
        """
        return self.color[0]

    def getGreen(self):
        """Returns the color's green value

        Returns
        -------
        int
            the green value
        """
        return self.color[1]

    def getBlue(self):
        """Returns the color's blue value

        Returns
        -------
        int
            the blue value
        """
        return self.color[2]

    def distance(self, otherColor):
        """Computes the Euclidean distance norm between two colors

        Parameters
        ----------
        otherColor : Color
            the color to compute the distance to

        Returns
        -------
        float
            the Euclidean distance between the two colors
        """
        if isinstance(otherColor, Color):
            r = pow((self.color[0] - otherColor.color[0]), 2)
            g = pow((self.color[1] - otherColor.color[1]), 2)
            b = pow((self.color[2] - otherColor.color[2]), 2)
            return math.sqrt(r + g + b)
        else:
            print("distance() expects a Color object")
            return

    def scaleColor(self, scaleFactor):
        """Return a uniformly scaled version of this color

        Parameters
        ----------
        scaleFactor : float
            the factor to scale each color component by

        Returns
        -------
        Color
            the color with the scaled components
        """
        r = Pixel.correctLevel(self.color[0] * scaleFactor)
        g = Pixel.correctLevel(self.color[1] * scaleFactor)
        b = Pixel.correctLevel(self.color[2] * scaleFactor)
        return Color(r, g, b)

    def makeDarker(self):
        """Return a darker version of this color

        Returns
        -------
        Color
            darker version of this color
        """
        return self.scaleColor(7.0/10.0)

    def makeLighter(self):
        """Return a lighter version of this color

        Returns
        -------
        Color
            lighter version of this color
        """
        if self.color == (0,0,0):
            # Special case -- black gets lighted to very dark gray
            lighterColor = Color(3,3,3)
        else:
            # Scale color values by 10/7
            lighterColor = self.scaleColor(10.0/7.0)
            if max(lighterColor.color) <= 2:
                # if all color values are 2 or less we need to adjust them
                c = list(lighterColor.color)
                for i in range(3):
                    if c[i] > 0 and c[i] < 2:
                        c[i] += 3
                    elif c[i] > 0 and c[i] == 2:
                        c[i] += 2
                lighterColor = Color(c)
        return lighterColor

    @classmethod
    def pickAColor(cls):
        app = wx.App()
        dlg = wx.ColourDialog(wx.GetApp().GetTopWindow())
        color = None
        if dlg.ShowModal() == wx.ID_OK:
            red =  dlg.GetColourData().GetColour().Red()
            green = dlg.GetColourData().GetColour().Green()
            blue = dlg.GetColourData().GetColour().Blue()
            color = Color(red,green,blue)
        return color
