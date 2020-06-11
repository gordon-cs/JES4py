from PIL import Image, ImageDraw

def show(image):
    image.show()

#width and height must be ints
def makeEmptyPicture(width, height):
    mode = "RGB"
    size = (width, height)
    color = (255,255,255)
    return Image.new(mode, size, color)

#width and height must be ints. Format for color is RGB.
#  An example color would be (255,0,0) which is RED.
def makeEmptyPicture(width, height, color):
    mode = "RGB"
    size = (width, height)
    return Image.new(mode, size, color)

#makeColor w/ 3 parameters (red, blue and green)
def makeColor(redValue, greenValue, blueValue):
    return (redValue, greenValue, blueValue)

#makeColor w/ 2 parameters (red and blue)
def makeColor(redValue, greenValue):
    return (redValue, greenValue, 0)

#makeColor w/ 1 parameters (red)
def makeColor(redValue):
    return (redValue, 0, 0)

#adds a rectangle to the image named (image)
def addRect(image, upperLeftX, upperLeftY, width, height):
    draw = ImageDraw.Draw(image)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = None, outline = None) 

#adds a rectangle to the image(image) with the outline color as (color)
def addRect(image, upperLeftX, upperLeftY, width, height, color):
    draw = ImageDraw.Draw(image)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = None, outline = color) 

#adds a rectangle to the image(image) that is filled in with black
def addFilledRect(image, upperLeftX, upperLeftY, width, height):
    draw = ImageDraw.Draw(image)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = (0, 0, 0), outline = None)

#adds a rectangle to the image(image) that is filled in with (color)
def addFilledRect(image, upperLeftX, upperLeftY, width, height, color):
    draw = ImageDraw.Draw(image)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = color, outline = None)