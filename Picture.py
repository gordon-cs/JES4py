import wx
import os
import PIL.ImageDraw
from Pixel import Pixel

class Picture:

    def __init__(self, image):
        self.title = image.filename
        self.fileName = image.filename
        #self.width = image.width
        #self.height = image.height
        self.image = image

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def __str__(self):
        """Return string representation of this picture

        Returns
        -------
        str
            representation of this picture
        """
        output = "Picture, filename {} height {} width {}".format(
            self.fileName, self.height, self.width)
        return output

    def getFileName(self):
        """Return picture file name

        Returns
        -------
        str
            name of file containing picture data
        """
        return self.fileName

    def setFileName(self, filename):
        """Set picture file name

        Parameters
        ----------
        filename : str
            filename to assign to this picture
        """
        self.fileName = filename

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
        for y in range(self.height):
            for x in range(self.width):
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
        #self.width = image.width
        #self.height = image.height

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
    # public void addText(Color acolor, int x, int y, String string) {
    #     Graphics g = this.getBufferedImage().getGraphics();
    #     g.setColor(acolor);
    #     g.drawString(string, x - SimplePicture._PictureIndexOffset, y - SimplePicture._PictureIndexOffset);
    # }

    #  * Method to add text to a picture withe a particular font style
    #  *    @param acolor the color of the text
    #  *    @param x the x-coordinate of the bottom left corner of the text
    #  *    @param y the y-coordinate of the bottom left corner of the text
    #  *    @param string the text to be added to the picture
    #  *    @param style the font style to be used
    # public void addTextWithStyle(Color acolor, int x, int y, String string, Font style) {
    #     Graphics g = this.getBufferedImage().getGraphics();
    #     g.setColor(acolor);
    #     g.setFont(style);
    #     g.drawString(string, x - SimplePicture._PictureIndexOffset, y - SimplePicture._PictureIndexOffset);
    # }

    def addRect(self, acolor, x, y, w, h):
        """Draw the outline of a rectangle on this picture
    
        Parameters
        ----------
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
    
        Parameters
        ----------
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
    
        Parameters
        ----------
        acolor : Color
            the color that the oval is filled with
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
    
        Parameters
        ----------
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
    
        Parameters
        ----------
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
    
        Parameters
        ----------
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

    #  Copies all the pixels from this picture to the destination picture,
    #  starting with the specified upper-left corner.  If this picture
    #  will not fit in the destination starting at the upper-left corner,
    #  then only the pixels that will fit are copied.  If the specified
    #  upper-left corner is not in the bounds of the destination picture,
    #  no pixels are copied.
    #  @param dest the picture which to copy into
    #  @param upperLeftX the x-coord for the upper-left corner
    #  @param upperLeftY the y-coord for the upper-left corner
    # public void copyInto(Picture dest, int upperLeftX, int upperLeftY) {
    #     #  Determine the actual dimensions to copy; might be less than
    #     #  dimensions of this picture if there is not enough space in the
    #     #  destination picture.
    #     int width = this.getWidth();
    #     int widthAvailable = dest.getWidth() - upperLeftX;
    #     if (widthAvailable < width) {
    #         width = widthAvailable;
    #     }
    #     int height = this.getHeight();
    #     int heightAvailable = dest.getHeight() - upperLeftY;
    #     if (heightAvailable < height) {
    #         height = heightAvailable;
    #     }

    #     #  Copy pixel values from this picture to the destination
    #     #   (Should have been implemented with the 7-parameter
    #     #    getRGB/setRGB methods from BufferedImage?)
    #     for (int x = 0; x < width; x++)
    #         for (int y = 0; y < height; y++) {
    #             dest.setBasicPixel(upperLeftX + x, upperLeftY + y, this.getBasicPixel(x, y));
    #         }

    # }

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
            the cropped copy of the original picture
        """
        pic = self
        pic.crop((upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height))
        return pic

    def show(self):
        """Display a PIL Image using a WX App

        Parameters
        ----------
        image : PIL.Image
            the image to display
        """
        class mainWindow(wx.Frame):
            """Frame class that display an image"""
            def __init__(self, image, parent=None, id=-1,
                    pos=wx.DefaultPosition, title=None):
                """Create a frame instance and display image"""
                temp = image.ConvertToBitmap()
                size = temp.GetWidth(), temp.GetHeight()
                wx.Frame.__init__(self, parent, id, pos=pos, title=title, size=size)
                self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

        class ShowImage(wx.App):
            """Application class"""
            def __init__(self, image=None, title=None, *args, **kwargs):
                self.image = image
                self.title = title
                wx.App.__init__(self, *args, **kwargs)

            def OnInit(self):
                self.frame = mainWindow(image=self.image, title=self.title)
                self.frame.Show()
                return True

        # Need wx app to run in separate thread or process.  It seems
        # that starting a wxPython GUI in a worker thread is not a good idea
        # so the easiest thing to do is just fork a new process.
        pid = os.fork()
        if pid == 0:
            wxImage = self.getWxImage()
            app = ShowImage(image=wxImage, title=self.fileName)
            app.MainLoop()
            exit(0)

 # end of class Picture, put all new methods before this
