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

        self.panel = wx.Panel(self.frame)
        
        # Set the maximum size of the picture
        self.PictureMaxSize = 360

        self.createWidgets()
        self.frame.Show()

    def createWidgets(self):
        instructions = 