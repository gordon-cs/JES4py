# 2020 CS Summer Practicum
# Author: Gahngnin Kim
# Show() accepts PIL image and converts to wxImage, then displays the image

import os
import wx

class ImgConverter(pil_img):
    # Converts PIL image to WX Image
    # Returns wx image
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

class ShowPic(wx_img):
    def __init__(self, parent, title):
        super().__init__()
        MainFrame = wx.Frame.__init__(self, parent, title=title, size=(660,500))

        self.Show(True)