import os, sys
import wx
import subprocess, tempfile
import PIL.ImageDraw, PIL.Image
import JESConfig
from Pixel import Pixel
from Pixel import Color
from FileChooser import *
from pathlib import Path

class Picture:

    def __init__(self, image=None, extension=".jpg"):
        self.image = image
        self.extension = extension
        try:
            self.filename = self.title = image.filename
        except AttributeError:
            self.filename = self.title = ''

    def __str__(self):
        """Return string representation of this picture

        Returns
        -------
        str
            representation of this picture
        """
        output = "Picture, filename {} height {} width {}".format(
            self.image.filename, self.image.height, self.image.width)
        return output

    def getFileName(self):
        """Return picture file name

        Returns
        -------
        str
            name of file containing picture data
        """
        return self.image.filename

    def setFileName(self, filename):
        """Set picture file name

        Parameters
        ----------
        filename : str
            filename to assign to this picture
        """
        self.image.filename = filename

    def getTitle(self):
        """Return picture title

        Returns
        -------
        str
            picture title
        """
        return self.title
        
    def setTitle(self, title):
        """Set picture title

        Parameters
        ----------
        title : str
            title to assign to this picture
        """
        self.title = title

    def getPixels(self):
        """Return list of pixels contained in picture

        Returns a list of all pixels in this picture as a flattened array.
        Pixels are listed row-by-row.

        Returns
        -------
        list of Pixel
            list of pixels in this picture
        """
        pixels = list()
        for y in range(self.image.height):
            for x in range(self.image.width):
                pixels.append(Pixel(self.image, x, y))
        return pixels

    def getPixel(self, x, y):
        """Return the pixel at specified coordinates

        Parameters
        ----------
        x, y : int
            the coordinates of the pixel

        Returns
        -------
        Pixel
            the pixel at (x,y) in this picture
        """
        pix = Pixel(self.image, x, y)
        return pix

    def getBasicPixel(self, x, y):
        """Return the pixel at specified coordinates as a tuple.

        Parameters
        ----------
        x, y : int
            the coordinates of the pixel

        Returns
        -------
        Tuple
            the color of the pixel at position (x,y) as a tuple
        """
        return self.getPixel(x,y).getColor().getRGB()

    def setBasicPixel(self, x, y, rgb):
        """Sets the pixel at specified coordinates to a color based on rgb(Tuple)

        Parameters
        ----------
        x, y : int
            the coordinates of the pixel
        rgb : tuple
            the color the pixel will be set to
        """
        col = Color(rgb[0], rgb[1], rgb[2])
        self.getPixel(x,y).setColor(col)

    def getImage(self):
        """Return the PIL Image associated with this picture

        Returns
        -------
        PIL.Image
            the PIL Image associated with this picture
        """
        return self.image

    def setImage(self, image):
        """Sets the PIL Image associated with this picture

        Parameters
        ----------
        image : PIL.Image
            the PIL Image to associate with this picture
        """
        self.image = image

    def getWxImage(self, copy_alpha=True):
        """Return a wx.Image version of this image

        Parameters
        ----------
        copy_alpha : boolean
            if True and image has alpha values, then convert them too

        Returns
        -------
        wx.Image
            the converted image
        """
        orig_width, orig_height = self.image.size
        wx_img = wx.Image(orig_width, orig_height)
        wx_img.SetData(self.image.convert('RGB').tobytes())

        if copy_alpha and (self.image.mode[-1] == 'A'):
            alpha = self.image.getchannel("A").tobytes()
            wx_img.InitAlpha()
            for i in range(orig_width):
                for j in range(orig_height):
                    wx_img.SetAlpha(i, j, alpha[i + j * orig_width])
        return wx_img

    def getWidth(self):
        """Return the width of this image in this picture

        Returns
        -------
        int
            number of pixels in a row of this image
        """
        return self.image.width

    def getHeight(self):
        """Return the height of the image in this picture

        Returns
        -------
        int
            number of pixels in a column of this image
        """
        return self.image.height

    #////////////////////// methods ///////////////////////////////////////

    #  Method to return a string with information about this picture.
    #  @return a string with information about the picture such as fileName,
    #  height and width.
    # public String toString() {
    #     String output = "Picture, filename " + getFileName() +
    #                     " height " + getHeight()
    #                     + " width " + getWidth();
    #     return output;
    # }

    #/* adding graphics to pictures, for use in JES. (added by alexr, Oct 2006) */

    def addLine(self, acolor, x1, y1, x2, y2):
        """Draw a line on this picture
    
        acolor : Color
            the color of the line
        x1 : int
            the x-coordinate of the first point
        y1 : int
            the y-coordinate of the first point
        x2 : int
            the x-coordinate of the second point
        y2 : int
            the y-coordinate of the second point
        """
        draw = PIL.ImageDraw.Draw(self.image)
        shape = [x1, y1, x2, y2]
        draw.line(shape, fill=acolor.getRGB())

    #  * Method to add a line of text to a picture
    #  *    @param acolor the color of the text
    #  *    @param x the x-coordinate of the bottom left corner of the text
    #  *    @param y the y-coordinate of the bottom left corner of the text
    #  *    @param string the text to be added to the picture
    def addText(self, acolor, x, y, string):
        """Adds text to the image
    
        acolor : Color
            the color of the text
        x : int
            the x-coordinate of the top left corner of the text
        y : int
            the y-coordinate of the top left corner of the text
        string : string
            the text that will be drawn on the picture
        """
        draw = PIL.ImageDraw.Draw(self.image)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        # font = ImageFont.truetype("sans-serif.ttf", 16)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((x, y), string, acolor.getRGB())

    #  * Method to add text to a picture withe a particular font style
    #  *    @param acolor the color of the text
    #  *    @param x the x-coordinate of the bottom left corner of the text
    #  *    @param y the y-coordinate of the bottom left corner of the text
    #  *    @param string the text to be added to the picture
    #  *    @param style the font style to be used
    # def addTextWithStyle(self, acolor, x, y, string, style):
    #     draw = PIL.ImageDraw.Draw(self.image)
    #     # font = ImageFont.truetype(<font-file>, <font-size>)
    #     # font = ImageFont.truetype("sans-serif.ttf", 16)
    #     # draw.text((x, y),"Sample Text",(r,g,b))

    #     draw.text((x, y), string, acolor.getRGB())

    def addRect(self, acolor, x, y, w, h):
        """Draw the outline of a rectangle on this picture
    
        acolor : instance of Color class
            the color of the rectangle border
        x : int
            the x-coordinate of the upper-left corner of the rectangle
        y : int
            the y-coordinate of the upper-left corner of the rectangle
        w : int
            the width of the rectangle
        h : int
            the height of the rectangle
        """
        draw = PIL.ImageDraw.Draw(self.image)
        shape = [x, y, x+w, y+h]
        draw.rectangle(shape, fill = None, outline = acolor.getRGB()) 

    def addRectFilled(self, acolor, x, y, w, h):
        """Draw a filled rectangle on this picture
    
        acolor : instance of Color class
            the color that the rectangle is filled
        x : int
            the x-coordinate of the upper-left corner of the rectangle
        y : int
            the y-coordinate of the upper-left corner of the rectangle
        w : int
            the width of the rectangle
        h : int
            the height of the rectangle
        """
        draw = PIL.ImageDraw.Draw(self.image)
        shape = [x, y, x+w, y+h]
        color = acolor.getRGB()
        draw.rectangle(shape, fill = color, outline = color) 

    def addOvalFilled(self, acolor, x, y, w, h):
        """Draw a filled oval on this picture
    
        acolor : instance of Color class
            the color that the oval is filled with.
        x : int
            the x-coordinate of the upper-left corner of the boundary rectangle for the oval
        y : int
            the y-coordinate of the upper-left corner of the boundary rectangle for the oval
        w : int
            the width of the oval
        h : int
            the height of the oval
        """
        draw = PIL.ImageDraw.Draw(self.image)
        shape = [x, y, x+w, y+h]
        color = acolor.getRGB()
        draw.ellipse(shape, fill=color, outline=color, width=1)

    def addOval(self, acolor, x, y, w, h):
        """Draw the outline of an oval on this picture
    
        acolor : instance of Color class
            the color of the oval border
        x : int
            the x-coordinate of the upper-left corner of the boundary rectangle for the oval
        y : int
            the y-coordinate of the upper-left corner of the boundary rectangle for the oval
        w : int
            the width of the oval
        h : int
            the height of the oval
        """
        draw = PIL.ImageDraw.Draw(self.image)
        shape = [x, y, x+w, y+h]
        draw.ellipse(shape, fill=None, outline=acolor.getRGB(), width=1)

    def addArcFilled(self, acolor, x, y, w, h, start, angle):
        """Draw a filled in arc on this picture
    
        acolor : instance of Color class
            the color that the arc is filled with
        x : int
            the x-coordinate of the center of the arc
        y : int
            the y-coordinate of the center of the arc
        w : int
            the width of the arc
        h : int
            the height of the arc
        start : int
            the start angle of the arc in degrees
        angle : int
            the angle of the arc relative to start in degrees
        """
        draw = PIL.ImageDraw.Draw(self.image)
        shape = [x, y, x+w, y+h]
        end = -start % 360
        start = -(start+angle) % 360
        if start > end:
            start, end = end, start
        color = acolor.getRGB()
        draw.pieslice(shape, start, end, fill=color, outline=color, width=1)

    def addArc(self, acolor, x, y, w, h, start, angle):
        """Draw the outline of an arc on this picture
    
        acolor : instance of Color class
            the color that outlines arc
        x : int
            the x-coordinate of the center of the arc
        y : int
            the y-coordinate of the center of the arc
        w : int
            the width of the arc
        h : int
            the height of the arc
        start : int
            the start angle of the arc in degrees
        angle : int
            the angle of the arc relative to start in degrees
        """
        draw = PIL.ImageDraw.Draw(self.image)
        shape = [x, y, x+w, y+h]
        end = -start % 360
        start = -(start+angle) % 360
        if start > end:
            start, end = end, start
        draw.arc(shape, start, end, fill=acolor.getRGB(), width=1)

    def copyPicture(self, sourcePicture):
        """Copies the passed in picture to the current Picture

        Parameters
        ----------
        sourcePicture : Picture
            the Picture object that self will look like

        """
        im = PIL.Image.new("RGB", (self.getWidth(), self.getHeight()), (0,0,0))
        im = sourcePicture.getImage().copy()
        self.setImage(im)

    def setAllPixelsToAColor(self, acolor):
        """Makes the image associated with the picture filled in with one color

        Parameters
        ----------
        acolor : instance of Color class
            the color that outlines arc
        """
        if not isinstance(acolor, Color):
            print ("setAllPixelsToAColor(color): Input is not a color")
            raise ValueError
        self.image = PIL.Image.new("RGB", (self.getWidth(), self.getHeight()), acolor.getRGB())

    def copyInto(self, dest, upperLeftX, upperLeftY):
        """Returns a picture with the current picture copied into it

        Copies the pixels in the current picture into the dest picture
        starting at point (upperLeftX,upperLeftY)

        Parameters
        ----------
        dest : Picture
            the Picture that the current picture will be copied into
        upperLeftX : int
            the x-coord of the upper-left corner in dest where the current picture will be copied
        upperLeftY : int
            the y-coord of the upper-left corner in dest where the current picture will be copied

        Returns
        -------
        Picture
            the dest picture that has self copied into it
        """
        for x in range(upperLeftX, self.getWidth()):
            for y in range(upperLeftY, self.getHeight()):
                smallPix = self.getPixel(x,y)
                dest.getPixel(x,y).setColor(smallPix.getColor())

        return dest

    def crop(self, upperLeftX, upperLeftY, width, height):
        """Returns a cropped version of this picture

        Copies the pixels in it starting at the specified upper-left corner
        and taking as many pixels as specified by width and height

        Parameters
        ----------
        upperLeftX : int
            the x-coord of the upper-left corner new cropped image
        upperLeftY : int
            the y-coord of the upper-left corner new cropped image
        width : int
            the desired width of the cropped picture
        height : int
            the desired height of the cropped picture

        Returns
        -------
        Picture
            a cropped version of the picture
        """
        croppedImage = self.image.crop((upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height))
        pic = Picture(croppedImage)
        pic.filename = self.filename
        pic.title = self.title
        return pic

    def __saveInTempFile(self):
        """Create temporary image file

        Returns
        -------
        string
            path to temporary image file
        """
        filename = os.path.join(tempfile.gettempdir(),
            "jes_" + next(tempfile._get_candidate_names()) + self.extension)
        self.write(filename)
        return filename

        # Run show script
    def __runScript(self, script, *argv):
        scriptpath = os.path.join(JESConfig.getConfigVal("CONFIG_JESPATH"), script)
        subprocess.Popen([sys.executable, scriptpath] + list(argv))

    def show(self):
        #script = os.path.join(JESConfig.getConfigVal("CONFIG_JESPATH"), 'show.py')
        filename = self.__saveInTempFile()
        self.__runScript('show.py', filename, self.title)
        #subprocess.Popen([sys.executable, script, filename, self.title])

        #os.remove(filename)

    def pictureTool(self):
        filename = self.__saveInTempFile()
        self.__runScript('pictureTool.py', filename, self.title)

        #os.remove(filename)

    def scale(self, xFactor, yFactor):
        """Create new scaled picture

        Method to create a new picture by scaling the current picture by
        the given x and y factors

        Parameters
        ----------
        xFactor : float
            the amount to scale in x
        yFactor : float
            the amount to scale in y

        Returns
        -------
        Picture

            a scaled version of the picture
        """
        scaledImage = self.image.resize((int(self.image.width*xFactor), int(self.image.height*yFactor)))
        pic = Picture(scaledImage)
        pic.filename = self.filename
        pic.title = None
        return pic

    def getPictureWithHeight(self, height):
        """Returns a scaled version of this picture

        Scales the picture so that the height is equal to height while keeping the same ratio

        Parameters
        ----------
        height : int
            The height of the returned picture

        Returns
        -------
        Picture
            a scaled version of the picture with height of (height)
        """
        # // set up the scale tranform
        yFactor = height / self.getHeight()
        result = self.scale(yFactor, yFactor)
        return result
        
    def getPictureWithWidth(self, width):
        """Returns a scaled version of this picture

        Scales the picture so that the width is equal to width while keeping the same ratio

        Parameters
        ----------
        width : int
            The width of the returned picture

        Returns
        -------
        Picture
            a scaled version of the picture with width of (width)
        """
        # // set up the scale tranform
        xFactor = width / self.getWidth()
        result = self.scale(xFactor, xFactor)
        return result

    def loadPictureAndShowIt(self, fileName):
        """Load picture from a file and show it

        Parameters
        ----------
        fileName : string
            the name of the file to load the picture from

        Returns
        -------
        Boolean
            True if success else False
        """
        result = True

        # // try to load the picture into the buffered image from the file name
        result = load(fileName)

        # // show the picture in a picture frame
        self.show()

        return result

    def load(self, fileName):
        """Load picture from a file without throwing exceptions

        Parameters
        ----------
        fileName : string
            the name of the file to load the picture from

        Returns
        -------
        Boolean
            True if success else False
        """
        try:
            self.loadOrFail(fileName)
            return True
        except BaseException:
            print("There was an error trying to open " + fileName)
            mode = "RGB"
            size = (600, 200)
            self.image = PIL.Image.new(mode, size, (255,255,255))
            self.addMessage("Couldn't load " + fileName, 5, 100)
            return False

    def loadOrFail(self, fileName):
        """Load a picture from a file
            the name of the file to load the picture from
        """
        self.image = PIL.Image.open(fileName)
        self.filename = self.title = fileName


    def write(self, fileName):
        """Writes this picture to a file with the name fileName

        Parameters
        ----------
        fileName : string
            The name of the file that this picture will be written to
        Returns
        -------
        Boolean
            True if the file is written False if an IO error occurs
        """
        try :
            self.writeOrFail(fileName)
            return True
        except:
            print("There was an error trying to write " + fileName)
            return False

    def writeOrFail(self, fileName):
        """Write the contents of the picture to a file
 
        Parameters
        ----------
        fileName : string
            the name of the file to write the picture to
        """
        # get name and extension
        name, ext = os.path.splitext(fileName)
        imageType = None
 
        # if no extension, use JES default
        if ext == '':
            imageType = self.extension.replace('.', '')
            if imageType.lower() == 'jpg':
                imageType = 'jpeg'
            print('imageType = {}'.format(imageType))
 
        # write file
        self.image.save(fileName, format=imageType)

    def loadImage(self, fileName):
        """Load picture from a file without throwing exceptions

        This just calls load(fileName) and is included for compatibility
        with JES.

        Parameters
        ----------
        fileName : string
            the name of the file to load the picture from

        Returns
        -------
        Boolean
            True if success else False
        """    
        return self.load(fileName)

    def addMessage(self, message, xPos, yPos):
        """Adds text to the image
    
        message : string
            the message that will be drawn on the picture
        x : int
            the x-coordinate of the top left corner of the text
        y : int
            the y-coordinate of the top left corner of the text
        """
        # get a graphics context to use to draw on the buffered image
        col = Color(0,0,0)
        self.addText(col, xPos, yPos, message)

    def drawString(self, text, xPos, yPos):
        """Adds text to the image
    
        text : string
            the text that will be drawn on the picture
        x : int
            the x-coordinate of the top left corner of the text
        y : int
            the y-coordinate of the top left corner of the text
        """
        # get a graphics context to use to draw on the buffered image
        self.addMessage(text, xPos, yPos)
   
