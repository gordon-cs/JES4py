#!/usr/bin/env python3

"""
filechooser.py - Script to use wxPython to select a file or folder.

Written: 2021-02-06 Jonathan R. Senning <jonathan.senning@gordon.edu>
Derived from method written by Gahngnin Kim and Jonathan Senning in 2020.
"""

import wx
import sys

def fileDialog(defaultFolder):
    """Use system-dependant file dialog to select a file path.
    
    Lets user pick a file and return the full path as as a string.
    If the user does not pick a file then the path will be None.

    Args:
        defaultFolder (string): initial folder to start search

    Returns:
        the file file name of the picked file or None
    """
    app = wx.App()
    frame = wx.Frame(None, -1, 'PickAFile')

    # Create open file dialog
    path = None
    openFileDialog = wx.FileDialog(frame, 'Pick A File', defaultFolder,
        "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    if openFileDialog.ShowModal() == wx.ID_OK:
        path = openFileDialog.GetPath()
    
    # Clean up
    openFileDialog.Destroy()
    return path

def folderDialog(defaultFolder):
    """Use system-dependant file dialog to select a folder path.
    
    Lets user pick a directory and return the full path as a string.
    If the user does not pick a file then the path will be None.

    Args:
        defaultFolder (string): initial folder to start search

    Returns:
        the full directory path
    """
    app = wx.App()
    frame = wx.Frame(None, -1, 'pickADirectory')

    # Create open file dialog
    path = None
    openDirDialog = wx.DirDialog(frame, 'Pick A Folder', defaultFolder,
        wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    if openDirDialog.ShowModal() == wx.ID_OK:
        path = openDirDialog.GetPath()

    # Clean up
    openDirDialog.Destroy()
    return path

def main(argv):
    """Main program.
    """
    if len(argv) == 3:
        path = None
        if argv[1].lower() == 'file':
            path = fileDialog(argv[2])
        elif argv[1].lower() == 'folder':
            path = folderDialog(argv[2])
        if path is not None:
            print(path, end='')
    else:
        print('usage: {} "file"|"folder" start_path'.format(argv[0]))

if __name__ == '__main__':
    main(sys.argv)
