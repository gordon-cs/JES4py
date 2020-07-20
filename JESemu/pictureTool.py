#!/usr/bin/env python3

"""
Simple picture tool to replace JES picture tool
CS Summer Practicum 2020
Author: Gahngnin Kim
Developed under the guidance of Dr. Jonathan Senning
Modified by:
"""

import os
import sys
import wx
import wx.lib.scrolledpanel
# import wx.lib.inspection


class MainWindow(wx.Frame):

    MinWindowWidth = 350
    MinWindowHeight = 0
    ColorPanelHeight = 70
    PaintChipSize = 24
    zoomLevels = [25, 50, 75, 100, 150, 200, 500]
    zoomLevel = float(zoomLevels[3]) / 100.0
    x = 0
    y = 0

    def __init__(self, filename, parent, title):
        # Load image and get image size
        self.image = wx.Image(filename, wx.BITMAP_TYPE_ANY)
        self.bmp = wx.Bitmap(self.image, wx.BITMAP_TYPE_ANY)

        super(MainWindow, self).__init__(parent=parent, title=title, style=wx.DEFAULT_FRAME_STYLE)

        self.InitUI()
        self.Center()
        self.clipOnBoundary()
        # wx.lib.inspection.InspectionTool().Show() # Inspection tool for debugging

    def InitUI(self):
        wScr, hScr = wx.DisplaySize()
        wView, hView = int(wScr * 0.95), int(hScr * 0.85)
        w, h = self.image.GetSize()

        # w = min(max(self.MinWindowWidth, w), wView)
        # h = min(max(self.MinWindowHeight, h + self.ColorPanelHeight), hView)
        w = min(max(self.MinWindowWidth, w), wView)
        h = min(max(self.MinWindowHeight, h + self.ColorPanelHeight), hView)

        # setup the zoom menu
        self.setupZoomMenu()

        # create main sizer
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        # setup the color information panel
        self.setupColorInfoDisplay()
        self.mainSizer.Add(self.colorInfoPanel, 0, wx.EXPAND|wx.ALL, 0)

        # set up the image display panel
        self.setupImageDisplay()
        self.mainSizer.Add(self.imagePanel, 0, wx.EXPAND|wx.ALL, 0)

        self.SetSizer(self.mainSizer)
        # self.SetSize((w, h))
        self.Fit()
        self.imagePanel.SetupScrolling(scrollToTop=True)

        # w, h = self.image.GetSize()
        # h = h + self.ColorPanelHeight
        self.SetSize((w, h))
        self.SetClientSize((w,h))

    def setupZoomMenu(self):
        # Set up zoom menu
        zoomMenu = wx.Menu()
        for z in self.zoomLevels:
            item = "{}%".format(z)
            helpString = "Zoom by {}%".format(z)
            zoomID = zoomMenu.Append(wx.ID_ANY, item, helpString)
            self.Bind(wx.EVT_MENU, self.onZoom, zoomID)

        # menuZoom25 = zoomMenu.Append(wx.ID_ANY, "25%","Zoom by 25%")
        # menuZoom50 = zoomMenu.Append(wx.ID_ANY, "50%","Zoom by 50%")
        # menuZoom75 = zoomMenu.Append(wx.ID_ANY, "75%","Zoom by 75%")
        # menuZoom100 = zoomMenu.Append(wx.ID_ANY, "100%","Zoom by 100%")
        # menuZoom150 = zoomMenu.Append(wx.ID_ANY, "150%","Zoom by 150%")
        # menuZoom200 = zoomMenu.Append(wx.ID_ANY, "200%","Zoom by 200%")
        # menuZoom500 = zoomMenu.Append(wx.ID_ANY, "500%","Zoom by 500%")

        # # Set menu events
        # self.Bind(wx.EVT_MENU, self.onZoom, menuZoom25)
        # self.Bind(wx.EVT_MENU, self.onZoom, menuZoom50)
        # self.Bind(wx.EVT_MENU, self.onZoom, menuZoom75)
        # self.Bind(wx.EVT_MENU, self.onZoom, menuZoom100)
        # self.Bind(wx.EVT_MENU, self.onZoom, menuZoom150)
        # self.Bind(wx.EVT_MENU, self.onZoom, menuZoom200)
        # self.Bind(wx.EVT_MENU, self.onZoom, menuZoom500)
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(zoomMenu, "&Zoom") # Adds the "zoomMenu" to the MenuBar
        self.SetMenuBar(menuBar) # Adds the MenuBar to the Frame content.

    def setupColorInfoDisplay(self):
        self.colorInfoPanel = wx.Panel(parent=self, size=(-1, self.ColorPanelHeight))

        # Create main sizer for this color info panel
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        # ---- First row ----

        # Create sizer to hold components
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)

        # X and Y labels
        lblX = wx.StaticText(self.colorInfoPanel, 0, style=wx.ALIGN_CENTER)
        lblY = wx.StaticText(self.colorInfoPanel, 0, style=wx.ALIGN_CENTER)
        lblX.SetLabel("X: ")
        lblY.SetLabel("Y: ")
    
        # Navigation buttons (Enable after getting the colorpicker/eyedropper functional)
        # Icons made by Freepik from www.flaticon.com; Modified by Gahngnin Kim
        img_R = os.path.join(sys.path[0], 'images', 'Right.png')
        img_L = os.path.join(sys.path[0], 'images', 'Left.png')
        bmp_R = wx.Bitmap(img_R, wx.BITMAP_TYPE_ANY)
        bmp_L = wx.Bitmap(img_L, wx.BITMAP_TYPE_ANY)
        bmp_size = (bmp_L.GetWidth()+5,bmp_L.GetHeight()+5)
        buttonX_L = wx.BitmapButton(self.colorInfoPanel, wx.ID_ANY, bitmap=bmp_L, size=bmp_size)
        buttonX_L.myname = "XL"
        buttonX_R = wx.BitmapButton(self.colorInfoPanel, wx.ID_ANY, bitmap=bmp_R, size=bmp_size)
        buttonX_R.myname = "XR"
        buttonY_L = wx.BitmapButton(self.colorInfoPanel, wx.ID_ANY, bitmap=bmp_L, size=bmp_size)
        buttonY_L.myname = "YL"
        buttonY_R = wx.BitmapButton(self.colorInfoPanel, wx.ID_ANY, bitmap=bmp_R, size=bmp_size)
        buttonY_R.myname = "YR"
        buttonX_L.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        buttonX_R.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        buttonY_L.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)
        buttonY_R.Bind(wx.EVT_BUTTON, self.ImageCtrl_OnNavBtn)

        # Textboxes to display X and Y coordinates on click
        self.pixelTxtX = wx.TextCtrl(self.colorInfoPanel, wx.ALIGN_CENTER, \
            style=wx.TE_PROCESS_ENTER, size=(50,-1))
        self.pixelTxtY = wx.TextCtrl(self.colorInfoPanel, wx.ALIGN_CENTER, \
            style=wx.TE_PROCESS_ENTER, size=(50,-1))
        self.pixelTxtX.Bind(wx.EVT_TEXT_ENTER, self.ImageCtrl_OnEnter)
        self.pixelTxtY.Bind(wx.EVT_TEXT_ENTER, self.ImageCtrl_OnEnter)

        # Add first row components to sizer
        # X coordinate display
        sizer1.Add(lblX, 0, flag=wx.CENTER, border=0)
        sizer1.Add(buttonX_L, 0, border=0)
        sizer1.Add(self.pixelTxtX, 0, flag=wx.CENTER, border=5) # Text Control Box
        sizer1.Add(buttonX_R, 0, border=0)

        # Horizonal spacer
        sizer1.Add((5, -1))

        # Y coordinate display
        sizer1.Add(lblY, 0, flag=wx.CENTER, border=0)
        sizer1.Add(buttonY_L, 0, border=0)
        sizer1.Add(self.pixelTxtY, 0, flag=wx.CENTER, border=5) # Text Control Box
        sizer1.Add(buttonY_R, 0, border=0)
        
        # Add first row sizer to the main sizer
        mainSizer.Add(sizer1, 0, flag=wx.LEFT|wx.RIGHT|
                    wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)

        # Vertical spacer
        mainSizer.Add((-1, 5))

        # ---- Second row ----

        # Create sizer to hold components
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        # Static text displays RGB values of the given coordinates
        # Initialized with dummie values
        self.rgbValue = wx.StaticText(self.colorInfoPanel, label=u'')#, style=wx.ALIGN_CENTER)
        font = self.rgbValue.GetFont()
        font.PointSize += 2
        self.rgbValue.Font = font

        # initialize an empty bitmap
        bmp = wx.Bitmap(self.PaintChipSize, self.PaintChipSize)
        self.colorPreview = wx.StaticBitmap(parent=self.colorInfoPanel, bitmap=bmp)

        # Add items to the second sizer (sizer2)
        sizer2.Add(self.rgbValue, 0, flag=wx.ALIGN_CENTER, border=5)

        # Horizontal spacer
        sizer2.Add((10, -1), 0)

        # Small image that shows the color at the selected pixel
        sizer2.Add(self.colorPreview, 0, flag=wx.ALIGN_CENTER, border=5) 

        # Add sizer2 to the main sizer
        mainSizer.Add(sizer2, 0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=1)

        # Vertical spacer
        mainSizer.Add((-1, 5))

        self.colorInfoPanel.SetSizer(mainSizer)
        #mainSizer.Fit(panel)
        #panel.Layout()
        #self.Show()

    def setupImageDisplay(self):
        """Set up image display panel
        """
        # Get image size and make scrolled panel large enough to hold image
        # even with maximum zoom
        w, h = self.image.GetSize()
        maxZoomLevel = int(int(self.zoomLevels[-1]) / 100)
        maxSize = (maxZoomLevel * w, maxZoomLevel * h)
    
        # Create a scrolled panel to hold the image
        self.imagePanel = wx.lib.scrolledpanel.ScrolledPanel(parent=self, size=maxSize, style=wx.NO_BORDER)

        # Store the image and setup even handlers for mouse clicks and motion
        self.imageCtrl = wx.StaticBitmap(parent=self.imagePanel, bitmap=self.bmp)
        if wx.Platform == "__WXMSW__" or wx.Platform == "__WXGTK__":
            self.imageCtrl.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)
            self.imageCtrl.Bind(wx.EVT_MOTION, self.ImageCtrl_OnMouseClick)
            #self.imageCtrl.Bind(wx.EVT_LEFT_UP, self.OnPaint)
        elif wx.Platform == "__WXMAC__":
            self.imagePanel.Bind(wx.EVT_LEFT_DOWN, self.ImageCtrl_OnMouseClick)
            self.imagePanel.Bind(wx.EVT_MOTION, self.ImageCtrl_OnMouseClick) 
            #self.imagePanel.Bind(wx.EVT_LEFT_UP, self.OnPaint)
        #panel.SetFocus()
        #panel.Bind(wx.EVT_LEFT_DOWN, self.onFocus)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.imageCtrl, 0, wx.ALIGN_LEFT|wx.ALIGN_TOP|wx.ALL, 0)
        self.imagePanel.SetSizer(mainSizer)
        self.mainSizer.Fit(self.imagePanel)
        self.imagePanel.SetupScrolling(scrollToTop=True)
        #return panel

    def clipOnBoundary(self):
        """Clips x and y to be valid pixel coordinates

        Ensures that the current values of x and y are valid pixel
        coordinates for the image

        Modifies
        --------
        self.x, self.y : int
            the pixel coordinates
        self.pixelTxtX, self.pixelTxtY : wx.TextCtrl
            the textboxes displaying the pixel coordinates
        """
        imageSize = self.image.GetSize()
        #print('image size: ', imageSize)
        if self.x < 0:
            self.x = 0
            self.y = 0
        elif self.x >= imageSize[0]:
            self.x = imageSize[0] - 1
            self.y = imageSize[1] - 1
        if self.y < 0:
            self.x = 0
            self.y = 0
        elif self.y >= imageSize[1]:
            self.y = imageSize[1] - 1
            self.x = imageSize[0] - 1
        self.pixelTxtX.SetValue(str(self.x))
        self.pixelTxtY.SetValue(str(self.y))
        self.updateColorInfo()

    def updateColorInfo(self):
        """Updates the color patch in the color information display

        The color patch is a small square image with a black outline and
        interior color matching that corresponding to the most-recently
        selected pixel in the image.
        """
        r = self.image.GetRed(self.x, self.y)
        g = self.image.GetGreen(self.x, self.y)
        b = self.image.GetBlue(self.x, self.y)
        self.rgbValue.SetLabel(label=u'R: {} G: {} B: {}  Color at location:'.format(r, g, b))

        # Sets the color of the square image on mouse click
        bmp = wx.Bitmap(self.PaintChipSize, self.PaintChipSize)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        pen = wx.Pen(wx.Colour(0,0,0)) # black for outline
        dc.SetPen(pen)
        brush = wx.Brush(wx.Colour(r,g,b)) # current image pixel color
        dc.SetBrush(brush)
        dc.DrawRectangle(0, 0, self.PaintChipSize, self.PaintChipSize)
        del dc
        self.colorPreview.SetBitmap(bmp) # Replace the bitmap with the new one
        self.colorInfoPanel.Layout()

    def updateView(self):
        """Scale image according to the zoom factor and (re)display it
        """
        imageSize = self.image.GetSize()
        w = int(imageSize[0] * self.zoomLevel)
        h = int(imageSize[1] * self.zoomLevel)
        image = self.image.Scale(w, h)
        self.bmp = wx.Bitmap(image, wx.BITMAP_TYPE_ANY)
        self.imageCtrl.SetBitmap(self.bmp)

    def drawCrosshairs(self):
        """Draw image with crosshairs to indicate selected position
        """
        dc = wx.ClientDC(self.imageCtrl)
        origin = dc.GetDeviceOrigin()
        scrolledPosition = self.imagePanel.CalcScrolledPosition(origin)
        x = int(self.x * self.zoomLevel) + scrolledPosition[0]
        y = int(self.y * self.zoomLevel) + scrolledPosition[1]
        dc.DrawBitmap(self.bmp, scrolledPosition, False)
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0), 1, wx.DOT))
        dc.CrossHair(x, y)

