"""Module for choosing and setting file and directory names

   Based on jes/jes/java/FileChooser.java
"""

import os
import easygui as eg
import JESConfig
import ast


def pickAFile():
    """Method to let the user pick a file and return the full name as
       as a string.  If the user didn't pick a file then the name
       will be None.

    Returns:
        the file file name of the picked file or None"""
    return eg.fileopenbox(title="Pick A File")

def pickADirectory():
    """Method to let the user pick a directory and return the full
       path as a string.

    Returns:
        the full directory path"""
    return eg.diropenbox(title="Pick A Folder")

def getMediaPath(fileName):
    """Method to get full path for the passed file name

    Parameters:
        fileName - the name of a file
    Returns:
        the full path for the file
    """
    return os.path.join(getMediaDirectory(), fileName)
    #return os.path.join(JESConfig.CONFIG_MEDIAPATH, fileName)

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
    f = open("JESConfig.py", "w+")
    contents = f.read()
    dict = ast.literal_eval(contents)
    dict["CONFIG_MEDIAPATH"] = directory
    # dict["CONFIG_MEDIAPATH"]="myPath"
    f.write(str(dict))
    f.close()
    JESConfig.CONFIG_MEDIAPATH = directory

def pickMediaPath():
    """Method to pick a media path using the file chooser and set it
    """
    JESConfig.CONFIG_MEDIAPATH = eg.diropenbox(title="Choose Media Path")
