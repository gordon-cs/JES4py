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
        menuZoom25 = filemenu.Append(wx.ID_ZOOM_25, "&25%", "Zoom by 25%")
        menuZoom50 = filemenu.Append(wx.ID_ZOOM_50, "&50%", "Zoom by 50%")
        menuZoom75 = filemenu.Append(wx.ID_ZOOM_75, "&75%", "Zoom by 75%")
        menuZoom100 = filemenu.Append(wx.ID_ZOOM_100, "&100%", "Zoom by 100%")
        menuZoom150 = filemenu.Append(wx.ID_ZOOM_150, "&150%", "Zoom by 150%")
        menuZoom200 = filemenu.Append(wx.ID_ZOOM_200, "&200%", "Zoom by 200%")
        menuZoom500 = filemenu.Append(wx.ID_ZOOM_500, "&500%", "Zoom by 500%")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        
        # Set the maximum size of the picture
        self.PictureMaxSize = 360

        self.createWidgets()
        self.frame.Show()

    