import os, sys
import wx
import atexit
import subprocess, tempfile
from subprocess import PIPE
import PIL.ImageDraw, PIL.Image
from jes4py import Config
from jes4py.PixelColor import Pixel, Color
from jes4py import FileChooser

class Picture:

    filename = None
    title = None
    extension = ".jpg"
    _PictureIndexOffset = 0
    tmpfilename = None
    process = None
    subprocessList = []

    def __init__(self, *args, **kwargs):
        """Initializer for Picture class
        """
        self.filename = self.title = 'None'
        if len(args) == 0:
            # no parameters, make 100x200 picture with white background
            self.image = PIL.Image.new("RGB", (200, 100), (255, 255, 255))
        elif len(args) == 1:
            if isinstance(args[0], str):
                self.filename = self.title = args[0]
                # Assume 'we've been passed a filename
                if not os.path.isfile(self.filename):
                    # File not found, try prepending media path
                    filepath = FileChooser.getMediaPath(self.filename)
                    if os.path.isfile(filepath):
                        self.filename = self.title = filepath
                try:
                    self.image = PIL.Image.open(self.filename)
                except:
                    self.image = PIL.Image.new("RGB", (600, 200))
                    draw = PIL.ImageDraw.Draw(self.image)
                    draw.text((0, 100), "Couldn't load " + self.filename)
            elif isinstance(args[0], Picture):
                # We've been passed a Picture object
                self.image = args[0].image.copy()
                self.filename = args[0].filename
                self.title = args[0].title
            elif isinstance(args[0], PIL.Image.Image):
                # We've been passed a PIL image object
                self.image = args[0]
                try:
                    self.filename = self.title = args[0].filename
                except AttributeError:
                    pass
        elif len(args) == 2 or len(args) == 3:
            # We've been passed width and height, and possibly a color
            size = (int(args[0]), int(args[1]))
            c = Color(255,255,255) if len(args) == 2 else args[2]
            self.image = PIL.Image.new("RGB", size, c.color)
        else:
            print("Could not construct Picture object")

    def __str__(self):
        """Return string representation of this picture

        Returns
        -------
        str
            representation of this picture
        """
        output = "Picture, filename {} height {} width {}".format(
            self.filename, self.image.height, self.image.width)
        return output

    def __repr__(self):
        """Return string representation of this picture

        Returns
        -------
        str
            representation of this picture
        """
        return self.__str__()

    def getExtension(self):
        """Return the filename extension for this picture

        Returns
        -------
        str
            the file extension for the picture (indicates the image file format)
        """
        return self.extension

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
        acolor : Color
            the color that outlines arc
        """
        if not isinstance(acolor, Color):
            print ("setAllPixelsToAColor(color): Input is not a color")
            raise ValueError
        self.image = PIL.Image.new("RGB", (self.getWidth(), self.getHeight()), acolor.getRGB())

    def getFileName(self):
        """Return picture file name

        Returns
        -------
        string
            name of file containing picture data
        """
        return self.filename

    def setFileName(self, filename):
        """Set picture file name

        Parameters
        ----------
        filename : string
            filename to assign to this picture
        """
        self.filename = filename

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

    def getImage(self):
        """Return the PIL Image associated with this picture

        Returns
        -------
        PIL.Image.Image
            the PIL Image associated with this picture
        """
        return self.image

    def setImage(self, image):
        """Sets the PIL Image associated with this picture

        Parameters
        ----------
        image : PIL.Image.Image
            the PIL Image to associate with this picture
        """
        self.image = image

    def getBasicPixel(self, x, y):
        """Return the pixel at specified coordinates as a tuple.

        Parameters
        ----------
        x, y : int
            the coordinates of the pixel

        Returns
        -------
        tuple of int
            the color of the pixel at position (x,y) as a tuple
        """
        return self.getPixel(x,y).getColor().getRGB()

    def setBasicPixel(self, x, y, rgb):
        """Sets the pixel at specified coordinates to a color based on rgb(tuple)

        Parameters
        ----------
        x, y : int
            the coordinates of the pixel
        rgb : tuple of int
            the color the pixel will be set to
        """
        col = Color(rgb[0], rgb[1], rgb[2])
        self.getPixel(x,y).setColor(col)

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

    def addText(self, acolor, x, y, string):
        """Add a line of text to the picture
    
        Parameters
        ----------
        acolor : Color
            the color of the text
        x : int
            the x-coordinate of the top left corner of the text
        y : int
            the y-coordinate of the top left corner of the text
        string : str
            the text that will be drawn on the picture
        """
        draw = PIL.ImageDraw.Draw(self.image)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        # font = ImageFont.truetype("sans-serif.ttf", 16)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((x, y), string, acolor.getRGB())

    def addTextWithStyle(self, acolor, x, y, string, style):
        """Add text to a picture withe a particular font style

        Parameters
        ----------
        acolor : Color
            the color of the text
        x : int
            the x-coordinate of the top left corner of the text
        y : int
            the y-coordinate of the top left corner of the text
        string : str
            the text that will be drawn on the picture
        style : ???
            the font style to be used
        """
    #    draw = PIL.ImageDraw.Draw(self.image)
    #    # font = ImageFont.truetype(<font-file>, <font-size>)
    #    # font = ImageFont.truetype("sans-serif.ttf", 16)
    #    # draw.text((x, y),"Sample Text",(r,g,b))
    #    draw.text((x, y), string, acolor.getRGB())
        print("This function is not yet implemented.")

    def addRect(self, acolor, x, y, w, h):
        """Draw the outline of a rectangle on this picture
    
        acolor : Color
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
    
        acolor : Color
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
    
        acolor : Color
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
    
        acolor : Color
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
    
        acolor : Color
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
    
        acolor : Color
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
        fileName : str
            the name of the file to load the picture from

        Returns
        -------
        bool
            True if success else False
        """
        result = True

        # try to load the picture into the buffered image from the file name
        result = self.load(fileName)

        # show the picture in a picture frame
        self.show()

        return result

    def load(self, fileName):
        """Load picture from a file without throwing exceptions

        Parameters
        ----------
        fileName : str
            the name of the file to load the picture from

        Returns
        -------
        bool
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

        Parameters
        ----------
        fileName : str
            the name of the file to load the picture from
        """
        self.image = PIL.Image.open(fileName) #.convert('RGB')
        self.filename = self.title = fileName


    def write(self, fileName):
        """Writes this picture to a file with the name fileName

        Parameters
        ----------
        fileName : str
            The name of the file that this picture will be written to

        Returns
        -------
        bool
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
        fileName : str
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

    def setMediaPath(self, directory):
        """Method to set the directory for the media

        Parameters
        ----------
        directory : str
            the directory to use for the media path

        """
        FileChooser.setMediaPath(directory)

    def getMediaPath(self, fileName):
        """Method to get the directory for the media

        Parameters
        ----------
        fileName : str
            the fileName the base file name to use

        Returns
        -------
        str
            the full path name by appending the file name to the media directory
        """
        return FileChooser.getMediaPath(fileName)

    def loadImage(self, fileName):
        """Load picture from a file without throwing exceptions

        This just calls load(fileName) and is included for compatibility
        with JES.

        Parameters
        ----------
        fileName : str
            the name of the file to load the picture from

        Returns
        -------
        bool
            True if success else False
        """    
        return self.load(fileName)

    def addMessage(self, message, xPos, yPos):
        """Adds text to the image
    
        message : str
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
    
        text : str
            the text that will be drawn on the picture
        x : int
            the x-coordinate of the top left corner of the text
        y : int
            the y-coordinate of the top left corner of the text
        """
        # get a graphics context to use to draw on the buffered image
        self.addMessage(text, xPos, yPos)

