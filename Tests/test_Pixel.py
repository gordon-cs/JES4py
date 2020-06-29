from JESemu import *
from random import randint
import PIL.Image

def getRandomPixelData():
    mediaPath = '.'
    filename = 'nico.jpg'
    setMediaPath(mediaPath)
    pic = makePicture(filename)
    image = PIL.Image.open(filename)
    x = randint(0, pic.getWidth()-1)
    y = randint(0, pic.getHeight()-1)
    pix = getPixel(pic, x, y)
    color = image.getpixel((x, y))
    return pix, x, y, color
    
def test_getPixel():
    pix, x, y, color = getRandomPixelData()
    assert isinstance(pix, Pixel)

def test_getX_getY():
    pix, x, y, color = getRandomPixelData()
    assert (x == pix.getX() and y == pix.getY())

def test_getRed_getGreen_getBlue():
    pix, x, y, color = getRandomPixelData()
    assert color[0] == pix.getRed()
    assert color[1] == pix.getGreen()
    assert color[2] == pix.getBlue()

def test_getColor():
    pix, x, y, color = getRandomPixelData()
    assert isinstance(pix.getColor(), Color)

def test_getAverage():
    pix, x, y, color = getRandomPixelData()
    averageColor = round((color[0] + color[1] + color[2]) / 3.0)
    assert averageColor == pix.getAverage()

def test_setRed_setGreen_setBlue():
    pix, x, y, color = getRandomPixelData()
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    pix.setRed(r)
    pix.setGreen(g)
    pix.setBlue(b)
    assert r == pix.getRed()
    assert g == pix.getGreen()
    assert b == pix.getBlue()

def test_wrapping():
    pix, x, y, color = getRandomPixelData()

    rNew = 250
    gNew = 260
    bNew = -45

    Pixel.setWrapLevels(True)
    assert Pixel.getWrapLevels()
    pix.setRed(rNew)
    pix.setGreen(gNew)
    pix.setBlue(bNew)
    assert rNew % 256 == pix.getRed()
    assert gNew % 256 == pix.getGreen()
    assert bNew % 256 == pix.getBlue()

    Pixel.setWrapLevels(False)
    assert not Pixel.getWrapLevels()
    pix.setRed(rNew)
    pix.setGreen(gNew)
    pix.setBlue(bNew)
    assert rNew == pix.getRed()
    assert 255 == pix.getGreen()
    assert 0 == pix.getBlue()
    
