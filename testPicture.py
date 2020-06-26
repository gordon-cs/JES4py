#!/usr/bin/env python3

from media import *

pic1 = makePicture('Sandbox/nico.jpg')
addRect(pic1, 0, 0, 150, 300, red)
#pic1.show()
show(pic1)

#file = pickAFile()
pic2 = makeEmptyPicture(300,300,green)
pic2.setFileName("Empty File")
addRectFilled(pic2, 100, 100, 50, 100, blue)
addRect(pic2, 100, 100, 50, 100, red)
addOvalFilled(pic2, 0, 25, 100, 50) #default color is black
addOval(pic2, 0, 0, 100, 100, magenta)
addArcFilled(pic2, 100, 100, 100, 100, 270, 45, orange)
addArcFilled(pic2, 100, 100, 100, 100, 270, -45, yellow)
addArc(pic2, 100, 100, 100, 100, 225, 90, black)
addLine(pic2, 0, 0, 100, 100, red)
show(pic2)
