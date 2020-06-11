from PIL import Image, ImageDraw

def show(picture):
    picture.show()

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

def getWidth(picture):
    return picture.width

def getHeight(picture):
    return picture.height

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
def addRect(picture, upperLeftX, upperLeftY, width, height):
    draw = ImageDraw.Draw(picture)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = None, outline = None) 

#adds a rectangle to the image(image) with the outline color as (color)
def addRect(picture, upperLeftX, upperLeftY, width, height, color):
    draw = ImageDraw.Draw(picture)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = None, outline = color) 

#adds a rectangle to the image(image) that is filled in with black
def addFilledRect(picture, upperLeftX, upperLeftY, width, height):
    draw = ImageDraw.Draw(picture)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = (0, 0, 0), outline = None)

#adds a rectangle to the image(image) that is filled in with (color)
def addFilledRect(picture, upperLeftX, upperLeftY, width, height, color):
    draw = ImageDraw.Draw(picture)
    shape = [upperLeftX, upperLeftY, upperLeftX+width, upperLeftY+height]
    draw.rectangle(shape, fill = color, outline = None)

def addArc(picture, startX, startY, width, height, start, angle):
    draw = ImageDraw.Draw(picture)
    shape = [startX, startY, startX+width, startY+height]
    draw.ellipse(shape, fill = None, outline = (0, 0, 0), width=1)
    
def addArc(picture, startX, startY, width, height, start, angle, color):
    draw = ImageDraw.Draw(picture)
    shape = [startX, startY, startX+width, startY+height]
    draw.ellipse(shape, fill = None, outline = color, width=1)

def addArcFilled(picture, startX, startY, width, height, start, angle):
    draw = ImageDraw.Draw(picture)
    shape = [startX, startY, startX+width, startY+height]
    draw.arc(shape, start, angle, fill = (0, 0, 0 ), outline = (0, 0, 0), width=1)
    
def addArcFilled(picture, startX, startY, width, height, start, angle, color):
    draw = ImageDraw.Draw(picture)
    shape = [startX, startY, startX+width, startY+height]
    draw.arc(shape, start, angle, fill = color, outline = ( 0, 0, 0), width=1)

def addOvalFilled(picture, startX, startY, width, height):
    draw = ImageDraw.Draw(picture)
    shape = [startX, startY, startX+width, startY+height]
    draw.ellipse(shape, fill = (0, 0, 0 ), outline = (0, 0, 0), width=1)
    
def addOvalFilled(picture, startX, startY, width, height, color):
    draw = ImageDraw.Draw(picture)
    shape = [startX, startY, startX+width, startY+height]
    draw.ellipse(shape, fill = color, outline = ( 0, 0, 0), width=1)

