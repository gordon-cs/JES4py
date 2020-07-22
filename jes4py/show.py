#!/usr/bin/env python3

import wx
import sys
import os
import time

from threading import *

# Define notification event for thread completion
EVT_MESSAGE_ID = wx.NewId()

class MessageEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data"""
    def __init__(self, data):
        """Init Message Event"""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_MESSAGE_ID)
        self.data = data

# Thread class that executes processing
class Listener(Thread):
    """Listener Thread Class"""
    def __init__(self, notifyWindow):
        """Init Listener Thread Class"""
        Thread.__init__(self)
        self.notifyWindow = notifyWindow
        self.start()

    def run(self):
        """Run Listener Thread"""
        while True:
            message = input().rstrip()
            if  message == 'exit':
                wx.PostEvent(self.notifyWindow, MessageEvent(None))
                return
            else:
                wx.PostEvent(self.notifyWindow, MessageEvent(message))

class MainWindow(wx.Frame):

    filename = None
    title = None

    def __init__(self, parent, filename, title):
        super(MainWindow, self).__init__(parent=parent, title=title)
        self.Connect(-1, -1, EVT_MESSAGE_ID, self.OnMessage)
        self.worker = Listener(self)
        self.filename = filename
        self.title = title
        self.showImage()

    def OnMessage(self, event):
        """Process message"""
        if event.data is None:
            # all done
            self.Close()
        else:
            self.filename, self.title = event.data.split(' ', 1)
            self.showImage()

    def showImage(self):
        image = wx.Image(self.filename, wx.BITMAP_TYPE_ANY)
        bmp = wx.Bitmap(image)
        imageSize = image.GetSize()
        self.SetTitle(self.title)
        self.imageCtrl = wx.StaticBitmap(parent=self, size=imageSize, bitmap=bmp)
        self.SetClientSize(imageSize)

# ===========================================================================
# Main program
# ===========================================================================

def main(argv):
    usage = "usage: {} file [title]".format(argv[0])
    # Get image file name and optional image title from command line
    if len(argv) == 2:
        filename = title = argv[1]
    elif len(argv) == 3:
        filename = argv[1]
        title = argv[2]
    else:
        print(usage)
        exit(1)

    if not os.path.isfile(filename):
        print("{} does not exist or is not a file".format(filename))
        print(usage)
        exit(1)

    app = wx.App(False)
    frame = MainWindow(parent=None, filename=filename, title=title)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main(sys.argv)
