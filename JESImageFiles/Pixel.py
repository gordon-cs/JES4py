from PIL import Image
class Pixel:

    def __init__(self, picture, x, y):
        self.picture = picture
        self.x = x
        self.y = y

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def __str__(self):
        output = "Picture, filename {} height {} width {}".format(self.fileName, self.picture.height, self.picture.width)
        return output

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setTitle(self, name):
        self.title = name

    def getTitle(self):
        return self.title

    def getPixels(self):
        pixels = np.asarray(self.picture)
        #pixels = np.reshape(self.height, self.width)
        return pixels

    def getImage(self):
        return self.picture

    def setImage(self, pic):
        self.picture = pic
        self.width = pic.width
        self.height = pic.height
