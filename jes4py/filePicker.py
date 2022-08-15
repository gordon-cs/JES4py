#!/usr/bin/env python3

"""
filePicker.py - Script to use tkinter to select a file or folder.

Written: 2022-06-21 Jonathan R. Senning <jonathan.senning@gordon.edu>
Derived from method using wxPython written by Gahngnin Kim 
and Jonathan Senning in 2020.
"""
import tkinter as tk
import tkinter.filedialog
import sys

class App():
    def __init__(self, argv):
        self.root = tk.Tk()
        # Disable hidden files and folders.  This is done by setting an
        # internal tk variable, but do this we first need to dialog object
        # to be created.  Unfortunately we need to set the variable before
        # showing the dialog object we want displayed.  So, we will create
        # a dialog object with an impossible option and catch and ignore the
        # error. Then we set two variables: one to show a button that allows
        # the user to see or not see hidden files & folders and another to
        # determine the initial state of this button (we want it off).  See
        # the following for more information.
        # https://stackoverflow.com/questions/53220711/how-to-avoid-hidden-files-in-file-picker-using-tkinter-filedialog-askopenfilenam
        try:
            self.root.tk.call('tk_getOpenFile', '-impossible-option')
        except tk.TclError:
            pass
        self.root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
        self.root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')

        # Don't display root window
        self.root.withdraw()

        # Determine what is requested and show the dialog
        if len(argv) == 3:
            path = None
            if argv[1].lower() == 'file':
                path = self.fileDialog(argv[2])
            elif argv[1].lower() == 'folder':
                path = self.folderDialog(argv[2])
            if path is not None:
                print(path, end='')
        else:
            print('usage: {} "file"|"folder" start_path'.format(argv[0]))

        # Clean up
        self.quit()

    def fileDialog(self, defaultFolder):
        """Use system-dependant file dialog to select a file path.
    
        Lets user pick a file and return the full path as as a string.
        If the user does not pick a file then the path will be None.

        Args:
            defaultFolder (string): initial folder to start search

        Returns:
            the file name of the picked file or None
        """
        name = tk.filedialog.askopenfilename(title='Pick A File',
                                             initialdir=defaultFolder)
        if isinstance(name, str):
            return name
        else:
            return None

    def folderDialog(self, defaultFolder):
        """Use system-dependant file dialog to select a folder path.

        Lets user pick a directory and return the full path as a string.
        If the user does not pick a file then the path will be None.

        Args:
            defaultFolder (string): initial folder to start search

        Returns:
            the full directory path
        """
        name = tk.filedialog.askdirectory(title='Pick A Folder',
                                          initialdir=defaultFolder)
        if isinstance(name, str):
            return name
        else:
            return None

    def quit(self):
        self.root.destroy()

if __name__ == '__main__':
    app = App(sys.argv)
