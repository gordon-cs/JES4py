# This is a text-only replacement for JES facilities needed for CPS121 Project 2
# Author: Russell C. Bjork
# Last revised: March 19, 2020

import time
useANSIColors = True

# Symbolic constants for colors. Depending on useANSIColors either ANSI colors or
# black and white only is used
 
if useANSIColors:
  white = ' '
  red = u'\u001b[31mr'
  green =  u'\u001b[32mg'
  black =  u'\u001b[30mb'
  reset = u'\u001b[0m'
else:
  white = ' '
  red = 'r'
  green = 'g'
  black = 'b'
  reset = ''
  
# Text-oriented replacement for the Pixel class of JES
class Pixel:
  # Constructor - parameters x and y coordinates and color of pixel
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def getColor(self):
    return self.color
  def setColor(self, color):
    self.color = color
    
# Text-oriented replacement for the Picture class of JES
class Picture:
  # Constructor - parameters width and height in pixels; initial color of each pixel
  def __init__(self, width, height, color):
    self.width = width
    self.height = height
    self.row = []
    for y in range(0, height):
      col = []
      for x in range(0, width):
        col.append(Pixel(x, y, color))
      self.row.append(col)
  # Get the width of the picture
  def getWidth(self):
    return self.width
  # Get the height of the picture
  def getHeight(self):
    return self.height
  # Get the pixel at a given position
  def getPixelAt(self, x, y):
    return self.row[y][x]
    
# Test to see whether a variable holds a value of a certain type
# Throw an exception if it is not
# Names of variable and type are strings used in forming exception
def typeTest(variable, typ, variableName, typName):
  if not isinstance(variable, typ):
    raise TypeError(variableName + " is not a " + typName)

# Test to see whether a value lies in a certain range
def rangeTest(value, range):
  if not value in range:
    minimum = range[0]
    if (value < minimum):
      raise ValueError(str(value) + " is less than " + str(minimum))
    else:
      raise ValueError(str(value) + " is greater than " + str(range[-1]))


# Text-oriented replacements for JES functions - parameters same meanings as in JES
def getColor(pixel):
  typeTest(pixel, Pixel, "pixel", "Pixel")
  return pixel.getColor()
def setColor(pixel, color):
  typeTest(pixel, Pixel, "pixel", "Pixel")
  pixel.setColor(color)
def getX(pixel):
  typeTest(pixel, Pixel, "pixel", "Pixel")
  return pixel.getX()
def getY(pixel):
  typeTest(pixel, Pixel, "pixel", "Pixel")
  return pixel.getY() 
def makeEmptyPicture(width, height, color = white):
  return Picture(width, height, color)
def getWidth(picture):
  typeTest(picture, Picture, "picture", "Picture")
  return picture.getWidth()
def getHeight(picture):
  typeTest(picture, Picture, "picture", "Picture")
  return picture.getHeight()
def getPixel(picture, x, y):
  typeTest(picture, Picture, "picture", "Picture")
  rangeTest(x, range(0, getWidth(picture)))
  rangeTest(y, range(0, getHeight(picture)))
  return picture.getPixelAt(x, y)
def getPixelAt(picture, x, y):
  typeTest(picture, Picture, "picture", "Picture")
  rangeTest(x, range(0, getWidth(picture)))
  rangeTest(y, range(0, getHeight(picture)))
  return picture.getPixelAt(x, y)
def getPixels(picture):
  typeTest(picture, Picture, "picture", "Picture")
  result = []
  for y in range(0, picture.getHeight()):
    for x in range(0, picture.getWidth()):
      result.append(picture.getPixelAt(x, y))
  return result
def duplicatePicture(picture):
  typeTest(picture, Picture, "picture", "Picture")
  result = makeEmptyPicture(picture.getWidth(), picture.getHeight())
  for x in range(0, picture.getWidth()):
    for y in range(0, picture.getHeight()):
      pixel = picture.getPixelAt(x, y)
      resultPixel = result.getPixelAt(x, y)
      resultPixel.setColor(pixel.getColor())
  return result
def show(picture):
  typeTest(picture, Picture, "picture", "Picture")
  width = getWidth(picture)
  height = getHeight(picture)
  for row in range(0, height):
    # , at end means don't go to new line
    for col in range(0, width):
      print picture.getPixelAt(col, row).getColor(),
    print
  print reset
def repaint(picture):
  # Same as show in this case
  show(picture)
  time.sleep(0.3)
      


    