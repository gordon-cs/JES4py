#!/usr/bin/env python3

"""
colorchooser.py - Script to use wxPython to allow user to select color.

Written: 2021-02-06 Jonathan R. Senning <jonathan.senning@gordon.edu>
Derived from method written by Gahngnin Kim and Jonathan Senning in 2020.
"""

import wx

def chooseColor():
    """Use system-dependent color chooser dialog to select color.

    Returns:
        RGB tuple or None.
    """
    app = wx.App()

    # setup defaults
    data = wx.ColourData()
    if wx.Platform == "__WXMAC__":
        data.SetChooseAlpha(False)
    data.SetChooseFull(True)
    data.SetColour(wx.WHITE) # show colors on initial color wheel on mac

    # start and process the dialog
    color = None
    dlg = wx.ColourDialog(wx.GetApp().GetTopWindow(), data)
    if dlg.ShowModal() == wx.ID_OK:
        red   = dlg.GetColourData().GetColour().Red()
        green = dlg.GetColourData().GetColour().Green()
        blue  = dlg.GetColourData().GetColour().Blue()
        color = (red, green, blue)

    # clean up
    dlg.Destroy()
    return color

if __name__ == '__main__':
    color = chooseColor()
    if color is not None:
        print(color[0], color[1], color[2], end='')
