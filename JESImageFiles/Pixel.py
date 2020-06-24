from PIL import Image
class Pixel:

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        #self.color = color

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def __str__(self):
        output = "Pixel: picture {}, x: {} y: {} color:{}".format(self.image, self.x, self.y, self.image.getpixel((self.x,self.y)))
        return output

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImage(self):
        return self.image

    def getRed(self):
        col = self.image.getpixel((self.x,self.y))
        return col[0]

    def getGreen(self):
        col = self.image.getpixel((self.x,self.y))
        return col[1]

    def getBlue(self):
        col = self.image.getpixel((self.x,self.y))
        return col[2]

    def setRed(self, value):
        col = self.image.getpixel((self.x,self.y))
        self.image.putpixel((self.x, self.y),(value, col[1], col[2]))

    def setGreen(self, value):
        col = self.image.getpixel((self.x,self.y))
        self.image.putpixel((self.x, self.y), (col[0], value, col[2]))

    def setBlue(self, value):
        col = self.image.getpixel((self.x,self.y))
        self.image.putpixel((self.x, self.y), (col[0], col[1], value))

    def getColor(self):
        return self.image.getpixel((self.x,self.y))

    def setColor(self, color):
        self.image.putpixel((self.x, self.y), color)