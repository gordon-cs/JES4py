import os

import wx
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