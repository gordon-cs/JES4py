import os

import wx
"""
class ImagePanel(wx.Panel):

    def __init__(self):



class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Picture Tool')
        panel = ImagePanel(self, image=(360,360))
        self.Show()

        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Picture Tool')
        #self.CreateStatusBar() # A StatusBar in the bottom of the window

        self.panel = wx.Panel(self.frame)

        # Set the maximum size of the picture
        self.PictureMaxSize = 360

        # Setting up the menu bar
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
       
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Create the menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&Zoom") # Adds the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar) # Adds the MenuBar to the Frame content
        self.Show(True)

        
        # Set events
        self.Bind(wx.ID_ABOUT, self.OnAbout, menuAbout)
        self.Bind(wx.ID_EXIT, self.OnExit, menuExit)

        self.Show(True)

        # self.createWidgets()
        #self.frame.Show()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A simple picture tool", "About Picture Tool", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

if __name__ == '__main__':
    app = PictureTool()
    app.MainLoop()

"""

class PictureTool(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Simple Picture Tool')                
        self.panel = wx.Panel(self.frame)
        self.PhotoMaxSize = 540
        
        self.createWidgets()
        self.frame.Show()
    
    def createWidgets(self):
        instructions = 'Browse for an image'
        img = wx.EmptyImage(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                         wx.BitmapFromImage(img))
        
        instructLbl = wx.StaticText(self.panel, label=instructions)
        self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1))
        browseBtn = wx.Button(self.panel, label='Browse')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(instructLbl, 0, wx.ALL, 5)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
        self.sizer.Add(browseBtn, 0, wx.ALL, 5)        
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)
        
        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)
        self.panel.Layout()
        
    def onBrowse(self, event):
        
        # Browse for file
        
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.ID_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy() 
        self.onView()
    
    def onView(self):
        filepath = self.photoTxt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)
        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        self.panel.Refresh()
        
if __name__ == '__main__':
    app = PictureTool()
    app.MainLoop()


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

