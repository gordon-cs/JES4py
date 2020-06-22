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
        output = "Pixel: picture {}, x {} y {} ".format(self.picture.getTitle(), self.picture.height, self.picture.width)
        return output

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPicture(self):
        return self.picture

    def getRed(self):
        col = self.getColor()
        return col[0]

    def getGreen(self):
        col = self.getColor()
        return col[1]

    def getBlue(self):
        col = self.getColor()
        return col[2]

    def setRed(self, value):
        self.color[0] = value

    def setGreen(self, value):
        self.color[1] = value

    def setBlue(self, value):
        self.color[2] = value

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color