from JESemu import *
from random import randint
import PIL.Image

def openPicture():
    mediaPath = ''
    filename = 'nico.jpg'
    setMediaPath(mediaPath)
    return makePicture(filename)

def openEmptyPicture(color=white, width=300, height=300):
    return makeEmptyPicture(width, height, color)

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

def test_show():
    picture = openPicture()
    picture.show()
    #show(picture)


#addRectFilled(pic2, 100, 100, 50, 100, blue)
#addRect(pic2, 100, 100, 50, 100, red)
#addOvalFilled(pic2, 0, 25, 100, 50) #default color is black
#addOval(pic2, 0, 0, 100, 100, magenta)
#addArcFilled(pic2, 100, 100, 100, 100, 270, 45, orange)
#addArcFilled(pic2, 100, 100, 100, 100, 270, -45, yellow)
#addArc(pic2, 100, 100, 100, 100, 225, 90, black)
#addLine(pic2, 0, 0, 100, 100, red)
#show(pic2)

#def test_pickAFile():



