from PIL import Image
from Pixel import Pixel
class Picture:

    def __init__(self, image, filename):
        self.title = "None"
        self.fileName = filename
        self.extension = "jpg"
        self.width = image.width
        self.height = image.height
        self.image = image
        self.pixels = image.getdata()

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def __str__(self):
        output = "Picture, filename {} height {} width {}".format(self.fileName, self.image.height, self.image.width)
        return output

    def getFileName(self):
        return self.fileName

    def setFileName(self, name):
        self.fileName = name

    def setTitle(self, name):
        self.title = name

    def getTitle(self):
        return self.title

    def getPixels(self):
        return self.pixels

    def getPixel(self, x, y): 
        imageList = self.getPixels()
        val = imageList[x+(y*self.width)]
        pix = Pixel(self.image, x, y)
        return pix

    def getImage(self):
        return self.image

    def setImage(self, pic):
        self.image = pic
        self.width = pic.width
        self.height = pic.height

    def getWidth(self):
        return self.image.width

    def getHeight(self):
        return self.image.height

