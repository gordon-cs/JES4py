# Simple picture tool to replace JES picture tool
# CS Summer Practicum 2020
# Author: Gahngnin Kim

import os, sys
import wx
import wx.lib.scrolledpanel as scrolled
# import wx.lib.inspection

class MainWindow(wx.Frame):
    def __init__(self, filename, parent=None, id=-1, pos=wx.DefaultPosition, title=None):
        #First retrieve the screen size of the device
        screenSize = wx.DisplaySize()
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]

        self.origImage = wx.Image(filename, wx.BITMAP_TYPE_ANY)
        self.ratio = 1.0  # Scale factor
        self.size = (self.origImage.GetWidth(), self.origImage.GetHeight())
        MainFrame = wx.Frame.__init__(self, parent, title=title, size=self.size)
        self.panel1 = wx.Panel(self,size=(self.size[0],100), pos=(0,0), style=wx.SIMPLE_BORDER)
        self.panel2 = scrolled.ScrolledPanel(self,-1, size=(self.size[0],400), pos=(0,55), style=wx.SIMPLE_BORDER)
        self.panel2.SetupScrolling()
        # wx.lib.inspection.InspectionTool().Show() # Inspection tool for debugging
        
        # Maximum horizontal dimension. Needs to be removed later.
        #self.PhotoMaxSize = 600

        # Initialize a buffer image
        self.image = None

        self.ColorPicker() # Color Eyedropper
        self.viewingWindow() # Image viewer
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        #self.SetClientSize(self.size)

        # Setting up the menu bar
        self.filemenu = wx.Menu()

        # Setting up the menu items
        # Standard ID given to each item are provided by wxWidgets.
        menuZoom25 = self.filemenu.Append(wx.ID_ANY, "25%","Zoom by 25%")
        menuZoom50 = self.filemenu.Append(wx.ID_ANY, "50%","Zoom by 50%")
        menuZoom75 = self.filemenu.Append(wx.ID_ANY, "75%","Zoom by 75%")
        menuZoom100 = self.filemenu.Append(wx.ID_ZOOM_100, "100%","Zoom by 100% (original size)")
        menuZoom150 = self.filemenu.Append(wx.ID_ANY, "150%","Zoom by 150%")
        menuZoom200 = self.filemenu.Append(wx.ID_ANY, "200%","Zoom by 200%")
        menuZoom500 = self.filemenu.Append(wx.ID_ANY, "500%","Zoom by 500%")
        #self.filemenu.AppendSeparator()
        #menuAbout = self.filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        #self.filemenu.AppendSeparator()
        #menuExit = self.filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        

        # Set events
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom25)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom50)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom75)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom100)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom150)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom200)
        self.Bind(wx.EVT_MENU, self.onZoom, menuZoom500)
        #self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        #self.Bind(wx.EVT_MENU, self.onExit, menuExit)

        self.x = 0
        self.y = 0
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(self.filemenu,"&Zoom") # Adds the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar) # Adds the MenuBar to the Frame content.
        self.Show(True)
        self.onView()
        self.isInteger()

    def viewingWindow(self):
        """ Main image viewing window
        """
        # initialize an empty image
        wxImg = self.origImage #wx.Image(self.size[0], self.size[1]) # wx.Image(width, height, clear)

        # Convert the image into a bitmap image
        self.imageCtrl = wx.StaticBitmap(self.panel2, wx.ID_ANY, wx.Bitmap(wxImg))

        # Event handler - Gets X, Y coordinates on mouse click
        self.imageCtrl.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)
        self.imageCtrl.Bind(wx.EVT_MOTION, self.ImageCtrl_OnMouseClick)

        # Stores the filepath of the image
        self.photoTxt = wx.TextCtrl(self.panel2, size=(200,-1))
        self.photoTxt.Show(False)
        
        #########LAYOUT SETUP###########
        # Initialize vertical and horizontal boxsizers
        mainSizer = wx.BoxSizer(wx.VERTICAL) # Main vertical boxsizer
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # Vertical spacer
        mainSizer.Add((-1, 50))

        # Draws a horizontal line
        mainSizer.Add(wx.StaticLine(self.panel2, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        
        # Places components to the sizers
        mainSizer.Add(self.imageCtrl, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5)
        hSizer.Add(self.photoTxt, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)

        # Set the main sizer to fit the top level panel
        #self.panel.SetSizer(mainSizer)
        mainSizer.Fit(self.panel2)
    
    def ColorPicker(self):
        """ Reads color information from the selected pixel.
            Displays X and Y coordinates, RGB values, and the color of the pixel.
            The user can select the pixel by directly clicking on it OR
            by typing a specific coordinate.
        """
        # initialize an empty bitmap
        self.bmp = wx.Bitmap(20,20)
        self.colorPreview = wx.StaticBitmap(self.panel1, wx.ID_ANY, self.bmp)
        self.colorPreview.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)

        # Textboxes to display X and Y coordinates on click
        self.pixelTxtX = wx.TextCtrl(self.panel1, wx.ALIGN_CENTER, style=wx.TE_PROCESS_ENTER, size=(50,-1))
        self.pixelTxtY = wx.TextCtrl(self.panel1, wx.ALIGN_CENTER, style=wx.TE_PROCESS_ENTER, size=(50,-1))
        self.pixelTxtX.Bind(wx.EVT_TEXT_ENTER, self.ImageCtrl_OnEnter)
        self.pixelTxtY.Bind(wx.EVT_TEXT_ENTER, self.ImageCtrl_OnEnter)

        # Static text displays RGB values of the given coordinates
        # Initialized with dummie values
        self.rgbValue = wx.StaticText(self.panel1, label=u'R: {} G: {} B: {} Color at location:'.format("N/A", "N/A", "N/A"),style = wx.ALIGN_CENTER)

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
        self.buttonX_L = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_L, size=(bmp_L.GetWidth()+5,bmp_L.GetHeight()+5))
        self.buttonX_L.myname = "XL"
        self.buttonX_R = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_R, size=(bmp_L.GetWidth()+5,bmp_L.GetHeight()+5))
        self.buttonX_R.myname = "XR"
        self.buttonY_L = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_L, size=(bmp_L.GetWidth()+5,bmp_L.GetHeight()+5))
        self.buttonY_L.myname = "YL"
        self.buttonY_R = wx.BitmapButton(self.panel1, wx.ID_ANY, bitmap=bmp_R, size=(bmp_L.GetWidth()+5,bmp_L.GetHeight()+5))
        self.buttonY_R.myname = "YR"
        self.buttonX_L.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        self.buttonX_R.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        self.buttonY_L.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        self.buttonY_R.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)

        # Initialize the sizers for layout
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # Display Y coordinate on click
        self.hbox1.Add(self.lblX, 0, flag=wx.CENTER, border=0)
        self.hbox1.Add(self.buttonX_L, 0, border=0)
        self.hbox1.Add(self.pixelTxtX, 0, flag=wx.CENTER, border=5) # Text Control Box
        self.hbox1.Add(self.buttonX_R, 0, border=0)

        # Horizonal spacer
        self.hbox1.Add((10, -1))

        # Display Y coordinate on click
        self.hbox1.Add(self.lblY, 0, flag=wx.CENTER, border=0)
        self.hbox1.Add(self.buttonY_L, 0, border=0)
        self.hbox1.Add(self.pixelTxtY, 0, flag=wx.CENTER, border=5) # Text Control Box
        self.hbox1.Add(self.buttonY_R, 0, border=0)
        
        # Add the hbox1 to the main sizer
        self.box.Add(self.hbox1, 0, flag=wx.LEFT|wx.RIGHT|
                    wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)

        # Vertical spacer
        self.box.Add((-1, 5))
        
        # Add items to the second sizer (hbox2)
        self.hbox2.Add(self.rgbValue, 0, border=5)
        self.hbox2.Add((5, -1)) # Horizonal spacer

        # Small image that shows the color at the selected pixel
        self.hbox2.Add(self.colorPreview, 0, border=5) 
        
        # Add hbox2 to the main sizer
        self.box.Add(self.hbox2, 0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)


        self.panel1.SetSizer(self.box)
        self.box.Fit(self.panel1)
        self.panel1.Layout()
        self.Show()

    def ImageCtrl_OnMouseClick(self, event):
        """ Gets X and Y coordinates of the selected pixel
            and displays the values on the text control boxes (pixelTxtX & pixelTxtY).
            Then, passes those positions to ColorInfo() to get RGB values
        """
        # Checks if the image exists before executing the next function
        if self.image is not None:
            # Check if the mouse is dragged
            if event.LeftIsDown():
                ctrl_pos = event.GetPosition()
                self.x = ctrl_pos.x
                self.y = ctrl_pos.y
                self.pixelTxtX.SetValue(str(self.x))
                self.pixelTxtY.SetValue(str(self.y))
                self.ColorInfo()
                # self.imageCtrl.Bind(wx.EVT_PAINT, self.CursorOnImage)
            else:
                "" # Do nothing if mouse left button is not pressed and hold
        else:
            "" # Do nothing if self.image is None

    def ImageCtrl_OnEnter(self, event):
        """ Gets X and Y coordinates from the user input
            Passes those coordinates onto ColorInfo() to get RGB values
        """
        self.x = self.pixelTxtX.GetValue()
        self.y = self.pixelTxtY.GetValue()
        self.ColorInfo()

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
        else:
            ""
        self.isInteger()

    def isInteger(self):
        currentX = self.x
        currentY = self.y
        w = int(self.ScaledW)
        h = int(self.ScaledH)
        if currentX < 0:
            self.x = 0
            self.pixelTxtX.SetValue(str(self.x))
        elif currentX >= w:
            self.x = w - 1
            self.pixelTxtX.SetValue(str(self.x))
        elif currentY < 0:
            self.y = 0
            self.pixelTxtY.SetValue(str(self.y))
        elif currentY >= h:
            self.y = h - 1
            self.pixelTxtY.SetValue(str(self.y))
        else:
            self.pixelTxtX.SetValue(str(self.x))
            self.pixelTxtY.SetValue(str(self.y))
        self.ColorInfo()
        

    def ColorInfo(self):
        """ Takes the X,Y coordinates and return RGB values
            Creates a small color square that shows the color of the selected pixel
        """
        r = self.image.GetRed(int(self.x), int(self.y))
        g = self.image.GetGreen(int(self.x), int(self.y))
        b = self.image.GetBlue(int(self.x), int(self.y))
        self.rgbValue.SetLabel(label=u'R: {} G: {} B: {} Color at location:'.format(r, g, b))

        # Sets the color of the square image on mouse click
        bmp = wx.Bitmap(20,20) # Empty bitmap image initialized
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(wx.Colour(r,g,b), wx.SOLID)) # Sets the color
        dc.Clear()
        del dc

        self.colorPreview.SetBitmap(bmp) # Replace the bitmap with the new one
        self.Refresh() # Updates the static bitmap
    
    # def CursorOnImage(self, event):
    #     dc = wx.PaintDC(self)
    #     dc.Clear()
    #     dc.SetPen(wx.Pen(wx.Black, 4))
    #     dc.DrawLine((self.x-5),self.y, (self.x+5), self.y)

    def onZoom(self,event):
        """ Scale the image by changing the scale factor
        """
        id_selected = event.GetId() # Gets the event id of the selected menu item
        obj = event.GetEventObject() # Gets the event object
        menuitem = obj.GetLabelText(id_selected) # Gets the label text of the menu item
        self.ratio = float(menuitem.replace('%',''))/100.0
        # if menuitem == "25%":
        #     self.ratio = 0.25
        # elif menuitem == "50%":
        #     self.ratio = 0.50
        # elif menuitem == "75%":
        #     self.ratio = 0.75
        # elif menuitem == "100%":
        #     self.ratio = 1.00
        # elif menuitem == "150%":
        #     self.ratio = 1.50
        # elif menuitem == "200%":
        #     self.ratio = 2.00
        # else:
        #     self.ratio = 5.00
        self.onView()
    
    def onView(self):
        # scale the image, preserving the aspect ratio
        W = self.origImage.GetWidth()
        H = self.origImage.GetHeight()
        # if W > H:
        #     NewW = self.PhotoMaxSize
        #     NewH = self.PhotoMaxSize * H / W
        # else:
        #     NewH = self.PhotoMaxSize
        #     NewW = self.PhotoMaxSize * W / H

        # self.ScaledW = NewW * self.ratio
        # self.ScaledH = NewH * self.ratio
        self.ScaledW = W * self.ratio
        self.ScaledH = H * self.ratio

        self.image = self.origImage.Scale(int(self.ScaledW),int(self.ScaledH))
        self.imageCtrl.SetBitmap(wx.Bitmap(self.image))
        self.panel1.Refresh()

    def onAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A simple picture tool", "About the Image Tool", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def onExit(self,e):
        self.Close(True)  # Close the frame.

if __name__ == '__main__':
    # Get image file name and optional image title from command line
    if len(sys.argv) == 2:
        filename = title = sys.argv[1]
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        title = sys.argv[2]
    else:
        print("usage: {} file title".format(sys.argv[0]))
        exit(1)

    app = wx.App(False)
    frame = MainWindow(filename=filename, parent=None, title=title)
    app.MainLoop()
