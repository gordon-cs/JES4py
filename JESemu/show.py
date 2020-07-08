#!/usr/bin/env python

# Demo program that
#   - optionally accepts an image file name as a command line argument
#   - creates a PIL image from the filename
#   - calls a "show()" function that converts the PIL image to a wx image
#     and displays the image in a new wx window
#
# wx code based on that provided at
# https://stackoverflow.com/questions/46374595/displaying-image-in-wxpython

import sys, os
import wx
import PIL.Image
from Picture import Picture

class mainWindow(wx.Frame):
    """Frame class that display an image"""
    def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title=None):
        """Create a frame instance and display image"""
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
        self.SetClientSize(size)

class ShowImage(wx.App):
    """Application class"""
    def __init__(self, image=None, title=None, *args, **kwargs):
        self.image = image
        self.title = title
        wx.App.__init__(self, *args, **kwargs)

    def OnInit(self):
        self.frame = mainWindow(image=self.image, title=self.title)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

# Main program

if __name__ == "__main__":
    # Get image file name and optional image title from command line
    if len(sys.argv) == 2:
        filename = title = sys.argv[1]
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        title = sys.argv[2]
    else:
        print("usage: {} file title".format(sys.argv[0]))
        exit(1)

    # load the image 
    try:
        image = Picture(PIL.Image.open(filename)).getWxImage()
        #image = getWxImage(PIL.Image.open(filename))
    except FileNotFoundError:
        print("Image file {} not found".format(filename))
        exit(1)
    except:
        print("Unable to load image from {}".format(filename))
        exit(1)

    # Show the image
    #wxImage = getWxImage(image)
    app = ShowImage(image=image, title=title)
    app.MainLoop()
