# Simple picture tool
# CS Summer Practicum 2020
# Author: Gahngnin Kim

import os, sys
import wx
import wx.lib.inspection

"""
class PictureTool(pil_img):
    def pil_image_to_wx_image(self, pil_img, copy_alpha=True):
        # Image conversion from a Pillow Image to a wx.Image.
        orig_width, orig_height = pil_img.size
        wx_img = wx.Image(orig_width, orig_height)
        wx_img.SetData(pil_img.convert('RGB').tobytes())
        if copy_alpha and (pil_img.mode[-1] == 'A'):
            alpha = pil_img.getchannel("A").tobytes()
            wx_img.InitAlpha()
            for i in range(orig_width):
                for j in range(orig_height):
                    wx_img.SetAlpha(i, j, alpha[i + j * orig_width])
        return wx_img
"""

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        MainFrame = wx.Frame.__init__(self, parent, title=title, size=(660,500))
        self.panel = wx.Panel(self)        
        wx.lib.inspection.InspectionTool().Show()
        
        # Maximum horizontal dimension
        self.PhotoMaxSize = 600

        # Color Eyedropper
        self.ColorPicker()

        # Image viewer
        self.viewingWindow()

        # A Statusbar in the bottom of the window
        self.CreateStatusBar()

        # Setting up the menu bar
        filemenu = wx.Menu()

        # Setting up the menu items
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Browse images to open")
        filemenu.AppendSeparator()
        menuZoom25 = filemenu.Append(wx.ID_ANY, "&25%","Zoom by 25%")
        menuZoom50 = filemenu.Append(wx.ID_ANY, "&50%","Zoom by 50%")
        menuZoom75 = filemenu.Append(wx.ID_ANY, "&75%","Zoom by 75%")
        menuZoom100 = filemenu.Append(wx.ID_ZOOM_100, "&100%","Zoom by 100% (original size)")
        menuZoom150 = filemenu.Append(wx.ID_ANY, "&150%","Zoom by 150%")
        menuZoom200 = filemenu.Append(wx.ID_ANY, "&200%","Zoom by 200%")
        menuZoom500 = filemenu.Append(wx.ID_ANY, "&500%","Zoom by 500%")
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

    # Main image viewing window
    def viewingWindow(self):
        # initialize an empty image
        wxImg = wx.Image(600,360) # wx.Image(width, height, clear)

        # Convert the image into a bitmap image
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(wxImg))


        # Event handler - Gets X, Y coordinates on mouse click
        self.imageCtrl.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)

        # Stores the filepath of the image
        self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1))
        self.photoTxt.Show(False)
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.hSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add((-1, 50))

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5)
        self.hSizer1.Add(self.photoTxt, 0, wx.ALL, 5)
        self.mainSizer.Add(self.hSizer1, 0, wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.panel)
        #self.panel.Layout()
    
    def ColorPicker(self):
        # initialize an empty bitmap
        self.bmp = wx.Bitmap(20,20)
        self.colorPreview = wx.StaticBitmap(self.panel, wx.ID_ANY, self.bmp)
        self.colorPreview.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)

        # Textboxes to display X and Y coordinates on click
        self.pixelTxtX = wx.TextCtrl(self.panel, wx.ALIGN_CENTER, size=(50,-1))
        self.pixelTxtY = wx.TextCtrl(self.panel, wx.ALIGN_CENTER, size=(50,-1))

        # Static text displays RGB values of the given coordinates
        # Initialized with dummie values
        self.rgbValue = wx.StaticText(self.panel, label=u'R: {} G: {} B: {}'.format("N/A", "N/A", "N/A"),style = wx.ALIGN_CENTER)
        
        
        # dc = wx.MemoryDC()
        # dc.SelectObject(self.bmp)
        # dc.SetBackground(wx.Brush("Red"))
        # dc.Clear()
        # del dc

        # Convert the image into a bitmap image
        #self.colorPreview = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(self.emptyImg))
        # self.colorPreview = wx.StaticBitmap(self.panel, wx.ID_ANY, self.bmp)
        # self.colorPreview.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)


        # X and Y labels
        self.lblX = wx.StaticText(self.panel,0,style = wx.ALIGN_CENTER)
        self.lblY = wx.StaticText(self.panel,0,style = wx.ALIGN_CENTER)
        self.lblX.SetLabel("X: ")
        self.lblY.SetLabel("Y: ")

        # Navigation buttons (Enable after getting the colorpicker/eyedropper functional)
        # self.buttonX1 = wx.Button(self, wx.BU_LEFT, label="<")
        # self.buttonX2 = wx.Button(self, wx.BU_RIGHT, label=">")
        # self.buttonY1 = wx.Button(self, wx.BU_LEFT, label="<")
        # self.buttonY2 = wx.Button(self, wx.BU_RIGHT, label=">")

        # Initialize the sizers for layout
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # Display Y coordinate on click
        self.hbox1.Add(self.lblX, 0, flag=wx.CENTER, border=0)
        #self.hbox1.Add(self.buttonX1, -1, flag=wx.CENTER, border=0)
        self.hbox1.Add(self.pixelTxtX, 0, flag=wx.CENTER, border=5) # Text Control Box
        #self.hbox1.Add(self.buttonX2, -1, flag=wx.CENTER, border=0)

        # Horizonal spacer
        self.hbox1.Add((10, -1))

        # Display Y coordinate on click
        self.hbox1.Add(self.lblY, 0, flag=wx.CENTER, border=0)
        self.hbox1.Add(self.pixelTxtY, 0, flag=wx.RIGHT, border=5) # Text Control Box
        
        # Add the hbox1 to the main sizer
        self.box.Add(self.hbox1, 0, flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)

        # Vertical spacer
        self.box.Add((-1, 5))
        
        # Add items to the second sizer (hbox2)
        self.hbox2.Add(self.rgbValue, 0, flag=wx.CENTER, border=5)
        self.hbox2.Add((10, -1)) # Horizonal spacer
        self.hbox2.Add(self.colorPreview, 0, flag=wx.CENTER, border=5) # Small image that shows the color at the selected pixel
        
        # Add hbox2 to the main sizer
        self.box.Add(self.hbox2, 0, flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)


        self.panel.SetSizer(self.box)
        self.box.Fit(self.panel)
        self.panel.Layout()
        self.Show()

    def ImageCtrl_OnMouseClick(self, event):
        # Returns X, Y coordinates on mouse click
        ctrl_pos = event.GetPosition()
        self.pixelTxtX.SetValue(str(ctrl_pos.x))
        self.pixelTxtY.SetValue(str(ctrl_pos.y))
        r = self.image.GetRed(ctrl_pos.x, ctrl_pos.y)
        g = self.image.GetGreen(ctrl_pos.x, ctrl_pos.y)
        b = self.image.GetBlue(ctrl_pos.x, ctrl_pos.y)
        # print ("R: {} G: {} B: {}".format(r,g,b))
        self.rgbValue.SetLabel(label=u'R: {} G: {} B: {}'.format(r, g, b))
        print (r, g, b)
        #dc.SetBrush(wx.Brush(wx.Color(r,g,b), wx.SOLID))
        bmp = wx.Bitmap(20,20)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(wx.Colour(r,g,b), wx.SOLID))
        dc.Clear()
        del dc

        # convert it to a wx.Bitmap, and put it on the wx.StaticBitmap
        self.colorPreview.SetBitmap(bmp)

        # You can fit the frame to the image, if you want.
        #self.Fit()
        #self.Layout()
        self.Refresh()

        # self.Refresh(eraseBackground=False)
        # self.Update()
        # self.panel.Refresh()

    def onOpen(self,e):
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
        img = img.Scale(int(NewW),int(NewH))
        self.image = img
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    # Zoom the image by 25%
    def onZoom25(self,e):
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
        ScaledW = NewW * 0.25
        ScaledH = NewH * 0.25

        img = img.Scale(int(ScaledW),int(ScaledH))
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    # Zoom the image by 50%
    def onZoom50(self,e):
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
        ScaledW = NewW * 0.50
        ScaledH = NewH * 0.50

        img = img.Scale(int(ScaledW),int(ScaledH))
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    # Zoom the image by 75%
    def onZoom75(self,e):
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
        ScaledW = NewW * 0.75
        ScaledH = NewH * 0.75

        img = img.Scale(int(ScaledW),int(ScaledH))
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    # Zoom the image by 100%
    def onZoom100(self,e):
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
        img = img.Scale(int(NewW),int(NewH))
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    # Zoom the image by 150%
    def onZoom150(self,e):
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
        ScaledW = NewW * 1.50
        ScaledH = NewH * 1.50

        img = img.Scale(int(ScaledW),int(ScaledH))
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    # Zoom the image by 200%
    def onZoom200(self,e):
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
        ScaledW = NewW * 2.0
        ScaledH = NewH * 2.0

        img = img.Scale(int(ScaledW),int(ScaledH))
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()
    
    # Zoom the image by 500%
    def onZoom500(self,e):
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
        ScaledW = NewW * 5.0
        ScaledH = NewH * 5.0

        img = img.Scale(int(ScaledW),int(ScaledH))
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()

    def onAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A simple picture tool", "About the Image Tool", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def onExit(self,e):
        self.Close(True)  # Close the frame.

def GetJpgList(dir):
    jpgs = [f for f in os.listdir(dir) if f[-4:] == ".jpg"]
    # print "JPGS are:", jpgs
    return [os.path.join(dir, f) for f in jpgs]

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Sample Image Tool")
    app.MainLoop()