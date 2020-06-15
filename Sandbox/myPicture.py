from PIL import Image
class myPicture:

    def __init__(self, picture):
        self.title = "None"
        self.fileName = "None"
        self.extension = "jpg"
        self.width = picture.width
        self.height = picture.height
        self.picture = picture

    #  * Method to return a string with information about this picture.
    #  * @return a string with information about the picture such as fileName,
    #  * height and width.
    #  */
    def toString(self):
        output = "Picture, filename " + getFileName() + " height " + self.picture.height + " width " + self.picture.width
        return output

    def getFileName(self):
        return self.fileName

    def setFileName(self, name):
        self.fileName = name

    def setTitle(self, name):
        self.title = name

    def getTitle(self):
        return self.title

    def getImage(self):
        return self.picture