#from PIL import Image, ImageDraw
import PIL.ImageDraw
from Pixel import Pixel

class Picture:

    def __init__(self, image):
        self.title = ""
        self.fileName = ""
        self.width = image.width
        self.height = image.height
        self.image = image
        #print("in constructor: ", image.__dict__.keys())
        #print("in constructor: filename = ", image.filename)
        #self.fileName = image.filename

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def __str__(self):
        output = "Picture, filename {} height {} width {}".format(pic, self.height, self.width)
        return output

    def getFileName(self):
        return self.fileName

    def setFileName(self, name):
        self.fileName = name

    def getTitle(self):
        return self.title
        
    def setTitle(self, name):
        self.title = name

    def getPixels(self):
        return self.image.getdata()

    def getPixel(self, x, y): 
        imageList = self.getPixels()
        val = imageList[x+(y*self.width)]
        pix = Pixel(self.image, x, y)
        return pix

    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image
        self.width = image.width
        self.height = image.height

    def getWidth(self):
        return self.image.width

    def getHeight(self):
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

    #  * Method to draw a line between two points on a picture
    #  * @param acolor the color of the line
    #  * @param x1 the x-coordinate of the first point
    #  * @param y1 the y-coordinate of the first point
    #  * @param x2 the x-coordinate of the second point
    #  * @param y2 the y-coordinate of the second point
    def addLine(self, acolor, x1, y1, x2, y2):
        """Method to draw a line on a picture.
    
        acolor : instance of Color class
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
        """Method to draw the outline of a rectangle on a picture.
    
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

#     Method to draw a solid rectangle on a picture.
#     @param acolor the color of the rectangle
#     @param x the x-coordinate of the upper-left corner of the rectangle
#     @param y the y-coordinate of the upper-left corner of the rectangle
#     @param w the width of the rectangle
#     @param h the height of the rectangle
    def addRectFilled(self, acolor, x, y, w, h):
        """Method to draw a filled rectangle on a picture.
    
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

#     Method to draw a solid oval on a picture.
#     @param acolor the color of the oval
#     @param x the x-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param y the y-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param w the width of the oval
#     @param h the height of the oval
    def addOvalFilled(self, acolor, x, y, w, h):
        """Method to draw a filled oval on a picture.
    
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
        draw.ellipse(shape, fill = color, outline = color, width=1)

#  Method to draw the outline of an oval on a picture.
#     @param acolor the color of the oval
#     @param x the x-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param y the y-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param w the width of the oval
#     @param h the height of the oval
    def addOval(self, acolor, x, y, w, h):
        """Method to draw the outline of an oval on a picture.
    
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
        draw.ellipse(shape, fill = None, outline = acolor.getRGB(), width = 1)

#  Method to draw a solid arc on a picture
#     @param acolor the color of the arc
#     @param x the x-coordinate of the center of the arc
#     @param y the y-coordinate of the center of the arc
#     @param w the width of the arc
#     @param h the height of the arc
#     @param start the starting angle at which to draw the arc
#     @param angle the angle of the arc, relative to the start angle
    def addArcFilled(self, acolor, x, y, w, h, start, angle):
        """Method to draw a filled in arc on a picture.
    
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
        draw.pieslice(shape, start, end, fill = color, outline = color, width = 1)

#  Method to draw the outline of an arc on a picture
#     @param acolor the color of the arc
#     @param x the x-coordinate of the center of the arc
#     @param y the y-coordinate of the center of the arc
#     @param w the width of the arc
#     @param h the height of the arc
#     @param start the starting angle at which to draw the arc
#     @param angle the angle of the arc, relative to the start angle
    def addArc(self, acolor, x, y, w, h, start, angle):
        """Method to draw the outline of an arc on a picture.
    
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
        draw.arc(shape, start, end, fill = acolor.getRGB(), width = 1)

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

    #  Returns a cropped version of this picture: copies the pixels in
    #  it starting at the specified upper-left corner and taking as
    #  many pixels as specified by <code>width</code> and <code>height</code>.
    #  The final cropped picture may be smaller than indicated by the
    #  parameters if the cropping area as specified would go beyond the
    #  bounds of this picture.  The cropping area will be <code>0 x 0</code>
    #  if the specified upper-left corner is not in the bounds of the
    #  destination picture.
    #  @param upperLeftX the x-coord of the upper-left corner
    #  @param upperLeftY the y-coord of the upper-left corner
    #  @param width the desired width of the cropped area
    #  @param height the desired height of the cropped area
    #  @return the new cropped picture
    def crop(self, upperLeftX, upperLeftY, width, height):
        """Method to draw the outline of an arc on a picture.
    
        upperLeftX : int
            the x-coord of the upper-left corner new cropped image
        upperLeftY : int
            the y-coord of the upper-left corner new cropped image
        width : int
            the desired width of the cropped picture
        height : int
            the desired height of the cropped picture
        """
        pic = self
        pic.crop((upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height))
        return pic

 # end of class Picture, put all new methods before this