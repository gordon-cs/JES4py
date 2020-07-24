# Gahngnin Kim
# CPS 121, Project 1

# Set the default folder to find input images 
setMediaPath("\Users\glgnk\OneDrive - qcc.mass.edu\Gordon\Fall 2018\Intro to Programming\Work_folder\Project\kim1")

def copyInto(dest, x, y, source):
    """Copy source picture into part of dest picture.

    Place the top left corner at (x, y) in dest.  If any
    part of source would be copied to a non-existent
    location in dest, that part is not copied.

    dest - destination picture, part of which will be
        replaced by a copy of source
    x, y - location (in dest) to which the upper left
        corner of source will be copied
    source - picture which will be copied into dest
    (No return value.  dest is modified.)
    """
    targetX = x
    for sourceX in range(getWidth(source)):
        targetY = y
        for sourceY in range(getHeight(source)):
            pixelColor = getColor(getPixel(source, sourceX, sourceY))
            setColor(getPixel(dest, targetX, targetY), pixelColor)
            targetY = targetY + 1
        targetX = targetX + 1
        
def copyPicSmaller(picture,srcX,srcY,ratio):
  # Set up the source and target pictures
  src=picture
  canvas=makeEmptyPicture(int(srcX/ratio),int(srcY/ratio))
  # Now, do the actual copying
  sourceX = 0
  for targetX in range(0,int(srcX/ratio)):
    sourceY = 0
    for targetY in range(0,int(srcY/ratio)):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY), color)
      sourceY = sourceY + ratio
    sourceX = sourceX + ratio
  return canvas

def createCollage():
    """Creates a collage according to the requirements for project 1.

    Returns the new collage.
    """
    collage = makeEmptyPicture(700, 950)
    catPortrait = makePicture("cat_portrait_white.jpg") # 350 x 328
    grayScale(catPortrait)
    copyInto(collage, 0, 0, copyPicSmaller(catPortrait, 350, 328, 2)) # scaling the picture down and place it top left
    posterize(catPortrait) # posterize the picture
    copyInto(collage, 175, 0, (copyPicSmaller(catPortrait, 350, 328, 2)))
    catPortrait = makePicture("cat_portrait_white.jpg") # 350 x 328
    sepiaTint(catPortrait) # tint the picture to look old
    copyInto(collage, 0, 163, copyPicSmaller(catPortrait, 350, 328, 2))
    catPortrait = makePicture("cat_portrait_white.jpg") # 350 x 328
    edgedetect(catPortrait) # convert the picture to a "line drawing"
    copyInto(collage, 175, 163, copyPicSmaller(catPortrait, 350, 328, 2))
    tiger =  makePicture("tiger.jpg") # 349 x 271
    copyInto(collage, 350, 0, pixelIt(tiger, 5)) # pixelate the image and place it top right
    roadCat = makePicture("roadcat.jpg") # 320 x 213
    catInTheField = makePicture("cat_landscape.jpg") # 700 x 467
    rightHalfBright(catInTheField) # make half of the picture brighter
    mirrorVertical(roadCat) # mirror the picture vertically
    copyInto(collage,0, 327, blendPictures(roadCat, catInTheField, 700, 468)) # blend two pictures
    catLookingUp = makePicture("catlookingup.jpg") # 175 x 117
    blur(catLookingUp) # blur the picture
    posterizeBKWB(catLookingUp) # posterize to black, white, and blue
    copyInto(collage, 0, 832, catLookingUp)
    catLookingUp = makePicture("catlookingup.jpg") # 175 x 117
    negative(catLookingUp) # negate the picture
    copyInto(collage, 175, 832, catLookingUp)
    copyInto(collage, 350, 832, flipRight(catLookingUp))
    catLookingUp = makePicture("catlookingup.jpg") # 175 x 117
    posterizeBKWR(catLookingUp) # posterize to black, white, and red
    copyInto(collage, 525, 832, flipRight(catLookingUp))
    addABlackBox(collage, 350, 270, 350, 57) # add a rectangular box to fill the empty space
    return collage

def crop(source, x, y, width, height):
    """Crop a picture by making a copy of part of it.

    source - original picture, which is not changed
    x, y - starting location, in source, of part to copy 
             (upper left corner, as pixel coordinates)
    width, height - dimensions of part of source to copy
             (expressed in pixels)

    Return a new picture with a copy of the specified part.
    """
    # Set up the source and target pictures
    src = source
    result = makeEmptyPicture(width, height)
    # Now, do the actual copying
    targetX = 0
    for sourceX in range(104,267):
      targetY = 0
      for sourceY in range(114,422):
        color = getColor(getPixel(src,sourceX,sourceY))
        setColor(getPixel(canvas,targetX,targetY), color)
        targetY = targetY + 1
      targetX = targetX + 1
    return result

