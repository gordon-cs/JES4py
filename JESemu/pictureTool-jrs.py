# Simple picture tool to replace JES picture tool
# CS Summer Practicum 2020
# Author: Gahngnin Kim
# Modified by:

import os, sys
import wx
import wx.lib.scrolledpanel
# import wx.lib.inspection

class MainWindow(wx.Frame):
    PaintChipSize = 24
    def __init__(self, filename, parent=None, id=-1, pos=wx.DefaultPosition, title=None):
        # Initial X,Y coordinates and zoom scale factor
        self.x = 0
        self.y = 0
        self.ratio = 1.0

        # The main window needs to be at least this wide (pixels)
        MIN_WIDTH = 300
        MIN_HEIGHT = 0

        # First retrieve the screen size of the device
        self.screenSize = wx.DisplaySize()
        self.screenWidth = self.screenSize[0]
        self.screenHeight = self.screenSize[1]

        # Get image information
        self.origImage = wx.Image(filename, wx.BITMAP_TYPE_ANY) # Imported image
        self.origWidth = self.origImage.GetWidth()
        self.origHeight = self.origImage.GetHeight()
        self.size = (self.origWidth, self.origHeight)
        self.image = self.origImage

        # Compute initial window size
        self.windowSize = (min(max(MIN_WIDTH, self.origWidth), self.screenWidth),
                            min(max(MIN_HEIGHT, self.origHeight), self.screenHeight))
        print(self.windowSize)
        self.viewableArea = (self.origWidth + 10, self.origHeight + 150)
        if self.viewableArea[0] < MIN_WIDTH:
            ratio = MIN_WIDTH / self.viewableArea[0]
            self.viewableArea = (int(self.viewableArea[0]*ratio), int(self.viewableArea[1]*ratio))
        elif self.viewableArea[0] >= self.screenWidth or self.viewableArea[1] >= self.screenHeight:
            self.viewableArea = (self.screenWidth - int(self.screenWidth/20)), \
                                (self.screenHeight - int(self.screenHeight/40))

        # Set the minimum and maximum width on launch
        if self.origWidth < MIN_WIDTH:
            Ratio = MIN_WIDTH / self.origWidth
            self.size = (int(self.origWidth*Ratio), int(self.origHeight*Ratio))
            print("very small: ", self.size)
        elif self.origWidth > self.viewableArea[0]:
            self.size = self.viewableArea #(self.viewableArea[0], self.viewableArea[1])
            print("viewable area: ", self.size)
        else:
            self.size = (self.origWidth, self.origHeight)
            print("orig size: ", self.size)

        # Top level wxframe -- Everything is contained here
        wx.Frame.__init__(self, parent, title=title, size=self.viewableArea, style=wx.DEFAULT_FRAME_STYLE)# ^ wx.RESIZE_BORDER)
        #wx.Frame.__init__(self, parent, title=title, size=self.windowSize, style=wx.DEFAULT_FRAME_STYLE)# ^ wx.RESIZE_BORDER)

        # Initialize the top level panel under the main frame
        # This will include sublevel panels
        self.SetAutoLayout(True)

        # Boxsizer to contain sublevel panels
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel1 = wx.Panel(parent=self, size=(-1,-1), pos=(0,0), style=wx.EXPAND, id=-1)
        self.panel2 = wx.lib.scrolledpanel.ScrolledPanel(parent=self, size=self.size, pos=(-1,-1), id=-1, style=wx.NO_BORDER)
        self.panel2.SetupScrolling()
        sizer.Add(self.panel1, 0, wx.EXPAND|wx.ALL, border=0)
        sizer.Add(self.panel2, 0, wx.EXPAND|wx.ALL, border=0)
        
        # wx.lib.inspection.InspectionTool().Show() # Inspection tool for debugging

        self.ColorPicker() # Color Eyedropper
        self.viewingWindow() # Image viewer
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        #self.panel2.SetClientSize(self.size)

        # Setting up the menu bar
        self.zoomMenu = wx.Menu()

        # Setting up the menu items
        # Standard ID given to each item are provided by wxWidgets.
        menuZoom25 = self.zoomMenu.Append(wx.ID_ANY, "25%","Zoom by 25%")
        menuZoom50 = self.zoomMenu.Append(wx.ID_ANY, "50%","Zoom by 50%")
        menuZoom75 = self.zoomMenu.Append(wx.ID_ANY, "75%","Zoom by 75%")
        menuZoom100 = self.zoomMenu.Append(wx.ID_ZOOM_100, "100%","Zoom by 100% (original size)")
        menuZoom150 = self.zoomMenu.Append(wx.ID_ANY, "150%","Zoom by 150%")
        menuZoom200 = self.zoomMenu.Append(wx.ID_ANY, "200%","Zoom by 200%")
        menuZoom500 = self.zoomMenu.Append(wx.ID_ANY, "500%","Zoom by 500%")

        # Set events
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom25)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom50)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom75)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom100)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom150)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom200)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom500)
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(self.zoomMenu, "&Zoom") # Adds the "zoomMenu" to the MenuBar
        self.SetMenuBar(menuBar) # Adds the MenuBar to the Frame content.

        #self.topPanel.SetSizer(sizer)
        self.SetSizer(sizer)
        self.Layout()
        self.panel1.Layout()
        self.panel2.Layout()
        self.Show()

        self.panel2.SetFocus()
        self.panel2.Bind(wx.EVT_LEFT_DOWN, self.onFocus)
        self.onView()
        self.isInteger()
        
    def onFocus(self, event):
        self.panel2.SetFocus()

    def viewingWindow(self):
        """ Main image viewing window
        """
        # Convert the image into a bitmap image
        self.imageCtrl = wx.StaticBitmap(self.panel2, -1, wx.Bitmap(self.image))

        # Event handler - Gets X, Y coordinates on mouse click
        self.imageCtrl.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)
        self.imageCtrl.Bind(wx.EVT_MOTION, self.ImageCtrl_OnMouseClick)
        
        #########LAYOUT SETUP###########
        # Initialize vertical and horizontal boxsizers
        mainSizer = wx.BoxSizer(wx.VERTICAL) # Main vertical boxsizer

        # Places components to the sizers
        mainSizer.Add(self.imageCtrl, 0, wx.ALIGN_LEFT|wx.ALL, 0)

        # Set the main sizer to fit the top level panel
        self.panel2.SetSizer(mainSizer)
        mainSizer.Fit(self.panel2)

    
    def ColorPicker(self):
        """ Reads color information from the selected pixel.
            Displays X and Y coordinates, RGB values, and the color of the pixel.
            The user can select the pixel by directly clicking on it OR
            by typing a specific coordinate.
        """
        # initialize an empty bitmap
        self.bmp = wx.Bitmap(self.PaintChipSize, self.PaintChipSize)
        self.colorPreview = wx.StaticBitmap(self.panel1, wx.ID_ANY, self.bmp)
        #self.colorPreview.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)

        # Textboxes to display X and Y coordinates on click
        self.pixelTxtX = wx.TextCtrl(self.panel1, wx.ALIGN_CENTER, style=wx.TE_PROCESS_ENTER, size=(50,-1))
        self.pixelTxtY = wx.TextCtrl(self.panel1, wx.ALIGN_CENTER, style=wx.TE_PROCESS_ENTER, size=(50,-1))
        self.pixelTxtX.Bind(wx.EVT_TEXT_ENTER, self.ImageCtrl_OnEnter)
        self.pixelTxtY.Bind(wx.EVT_TEXT_ENTER, self.ImageCtrl_OnEnter)

        # Static text displays RGB values of the given coordinates
        # Initialized with dummie values
        #self.rgbValue = wx.StaticText(self.panel1, label=u'R: {} G: {} B: {}  Color at location:'.format(255, 255, 255), style=wx.ALIGN_CENTER)
        self.rgbValue = wx.StaticText(self.panel1, label=u'this is a test')#, style=wx.ALIGN_CENTER)
        font = self.rgbValue.GetFont()
        font.PointSize += 2
        self.rgbValue.Font = font
        
        # X and Y labels
        self.lblX = wx.StaticText(self.panel1, 0, style=wx.ALIGN_CENTER)
        self.lblY = wx.StaticText(self.panel1, 0, style=wx.ALIGN_CENTER)
        self.lblX.SetLabel("X: ")
        self.lblY.SetLabel("Y: ")

        # Navigation buttons (Enable after getting the colorpicker/eyedropper functional)
        # Icons made by Freepik from www.flaticon.com; Modified by Gahngnin Kim
        rightImage = os.path.join(sys.path[0], 'images', 'Right.png')
        leftImage = os.path.join(sys.path[0], 'images', 'Left.png')
        bmp_R = wx.Bitmap(rightImage, wx.BITMAP_TYPE_ANY)
        bmp_L = wx.Bitmap(leftImage, wx.BITMAP_TYPE_ANY)
        bmp_size = (bmp_L.GetWidth()+5,bmp_L.GetHeight()+5)
        self.buttonX_L = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_L, size=bmp_size)
        self.buttonX_L.myname = "XL"
        self.buttonX_R = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_R, size=bmp_size)
        self.buttonX_R.myname = "XR"
        self.buttonY_L = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_L, size=bmp_size)
        self.buttonY_L.myname = "YL"
        self.buttonY_R = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_R, size=bmp_size)
        self.buttonY_R.myname = "YR"
        self.buttonX_L.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        self.buttonX_R.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        self.buttonY_L.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        self.buttonY_R.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)

        # Initialize the sizers for layout
        box = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # Display Y coordinate on click
        hbox1.Add(self.lblX, 0, flag=wx.CENTER, border=0)
        hbox1.Add(self.buttonX_L, 0, border=0)
        hbox1.Add(self.pixelTxtX, 0, flag=wx.CENTER, border=5) # Text Control Box
        hbox1.Add(self.buttonX_R, 0, border=0)

        # Horizonal spacer
        hbox1.Add((10, -1))

        # Display Y coordinate on click
        hbox1.Add(self.lblY, 0, flag=wx.CENTER, border=0)
        hbox1.Add(self.buttonY_L, 0, border=0)
        hbox1.Add(self.pixelTxtY, 0, flag=wx.CENTER, border=5) # Text Control Box
        hbox1.Add(self.buttonY_R, 0, border=0)
        
        # Add the hbox1 to the main sizer
        box.Add(hbox1, 0, flag=wx.LEFT|wx.RIGHT|
                    wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)

        # Vertical spacer
        box.Add((-1, 5))
        
        # Add items to the second sizer (hbox2)
        hbox2.Add(self.rgbValue, 5, flag=wx.ALIGN_CENTER, border=5)
        hbox2.Add((10, -1), 0) # Horizonal spacer

        # Small image that shows the color at the selected pixel
        hbox2.Add(self.colorPreview, 1, flag=wx.ALIGN_CENTER, border=5) 

        # Add hbox2 to the main sizer
        box.Add(hbox2, 0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)
        #self.box.Add(self.hbox2, 0, flag=wx.ALIGN_LEFT|wx.ALL, border=1)

        # Vertical spacer
        box.Add((-1, 5))

        self.panel1.SetSizer(box)
        box.Fit(self.panel1)
        self.panel1.Layout()
        self.Show()

    def ImageCtrl_OnMouseClick(self, event):
        """ Gets X and Y coordinates of the selected pixel
            and displays the values on the text control boxes (pixelTxtX & pixelTxtY).
            Then, passes those positions to ColorInfo() to get RGB values
        """
        # Checks if the image exists and left mouse button is pressed
        #if (self.image is not None) and event.LeftIsDown():
        if event.LeftIsDown():
            event.Skip()
            dc = wx.ClientDC(self)
            self.panel2.DoPrepareDC(dc)
            dc_pos = event.GetLogicalPosition(dc)
            del dc
            self.x = int(dc_pos.x / self.ratio)
            self.y = int(dc_pos.y / self.ratio)
            self.isInteger()
            #print(dc_pos, (self.x, self.y))

    def ImageCtrl_OnEnter(self, event):
        """ Gets X and Y coordinates from the user input
            Passes those coordinates onto ColorInfo() to get RGB values
        """
        self.x = int(self.pixelTxtX.GetValue())
        self.y = int(self.pixelTxtY.GetValue())
        self.isInteger()

    def ImageCtrl_OnNavBtn(self, event):
        selectedBtn = event.GetEventObject().myname # Gets the event object's name
        if selectedBtn == "XL":
            self.x = int(self.pixelTxtX.GetValue()) - 1
        elif selectedBtn == "XR":
            self.x = int(self.pixelTxtX.GetValue()) + 1
        elif selectedBtn == "YL":
            self.y = int(self.pixelTxtY.GetValue()) - 1
        elif selectedBtn == "YR":
            self.y = int(self.pixelTxtY.GetValue()) + 1
        self.isInteger()

    def isInteger(self):
        if self.x < 0:
            self.x = 0
        elif self.x >= self.origWidth:
            self.x = self.origWidth - 1
        if self.y < 0:
            self.y = 0
        elif self.y >= self.origHeight:
            self.y = self.origHeight - 1
        self.pixelTxtX.SetValue(str(self.x))
        self.pixelTxtY.SetValue(str(self.y))
        self.ColorInfo()

    def ColorInfo(self):
        """ Takes the X,Y coordinates and return RGB values
            Creates a small color square that shows the color of the selected pixel
        """
        r = self.origImage.GetRed(self.x, self.y)
        g = self.origImage.GetGreen(self.x, self.y)
        b = self.origImage.GetBlue(self.x, self.y)
        self.rgbValue.SetLabel(label=u'R: {} G: {} B: {}  Color at location:'.format(r, g, b))

        # Sets the color of the square image on mouse click
        bmp = wx.Bitmap(self.PaintChipSize, self.PaintChipSize)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        pen = wx.Pen(wx.Colour(0,0,0))
        dc.SetPen(pen)
        brush = wx.Brush(wx.Colour(r,g,b))
        dc.SetBrush(brush)
        dc.DrawRectangle(0, 0, self.PaintChipSize, self.PaintChipSize)
        del dc
        self.colorPreview.SetBitmap(bmp) # Replace the bitmap with the new one
        self.panel1.Layout()

    def onZoom(self,event):
        """ Scale the image by changing the scale factor
        """
        id_selected = event.GetId() # Gets the event id of the selected menu item
        obj = event.GetEventObject() # Gets the event object
        menuitem = obj.GetLabelText(id_selected) # Gets the label text of the menu item
        self.ratio = float(menuitem.replace('%','')) / 100.0
        self.onView()
    
    def onView(self):
        # scale the image, preserving the aspect ratio
        w = int(self.origWidth * self.ratio)
        h = int(self.origHeight * self.ratio)
        self.image = self.origImage.Scale(w, h)
        self.imageCtrl.SetBitmap(wx.Bitmap(self.image))
        #self.panel1.Refresh()
        #self.topPanel.Layout()
        self.panel2.Refresh()
        self.Layout()

    def onAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self, "A simple picture tool", "About the Image Tool", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def onExit(self,e):
        self.Close(True)  # Close the frame.

if __name__ == '__main__':
    usage = "usage: {} file [title]".format(sys.argv[0])
    # Get image file name and optional image title from command line
    if len(sys.argv) == 2:
        filename = title = sys.argv[1]
    elif len(sys.argv) == 3 :
        filename = sys.argv[1]
        title = sys.argv[2]
    else:
        print(usage)
        exit(1)

    if not os.path.isfile(filename):
        print("{} does not exist or is not a file".format(filename))
        print(usage)
        exit(1)

    app = wx.App(False)
    frame = MainWindow(filename=filename, parent=None, title=title)
    frame.Show()
    app.MainLoop()
