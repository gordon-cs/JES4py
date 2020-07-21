"""Module for choosing and setting file and directory names

   Based on jes/jes/java/FileChooser.java
"""

import os
import wx
from jes4py import Config

def pickAFile():
    """Method to let the user pick a file and return the full name as
       as a string.  If the user didn't pick a file then the name
       will be None.

    Returns:
        the file file name of the picked file or None"""
    app = wx.App()

    frame = wx.Frame(None, -1, 'PickAFile')
    frame.SetSize(0,0,200,50)

    # Create open file dialog
    directory = Config.getConfigVal('CONFIG_SESSION_PATH')
    openFileDialog = wx.FileDialog(frame, "Pick A File", directory, "", "", 
        wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    if openFileDialog.ShowModal() == wx.ID_CANCEL:
        return ""
    else:
        path = openFileDialog.GetPath()
        Config.setConfigVal('CONFIG_SESSION_PATH',os.path.dirname(path))
        openFileDialog.Destroy()
        return path

def pickADirectory():
    """Method to let the user pick a directory and return the full
       path as a string.

    Returns:
        the full directory path"""
    app = wx.App()

    frame = wx.Frame(None, -1, 'pickADirectory')
    frame.SetSize(0,0,200,50)

    # Create open file dialog
    directory = Config.getConfigVal('CONFIG_SESSION_PATH')
    openDirDialog = wx.DirDialog(frame, "Pick A Folder", directory,
        wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    if openDirDialog.ShowModal() == wx.ID_CANCEL:
        return ""
    else:
        path = openDirDialog.GetPath()
        openDirDialog.Destroy()
        Config.setConfigVal('CONFIG_SESSION_PATH',path)
        return path

def getMediaPath(fileName):
    """Method to get full path for the passed file name

    Parameters:
        fileName - the name of a file
    Returns:
        the full path for the file
    """
    return os.path.join(Config.getConfigVal("CONFIG_MEDIA_PATH"), fileName)

def getMediaDirectory():
    """Method to get the directory for the media

    Returns:
        the media directory
    """
    return Config.getConfigVal("CONFIG_MEDIA_PATH")

def setMediaPath(directory):
    """Method to set the media path by setting the directory to use

    Parameters:
        directory - the directory to use for the media path
    """
    Config.setConfigVal("CONFIG_MEDIA_PATH", directory)

def pickMediaPath():
    path = pickADirectory()
    Config.setConfigVal("CONFIG_MEDIA_PATH", path)