# ===========================================================================
# Event handlers
# ===========================================================================

    def onFocus(self, event):
        self.imagePanel.SetFocus()

    def onZoom(self, event):
        """Sets desired zoom level and updates image display

        (Zoom event handler)
        """
        id_selected = event.GetId() # Gets the event id of the selected menu item
        obj = event.GetEventObject() # Gets the event object
        menuItem = obj.GetLabelText(id_selected) # Gets the label text of the menu item
        self.zoomLevel = float(menuItem.replace('%','')) / 100.0
        self.x = self.y = 0
        self.imagePanel.Scroll(self.x, self.y) # "non-scrolled" position
        self.PostSizeEvent()
        self.clipOnBoundary()
        self.updateView()

    def ImageCtrl_OnNavBtn(self, event):
        """Increment or decrement x or y pixel coordinate
        """
        selectedBtn = event.GetEventObject().myname
        if selectedBtn == "XL":
            self.x = int(self.pixelTxtX.GetValue()) - 1
        elif selectedBtn == "XR":
            self.x = int(self.pixelTxtX.GetValue()) + 1
        elif selectedBtn == "YL":
            self.y = int(self.pixelTxtY.GetValue()) - 1
        elif selectedBtn == "YR":
            self.y = int(self.pixelTxtY.GetValue()) + 1
        self.clipOnBoundary()
        self.drawCrosshairs()

    def ImageCtrl_OnEnter(self, event):
        """Adjusts x and y pixel values to match displayed values
        """
        self.x = int(self.pixelTxtX.GetValue())
        self.y = int(self.pixelTxtY.GetValue())
        self.clipOnBoundary()
        self.drawCrosshairs()

    def ImageCtrl_OnMouseClick(self, event):
        """Update x and y pixel coordinates from pointer location
        """
        if event.LeftIsDown():
            event.Skip()
            dc = wx.ClientDC(self)
            self.imagePanel.DoPrepareDC(dc)
            if wx.Platform == "__WXMSW__":
                dc_pos = event.GetPosition()
            elif wx.Platform == "__WXGTK__" or wx.Platform == "__WXMAC__":
                dc_pos = event.GetLogicalPosition(dc)
            self.coordinates = dc_pos
            del dc
            self.x = int(dc_pos.x / self.zoomLevel)
            self.y = int(dc_pos.y / self.zoomLevel)
            self.clipOnBoundary()
            self.drawCrosshairs()

# ===========================================================================
# Main program
# ===========================================================================

def main(argv):

    usage = "usage: {} file [title]".format(argv[0])
    # Get image file name and optional image title from command line
    if len(argv) == 2:
        filename = title = argv[1]
    elif len(argv) == 3:
        filename = argv[1]
        title = argv[2]
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

if __name__ == '__main__':
    main(sys.argv)
