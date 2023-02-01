#!/usr/bin/env python3

"""
show.py - script program to implement the "show" and "repaint" functionality
            in JES for the JES4py package

Written: 2020-07-22 Jonathan Senning <jonathan.senning@gordon.edu>
Revised: 2020-09-02 Jonathan Senning <jonathan.senning@gordon.edu>
- received pickled picture objects rather than filename, no need to read files

The "show()" function in JES will open a new window and display the image
associated with the given Picture object in the window.  The window is
static and does not provide for user interaction.  When the "repaint()"
function is called, however, the contents of the window are refreshed so
that any changes to the displayed Picture (the image itself or the picture's
title) are displayed.  Thus, repaint() can be used to produce simple
animations.

The jes4py.Picture module defines the Picture class, which has show() and
repaint() methods.  The show() method causes this script to be run in a
subprocess and uses a pipe to send a pickled picture object to the subprocess.
The repaint() method checks to make sure a subprocess for this picture object
is currently running and then sends the pickled updated picture object.

This script expects the initial byte of data to be 0 (to exit) or 1
(a pickled picture object follows).

Implementation note: The thread portion of this program is based on the
first example at https://wiki.wxpython.org/LongRunningTasks.  The pickling
method is based on that shown in
https://www.imagetracking.org.uk/2018/03/piping-numpy-arrays-to-other-processes-in-python/
"""

import wx
import sys, os
import pickle
from threading import *
from jes4py import *

class MessageEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data"""
    def __init__(self, data):
        """Initializer for MessageEvent class

        Parameters
        ----------
        data : (can be any type, but will be a string in this program)
            the message contents
        """
        wx.PyEvent.__init__(self)
        self.SetEventType(wx.ID_ANY)
        self.data = data

# Thread class that executes processing
class Listener(Thread):
    """Listener Thread Class"""
    def __init__(self, notifyWindow):
        """Initializer for Listener Thread Class

        Parameters
        ----------
        notifyWindow : wx.Frame
            the window to notify when a message is received
        """
        Thread.__init__(self)
        self.notifyWindow = notifyWindow
        self.start()

    def run(self):
        """Run Listener thread"""
        while True:
            # wait for control code
            data = sys.stdin.buffer.read(1)
            if data == Picture.show_control_exit:
                # shutdown program
                wx.PostEvent(self.notifyWindow, MessageEvent(None))
                return
            elif data == Picture.show_control_data:
                # read picture size and pickled picture data
                try:
                    data = sys.stdin.buffer.read(8)
                    dataLen = int.from_bytes(data, byteorder='big')
                    pkg = sys.stdin.buffer.read(dataLen)
                    wx.PostEvent(self.notifyWindow, MessageEvent(pkg))
                except RuntimeError:
                    return
            else:
                # unrecognised control code
                return

class MainWindow(wx.Frame):
    """Window class for show program
    """

    def __init__(self, parent):
        """Initializer for MainWindow

        Parameters
        ----------
        parent : wxFrame
            the parent frame
        """
        super(MainWindow, self).__init__(parent=parent)

        # Set up listener for data coming in over pipe
        self.Connect(-1, -1, wx.ID_ANY, self.OnMessage)
        self.worker = Listener(self)

        # Create panel for displayed window
        self.panel = wx.Panel(parent=self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 0, wx.ALIGN_LEFT|wx.ALIGN_TOP|wx.ALL, 0)
        self.SetSizerAndFit(self.sizer)

    def OnMessage(self, event):
        """Handle received message

        Parameters
        ----------
        event : wx.Event
            the event object

        event.data is either None (to indicate request to terminate program)
        or a pickled Picture object
        """
        if event.data is None:
            # all done
            self.Close()
        else:
            # unpickle data and update displayed image
            picture = pickle.loads(event.data)
            self.updateBitmap(picture)

    def updateBitmap(self, picture):
        """Update bitmap of displayed image

        Parameters
        ----------
        picture : Picture object
            picture to display
        """
        image = picture.getWxImage()
        imageSize = image.GetSize()
        bmp = wx.Bitmap(image)
        self.SetTitle(picture.getTitle())
        self.bitmap = wx.StaticBitmap(parent=self.panel, size=imageSize, \
                                        bitmap=bmp)
        self.SetClientSize(imageSize)
        self.Refresh()

# ===========================================================================
# Main program
# ===========================================================================

def main(argv):
    app = wx.App(False)
    frame = MainWindow(parent=None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main(sys.argv)
