#!/usr/bin/env python3

"""
colorPicker.py - Script to use wxPython to allow user to select color.

Written: 2021-02-06 Jonathan R. Senning <jonathan.senning@gordon.edu>
Derived from method written by Gahngnin Kim and Jonathan Senning in 2020.
"""

import tkinter as tk
import tkinter.colorchooser

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.pickAColor()
        self.quit()

    def pickAColor(self):
        (rgb, hexstr) = tk.colorchooser.askcolor(title='Pick A Color')
        if rgb is not None:
            print(rgb[0], rgb[1], rgb[2], end='')

    def quit(self):
        self.root.destroy()

if __name__ == '__main__':
    app = App()
