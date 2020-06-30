"""Module for choosing and setting file and directory names

   Based on jes/jes/java/FileChooser.java
"""

import os
import JESConfig
import ast
import wx


def pickAFile():
    """Method to let the user pick a file and return the full name as
       as a string.  If the user didn't pick a file then the name
       will be None.

    Returns:
        the file file name of the picked file or None"""
    #return eg.fileopenbox(title="Pick A File")
    frame = wx.Frame(None, -1, 'win.py')
    frame.SetSize(0,0,200,50)

    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Open", "", "", "Python files (*.py)|*.py",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    openFileDialog.ShowModal()
    path = openFileDialog.GetPath()
    openFileDialog.Destroy()
    return path

def pickADirectory():
    """Method to let the user pick a directory and return the full
       path as a string.

    Returns:
        the full directory path"""
    app = wx.App()

    frame = wx.Frame(None, -1, 'pathPicker.py')
    frame.SetSize(0,0,200,50)

    # Create open file dialog
    # openFileDialog = wx.FileDialog(frame, "Open", "", "", "",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    openDirDialog = wx.DirDialog (frame, "Choose input directory", "",wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    openDirDialog.ShowModal()
    path = openDirDialog.GetPath()
    openDirDialog.Destroy()
    JESConfig.CONFIG_MEDIAPATH = path
    JESConfig.writeOrGenerateFromConfig(JESConfig.CONFIG_MEDIAPATH)
    return path


def getMediaPath(fileName):
    """Method to get full path for the passed file name

    Parameters:
        fileName - the name of a file
    Returns:
        the full path for the file
    """
    #return os.path.join(getMediaDirectory(), fileName)
    return os.path.join(JESConfig.CONFIG_MEDIAPATH, fileName)

def getMediaDirectory():
    """Method to get the directory for the media

    Returns:
        the media directory
    """
    return JESConfig.CONFIG_MEDIAPATH

def setMediaPath(directory):
    """Method to set the media path by setting the directory to use

    Parameters:
        directory - the directory to use for the media path
    """
    JESConfig.CONFIG_MEDIAPATH = directory
    JESConfig.writeToConfig(directory)

def pickMediaPath():
    app = wx.App()

    frame = wx.Frame(None, -1, 'pathPicker.py')
    frame.SetSize(0,0,200,50)

    # Create open file dialog
    # openFileDialog = wx.FileDialog(frame, "Open", "", "", "",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    openDirDialog = wx.DirDialog (frame, "Choose input directory", "",wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    openDirDialog.ShowModal()
    path = openDirDialog.GetPath()
    openDirDialog.Destroy()
    JESConfig.CONFIG_MEDIAPATH = path
    JESConfig.writeToConfig(JESConfig.CONFIG_MEDIAPATH)
