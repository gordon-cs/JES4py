from JESemu import *
from random import randint
import PIL.Image

# Supporting functions
def openPicture(mediaPath='', filename='nico.jpg'):
    setMediaPath(mediaPath)
    return makePicture(filename)

def openEmptyPicture(color=white, width=300, height=300):
    return makeEmptyPicture(width, height, color)

def scribble():
    pic = openEmptyPicture(white, 300, 300)
    pic.setFileName("ScribbleTest")
    addRectFilled(pic, 100, 100, 50, 100, blue)
    addRect(pic, 100, 100, 50, 100, red)
    addOvalFilled(pic, 0, 25, 100, 50) #default color is black
    addOval(pic, 0, 0, 100, 100, magenta)
    addArcFilled(pic, 100, 100, 100, 100, 270, 45, orange)
    addArcFilled(pic, 100, 100, 100, 100, 270, -45, yellow)
    addArc(pic, 100, 100, 100, 100, 225, 90, black)
    addLine(pic, 0, 0, 100, 100, red)
    return pic

def makeReferenceImage(filename='refimage.jpg'):
    pic = scribble()
    pic.image.save(filename)


# Testing functions

def test_init():
    picture = openPicture()
    pilImage = picture.getImage()

    # create empty Picture
    p1 = Picture()
    assert isinstance(p1, Picture)
    assert p1.getFileName() == ''
    assert p1.getTitle() == ''
    assert p1.getExtension() == '.jpg'

    # create Picture from PIL Image
    p2 = Picture(pilImage)
    assert isinstance(p2, Picture)
    assert isinstance(p2.getImage(), PIL.Image.Image)
    assert p2.getFileName() == p2.getImage().filename
    assert p2.getTitle() == p2.getImage().filename
    assert p2.getExtension() == '.jpg'

    # create Picture from existing Picture
    p3 = Picture(picture)
    assert isinstance(p3, Picture)
    assert isinstance(p3.getImage(), PIL.Image.Image)
    assert p3.getFileName() == picture.getFileName()
    assert p3.getTitle() == picture.getTitle()
    assert p3.getExtension() == picture.getExtension()

    # create Picture from string
    s = "This is a test"
    p4 = Picture(s)
    assert isinstance(p4, Picture)
    assert isinstance(p4.getImage(), PIL.Image.Image)
    assert p4.getFileName() == ''
    assert p4.getTitle() == s
    assert p4.getExtension() == '.jpg'

def test_makePicture():
    picture = openPicture()
    assert isinstance(picture, Picture)

def test_makeEmptyPicture():
    picture = openEmptyPicture(green)
    assert isinstance(picture, Picture)

def test_setFileName_getFileName():
    newName = "My_new_and_really_long_file_name.jpg"
    picture = openEmptyPicture()
    picture.setFileName(newName)
    assert newName == picture.getFileName()

def test_setTitle_getTitle():
    newName = "My new and really long title"
    picture = openEmptyPicture()
    picture.setTitle(newName)
    assert newName == picture.getTitle()

def getWidth_getHeight():
    picture = openPicture()
    image = picture.getImage()
    assert image.width == picture.getWidth()
    assert image.height == picture.getHeight()

def test_getPixel_getPixels():
    picture = openPicture()
    w = picture.getWidth()
    h = picture.getHeight()
    x = randint(0, w-1)
    y = randint(0, h-1)
    pix = picture.getPixel(x, y)
    assert isinstance(pix, Pixel)
    pixels = picture.getPixels()
    assert len(pixels) == w * h
    assert pixels[x + w * y].getColor() == pix.getColor()

def test_setImage_getImage():
    picture = openPicture()
    image = picture.getImage()
    #assert isinstance(image, PIL.Image)
    w, h = image.size
    x1, y1 = round(w/4), round(h/4)
    x2, y2 = w-x1, h-y1
    newImage = image.crop([x1, y1, x2, y2])
    picture.setImage(newImage)
    assert (x2 - x1) == picture.getWidth()
    assert (y2 - y1) == picture.getHeight()

def test_crop():
    picture = openPicture()
    image = picture.getImage()
    w, h = picture.getWidth(), picture.getHeight()
    x = randint(0, w/4)
    y = randint(0, h/4)
    cw = randint(w/4, w/2)
    ch = randint(h/4, h/2)
    croppedPicture = picture.crop(x, y, cw, ch)
    croppedImage = croppedPicture.getImage()
    assert croppedImage == image.crop([x, y, x+cw, y+ch])
    
def test_drawing():
    pic = scribble()
    testImagePix = pic.getPixels()
    refImagePix = openPicture('','refimage.jpg').getPixels()
    assert len(testImagePix) == len(refImagePix)

#def test_show():
#    picture = openPicture()
#    picture.show()

def test_write():
    picture = openPicture()
    assert picture.write('test_picture.jpg')
    assert not picture.write('/nonexistant-folder/test_picture.jpg')

# Can be run as script to create or recreate refimage.jpg if needed
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "makeref":
        makeReferenceImage('refimageA.jpg')
    else:
        print("To (re)create reference image 'refimage.jpg', ", end="")
        print("run script with command:",)
        print("    python {} makeref".format(sys.argv[0]))
