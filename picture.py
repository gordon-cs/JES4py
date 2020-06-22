from PIL import Image
import numpy as np
class Picture:

    def __init__(self, picture, filename):
        self.title = "None"
        self.fileName = filename
        self.extension = "jpg"
        self.width = picture.width
        self.height = picture.height
        self.picture = picture

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def __str__(self):
        output = "Picture, filename {} height {} width {}".format(self.fileName, self.picture.height, self.picture.width)
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
        pixels = np.asarray(self.picture)
        # pixels = np.reshape(pixels, self.height, self.width)
        return pixels

    def getImage(self):
        return self.picture

    def setImage(self, pic):
        self.picture = pic
        self.width = pic.width
        self.height = pic.height

    def getWidth(self):
        return self.picture.width

    def getHeight(self):
        return self.picture.height