def rotateRight(source):
    """Rotate source image right 90 degrees.
    Create a new target image of the correct shape.
    Return the newly created (and rotated) image.
    """
    canvas = makeEmptyPicture(getHeight(src),getWidth(src))
    targetX = 0
    width = getWidth(src)
    for sourceX in range(0,getHeight(src)):
      targetY = 0
      for sourceY in range(0,getWidth(src)):
        color = getColor(getPixel(src,sourceX,sourceY))
        # Change is here
        setColor(getPixel(canvas,targetY,width - targetX - 1), color)
        targetY = targetY + 1
        targetX = targetX + 1
    return canvas

def posterize(picture):
  #posterize the picture
  #loop through the pixels
  for p in getPixels(picture):
    #get the RGB values
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    
    #check and set red values
    if(red < 64):
      setRed(p, 31)
    elif(red < 128):
      setRed(p, 95)
    elif(red < 192):
      setRed(p, 159)
    elif(red < 256):
      setRed(p, 223)
    
    #check and set green values
    if(green < 64):
      setGreen(p, 31)
    elif(green < 128):
      setGreen(p, 95)
    elif(green < 192):
      setGreen(p, 159)
    elif(green < 256):
      setGreen(p, 223)
    
    #check and set blue values
    if(blue < 64):
      setBlue(p, 31)
    elif(blue < 128):
      setBlue(p, 95)
    elif(blue < 192):
      setBlue(p, 159)
    elif(blue < 256):
      setBlue(p, 223)
  return picture

def posterizeBKWB(pic):
  # posterize to black, white, and blue
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = (r+g+b)/3
    if luminance < 64:
      setColor(p,black)
    elif luminance > 120:
      setColor(p,white)
    else: setColor(p,blue)
  return pic

def posterizeBKWR(pic):
  # posterize to black, white, and red
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = (r+g+b)/3
    if luminance < 64:
      setColor(p,black)
    elif luminance > 120:
      setColor(p,white)
    else: setColor(p,red)
  return pic

def grayScale(pic):
  #makes a picture black and white
  for pix in getPixels(pic):
    red = getRed(pix)
    blue = getBlue(pix)
    green = getGreen(pix)
    newColor =(blue + green + red)/3
    setColor(pix, makeColor(newColor, newColor, newColor))
  return pic

def sepiaTint(picture):
  #Convert image to grayscale
  grayScale(picture)
  
  #loop through picture to tint pixels
  for p in getPixels(picture):
    red = getRed(p)
    blue = getBlue(p)
    
    #tint shadows
    if (red < 63):
      red = red*1.1
      blue = blue*0.9
    
    #tint midtones
    if (red > 62 and red < 192):
      red = red*1.15
      blue = blue*0.85
    
    #tint highlights
    if (red > 191):
      red = red*1.08
      if (red > 255):
        red = 255
      blue = blue*0.93
    
    #set the new color values
    setBlue(p, blue)
    setRed(p, red)
  return picture

def luminance(pixel):
  # calculate the luminance of a pixel by taking an average of the three pixels
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  return (r+g+b)/3

def edgedetect(source):
  # create a simple "line drawing" from a picture
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source)-1 and x < getWidth(source)-1:
      botrt = getPixel(source,x+1,y+1)
      thislum = luminance(px)
      brlum = luminance(botrt)
      if abs(brlum-thislum) > 10:
        setColor(px,black)
      if abs(brlum-thislum) <= 10:
        setColor(px,white)
  return source

def mirrorVertical(source):
  #mirror the picture vertically
  mirrorPoint = getWidth(source) / 2
  width = getWidth(source)
  for y in range(0,getHeight(source)):
    for x in range(0,mirrorPoint):
      leftPixel = getPixel(source,x,y)
      rightPixel = getPixel(source,width - x - 1,y)
      color = getColor(leftPixel)
      setColor(rightPixel,color)
  return source

