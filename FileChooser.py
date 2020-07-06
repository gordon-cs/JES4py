"""Module for choosing and setting file and directory names

   Based on jes/jes/java/FileChooser.java
"""

import os
import JESConfig
import wx


def pickAFile():
    """Method to let the user pick a file and return the full name as
       as a string.  If the user didn't pick a file then the name
       will be None.

    Returns:
        the file file name of the picked file or None"""
    #return eg.fileopenbox(title="Pick A File")
    app = wx.App()

    frame = wx.Frame(None, -1, 'filePicker.py')
    frame.SetSize(0,0,200,50)

    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Pick A File",  JESConfig.getConfigVal('CONFIG_MEDIAPATH'), "", "",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
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
    openDirDialog = wx.DirDialog (frame, "Pick A Folder", JESConfig.getConfigVal('CONFIG_MEDIAPATH'), wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    openDirDialog.ShowModal()
    path = openDirDialog.GetPath()
    openDirDialog.Destroy()
    return path


def getMediaPath(fileName):
    """Method to get full path for the passed file name

    Parameters:
        fileName - the name of a file
    Returns:
        the full path for the file
    """
    #return os.path.join(getMediaDirectory(), fileName)
    return os.path.join(JESConfig.getConfigVal("CONFIG_MEDIAPATH"), fileName)

def getMediaDirectory():
    """Method to get the directory for the media

    Returns:
        the media directory
    """
    return JESConfig.getConfigVal("CONFIG_MEDIAPATH")

def setMediaPath(directory):
    """Method to set the media path by setting the directory to use

    Parameters:
        directory - the directory to use for the media path
    """
    JESConfig.setConfigVal("CONFIG_MEDIAPATH", directory)

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
    JESConfig.setConfigVal("CONFIG_MEDIAPATH", path)