#----------------------------------------------------------------------------
# WX specific methods
#----------------------------------------------------------------------------

    def getWxImage(self, copy_alpha=True):
        """Return a wx.Image version of this image

        Parameters
        ----------
        copy_alpha : bool
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

    def __saveInTempFile(self):
        """Create temporary image file

        Returns
        -------
        string
            path to temporary image file
        """
        filename = os.path.join(tempfile.gettempdir(),
            "jes4py_" + next(tempfile._get_candidate_names()) + self.extension)
        #tempdir = tempfile.mkdtemp()
        #filename = os.path.join(tempdir, "showimage" + self.extension)
        #os.mkdir(tempdir)
        self.write(filename)
        return filename

        # Run show script
    def __runScript(self, script, *argv):
        """Run a Python script in a subprocess

        Parameters
        ----------
        script : str
            the script to run; must be in the jes4py directory
        *argv : list
            parameters to pass to script on command line

        Returns
        -------
        Popen instance
        """
        # Start subprocess using current Python intepreter to run a script
        scriptpath = os.path.join(Config.getConfigVal("CONFIG_JES4PY_PATH"), script)
        proc = subprocess.Popen([sys.executable, scriptpath] + list(argv), stdin=PIPE)

        # Register atexit handler if this is the first subprocess
        if len(self.subprocessList) == 0:
            atexit.register(self._stopAllSubprocesses)

        # Record the process and return

        self.subprocessList.append(proc)
        return proc

    def _stopAllSubprocesses(self):
        """Close windows (i.e. terminate subprocess)
        """
        for proc in self.subprocessList:
            try:
                proc.stdin.write(b'exit\n')
                proc.stdin.flush()
                proc.stdin.close()
                proc.terminate()
                proc.wait(timeout=0.2)
            except: # BrokenPipeError, OSError:
                pass

    def show(self):
        """Show a picture using stand-alone Python script
        """
        if self.process is None:
            # no show process for this picture, start one
            self.tmpfilename = self.__saveInTempFile()
            self.process = self.__runScript('show.py', self.tmpfilename, self.title)
        elif self.process.poll() is not None:
            # there was a show process, but it's not running, start a new one
            if self.tmpfilename is None or not os.path.isfile(self.tmpfilename):
                # temporary image file does not exist, make one
                self.tmpfilename = self.__saveInTempFile()
            self.process = self.__runScript('show.py', self.tmpfilename, self.title)
        else:
            # show process already running, repaint the picture
            # NOTE: this is different than JES.  JES raises the picture
            # to the top so it is visible.
            self.repaint()

    def repaint(self):
        """Reshow a picture using stand-alone Python script
        """
        if (self.process is not None) and self.process.poll() is None:
            # subprocess seems to be running, ask it to update image
            try:
                self.write(self.tmpfilename) # update temp image file
                msg = self.tmpfilename + ' ' + self.title + '\n'
                self.process.stdin.write(msg.encode('utf8'))
                self.process.stdin.flush()
            except: # BrokenPipeError:
                # something went wrong, reset and call show
                self.process = None
                self.tmpfilename = None
                self.show()
        else:
            # subprocess is not running, start a new one
            self.process = None
            self.tmpfilename = None
            self.show()

    def pictureTool(self):
        """Explore a picture using a stand-alone Python script
        """
        filename = self.__saveInTempFile()
        self.__runScript('pictureTool.py', filename, self.title)