def flipRight(source):
  # flip the picture horizontally
  canvas = makeEmptyPicture(getWidth(source),getHeight(source))
  targetX = getWidth(source)-1
  for sourceX in range(0,getWidth(source)):
    targetY = 0
    for sourceY in range(0,getHeight(source)):
      pixelColor = getColor(getPixel(source, sourceX, sourceY))
      setColor(getPixel(canvas, targetX, targetY), pixelColor)
      targetY = targetY + 1
    targetX = targetX - 1
  return canvas

def pixelIt(picture, ps):
  # creates a picture that has blocks of color instead of individual pixels of color
  newPic = makeEmptyPicture(getWidth(picture), getHeight(picture))
  for x in range(0,  getWidth(picture), ps):
    for y in range(0, getHeight(picture), ps):
      redStore =  greenStore = blueStore = 0
      for psX in range(x, x + ps):
        for psY in range(y, y + ps):
          psPix = getPixel(picture, psX, psY)
          redStore = redStore + getRed(psPix)
          greenStore = greenStore + getGreen(psPix)
          blueStore = blueStore + getBlue(psPix)
      psRed = redStore / (ps*ps)
      psGreen = greenStore / (ps*ps)
      psBlue = blueStore / (ps*ps)
      for psX in range(x, x + ps):
        for psY in range(y, y + ps):
          psPix = getPixel(picture, psX, psY)
          newPix = getPixel(newPic, psX, psY)
          setColor(newPix, makeColor(psRed,psGreen,psBlue))
  return newPic

def blur(source):
  # blur the picture for smoother looking
  target=duplicatePicture(source)
  for x in range(1, getWidth(source)-1):
    for y in range(1, getHeight(source)-1):
      top = getPixel(source,x,y-1)
      left = getPixel(source,x-1,y)
      bottom = getPixel(source,x,y+1)
      right = getPixel(source,x+1,y)
      center = getPixel(target,x,y)
      newRed=(getRed(top)+ getRed(left) + getRed(bottom) + getRed(right) + getRed(center))/5
      newGreen=(getGreen(top) + getGreen(left) + getGreen(bottom)+ getGreen(right)+getGreen(center))/5
      newBlue=(getBlue(top) + getBlue(left) + getBlue(bottom) + getBlue(right)+ getBlue(center))/5
      setColor(center, makeColor(newRed, newGreen, newBlue))
  return target


def blendPictures(pic1, pic2, targX, targY):
  #blend two pictures together
  src1 = pic1
  src2 = pic2
  canvas = makeEmptyPicture(targX,targY)
  # Blend src1 with src2 at 50%
  overlapX = getWidth(src1)
  overlapY = getHeight(src1)
  sourceX=0
  for targetX in range(0,getWidth(src1)):
    sourceY=0
    for targetY in range(0,getHeight(src1)):
      bPixel = getPixel(src1,sourceX,sourceY)
      kPixel = getPixel(src2,sourceX,sourceY)
      newRed= 0.50*getRed(bPixel)+0.50*getRed(kPixel)
      newGreen=0.50*getGreen(bPixel)+0.50*getGreen(kPixel)
      newBlue = 0.50*getBlue(bPixel)+0.50*getBlue(kPixel)
      color = makeColor(newRed,newGreen,newBlue)
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY = sourceY + 1
    sourceX = sourceX + 1
  # The rest of src2
  sourceX=0
  for targetX in range(0,overlapX):
    sourceY=overlapY
    for targetY in range(overlapY,getHeight(src2)):
      color = getColor(getPixel(src2,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY = sourceY + 1
    sourceX = sourceX + 1
  sourceX=overlapX
  for targetX in range(overlapX,getWidth(src2)):
    sourceY=0
    for targetY in range(0,getHeight(src2)):
      color = getColor(getPixel(src2,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY = sourceY + 1
    sourceX = sourceX + 1
  return canvas

def negative(picture):
  # negate the colors of the picture
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255-red, 255-green, 255-blue)
    setColor(px,negColor)
  return picture

def addABlackBox(picture, targX, targY, boxwidth, boxheight):
  # add a black box with the specified dimension at the 
  target = picture
  addRectFilled(target,targX,targY,boxwidth,boxheight,black)
  return target

def rightHalfBright(pic):
  # make half of the picture brighter
  halfway = getWidth(pic) / 2
  for px in getPixels(pic):
    x = getX(px)
    if x > halfway:
      color = getColor(px)
      setColor(px,makeLighter(color))
  return pic
setMediaPath("/Users/Tuck/121/Projects/grading/p1/kim1")
writePictureTo(createCollage(), "kim1.jpg")
