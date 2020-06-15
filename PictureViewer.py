import os

import wx

"""
# Image viewer using the existing library of wxPython
import wx.lib.mixins.inspection as wit
import wx.lib.imagebrowser as ib

app = wit.InspectableApp()

with ib.ImageDialog(None) as dlg:
    if dlg.ShowModal() == wx.ID_OK:
        # show the selected file
        print("You Selected File: " + dlg.GetFile())
    else:
        print("You pressed Cancel")

app.MainLoop()
"""

class PictureTool(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Picture Tool')
        self.CreateStatusBar() # Creates a status bar on the bottom of the window

        self.panel = wx.Panel(self.frame)

        # Setting up the menu bar
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_OPEN, "&Open", "Browse for an image")
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        
        # Set the maximum size of the picture
        self.PictureMaxSize = 360

        self.createWidgets()
        self.frame.Show()

    def createWidgets(self):
        img = wx.EmptyImage(360,360)