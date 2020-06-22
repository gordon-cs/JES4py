
from PIL import Image, ImageDraw
from picture import Picture
import numpy as np
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
    # public void addLine(Color acolor, int x1, int y1, int x2, int y2) {
    #     Graphics g = this.getBufferedImage().getGraphics();
    #     g.setColor(acolor);
    #     g.drawLine(x1 - SimplePicture._PictureIndexOffset, y1 - SimplePicture._PictureIndexOffset, x2 - SimplePicture._PictureIndexOffset, y2 - SimplePicture._PictureIndexOffset);
    # }

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

    #     Method to draw the outline of a rectangle on a picture.
    #     @param acolor the color of the rectangle
    #     @param x the x-coordinate of the upper-left cornerof the rectangle
    #     @param y the y-coordinate of the upper-left corner of the rectangle
    #     @param w the width of the rectangle
    #     @param h the height of the rectangle
def addRect(pic, acolor, x, y, w, h):
    draw = ImageDraw.Draw(pic)
    shape = [x, y, x+w, y+h]
    draw.rectangle(shape, fill = None, outline = acolor) 
    return pic

#     Method to draw a solid rectangle on a picture.
#     @param acolor the color of the rectangle
#     @param x the x-coordinate of the upper-left corner of the rectangle
#     @param y the y-coordinate of the upper-left corner of the rectangle
#     @param w the width of the rectangle
#     @param h the height of the rectangle
def addRectFilled(pic, acolor, x, y, w, h):
    draw = ImageDraw.Draw(pic)
    shape = [x, y, x+w, y+h]
    draw.rectangle(shape, fill=acolor, outline = None) 
    return pic

#     Method to draw a solid oval on a picture.
#     @param acolor the color of the oval
#     @param x the x-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param y the y-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param w the width of the oval
#     @param h the height of the oval
def addOvalFilled(pic, acolor, x, y, w, h):
    draw = ImageDraw.Draw(pic)
    shape = [x, y, x+w, y+h]
    draw.ellipse(shape, fill = acolor, outline = None, width=1)
    return pic

#  Method to draw the outline of an oval on a picture.
#     @param acolor the color of the oval
#     @param x the x-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param y the y-coordinate of the upper-left corner of the bounding rectangle for the oval
#     @param w the width of the oval
#     @param h the height of the oval
def addOval(pic, acolor, x, y, w, h):
    draw = ImageDraw.Draw(pic)
    shape = [x, y, x+w, y+h]
    draw.ellipse(shape, fill = None, outline = acolor, width=1)
    return pic

#  Method to draw a solid arc on a picture
#     @param acolor the color of the arc
#     @param x the x-coordinate of the center of the arc
#     @param y the y-coordinate of the center of the arc
#     @param w the width of the arc
#     @param h the height of the arc
#     @param start the starting angle at which to draw the arc
#     @param angle the angle of the arc, relative to the start angle
def addArcFilled(pic, acolor, x, y, w, h, start, angle):
    draw = ImageDraw.Draw(pic)
    shape = [x, y, x+w, y+h]
    draw.pieslice(shape, start, angle,fill = acolor, outline=None, width=1)
    return pic

#  Method to draw the outline of an arc on a picture
#     @param acolor the color of the arc
#     @param x the x-coordinate of the center of the arc
#     @param y the y-coordinate of the center of the arc
#     @param w the width of the arc
#     @param h the height of the arc
#     @param start the starting angle at which to draw the arc
#     @param angle the angle of the arc, relative to the start angle
def addArc(pic, acolor, x, y, w, h, start, angle):
    draw = ImageDraw.Draw(pic)
    shape = [x, y, x+w, y+h]
    draw.arc(shape, start, angle, fill = acolor, width=1)
    return pic

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
def crop(pic, upperLeftX, upperLeftY, width, height):    
    pic.crop((upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height))
    return pic

 # end of class Picture, put all new methods before this