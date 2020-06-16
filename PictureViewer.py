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
        wx.Frame.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Picture Tool')
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        self.panel = wx.Panel(self.frame)

        # Setting up the menu bar
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuZoom25 = filemenu.Append(wx.ID_ZOOM_OUT, "&25%", "Zoom by 25%")
        menuZoom50 = filemenu.Append(wx.ID_ZOOM_OUT, "&50%", "Zoom by 50%")
        """
        menuZoom75 = filemenu.Append(wx.ID_ZOOM_OUT, "&75%", "Zoom by 75%")
        menuZoom100 = filemenu.Append(wx.ID_ZOOM_100, "&100%", "Zoom by 100%")
        menuZoom150 = filemenu.Append(wx.ID_ZOOM_IN, "&150%", "Zoom by 150%")
        menuZoom200 = filemenu.Append(wx.ID_ZOOM_IN, "&200%", "Zoom by 200%")
        menuZoom500 = filemenu.Append(wx.ID_ZOOM_IN, "&500%", "Zoom by 500%")
        """
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Create the menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&Zoom") # Adds the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar) # Adds the MenuBar to the Frame content

        
        # Set events
        self.Bind(wx.ID_ZOOM_OUT, self.OnZoom25, menuZoom25)
        self.Bind(wx.ID_ZOOM_OUT, self.OnZoom50, menuZoom50)
        """
        self.Bind(wx.ID_ZOOM_OUT, self.OnZoom75, menuZoom75)
        self.Bind(wx.ID_ZOOM_100, self.OnZoom100, menuZoom100)
        self.Bind(wx.ID_ZOOM_IN, self.OnZoom150, menuZoom150)
        self.Bind(wx.ID_ZOOM_IN, self.OnZoom200, menuZoom200)
        self.Bind(wx.ID_ZOOM_IN, self.OnZoom500, menuZoom500)
        """
        self.Bind(wx.ID_ABOUT, self.OnAbout, menuAbout)
        self.Bind(wx.ID_EXIT, self.OnExit, menuExit)

        self.Show(True)

        # Set the maximum size of the picture
        self.PictureMaxSize = 360

        # self.createWidgets()
        #self.frame.Show()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A simple picture tool", "About Picture Tool", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

app = wx.App(False)
frame = PictureTool(None, "Picture Tool")
app.MainLoop()