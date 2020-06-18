import os
import wx
"""
# Simplist Hello World app
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))

        self.Show()
"""
"""
# Less simple Hellow World app
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        my_btn = wx.Button(panel, label='Press Me')
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)        
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
"""

# Simple text editor
# Will be implemented into a picture tool

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300,200))
        self.frame = wx.Frame(None, title='ImageViewer')
        self.panel = wx.Panel(self.frame)
        self.viewingWindow()
        self.frame.Show()
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu bar
        filemenu = wx.Menu()

        # Setting up the menu items
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Browse images to open")
        filemenu.AppendSeparator()
        menuZoom25 = filemenu.Append(wx.ID_ZOOM_OUT, "&25%","Zoom by 25%")
        menuZoom50 = filemenu.Append(wx.ID_ZOOM_OUT, "&50%","Zoom by 50%")
        menuZoom75 = filemenu.Append(wx.ID_ZOOM_OUT, "&75%","Zoom by 75%")
        menuZoom100 = filemenu.Append(wx.ID_ZOOM_100, "&100%","Zoom by 100% (original size)")
        menuZoom150 = filemenu.Append(wx.ID_ZOOM_IN, "&150%","Zoom by 150%")
        menuZoom200 = filemenu.Append(wx.ID_ZOOM_IN, "&200%","Zoom by 200%")
        menuZoom500 = filemenu.Append(wx.ID_ZOOM_IN, "&500%","Zoom by 500%")
        filemenu.AppendSeparator()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        

        # Set events
        self.Bind(wx.EVT_MENU, self.onOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.onZoom25, menuZoom25)
        self.Bind(wx.EVT_MENU, self.onZoom50, menuZoom50)
        self.Bind(wx.EVT_MENU, self.onZoom75, menuZoom75)
        self.Bind(wx.EVT_MENU, self.onZoom100, menuZoom100)
        self.Bind(wx.EVT_MENU, self.onZoom150, menuZoom150)
        self.Bind(wx.EVT_MENU, self.onZoom200, menuZoom200)
        self.Bind(wx.EVT_MENU, self.onZoom500, menuZoom500)

        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)


        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&Zoom") # Adds the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar) # Adds the MenuBar to the Frame content.
        self.Show(True)

    def viewingWindow(self):
        img = wx.EmptyImage(360,360)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)

        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)
        self.panel.Layout()


    # Browse images
    def onOpen(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Open an image", "Browse images", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Zoom the image by 25%
    def onZoom25(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Image zoomed by 25%", "Zoom feature - 25%", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Zoom the image by 50%
    def onZoom50(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Image zoomed by 50%", "Zoom feature - 50%", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Zoom the image by 75%
    def onZoom75(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Image zoomed by 75%", "Zoom feature - 75%", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Zoom the image by 100%
    def onZoom100(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Image zoomed by 100%", "Zoom feature - 100%", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Zoom the image by 150%
    def onZoom150(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Image zoomed by 150%", "Zoom feature - 150%", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Zoom the image by 200%
    def onZoom200(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Image zoomed by 200%", "Zoom feature - 200%", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.
    
    # Zoom the image by 500%
    def onZoom500(self,e):
        # Dummie method - returns a dialog box
        dlg = wx.MessageDialog(self, "Image zoomed by 500%", "Zoom feature - 500%", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def onAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def onExit(self,e):
        self.Close(True)  # Close the frame.

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Sample editor")
    app.MainLoop()