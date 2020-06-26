# Module file for the JES Emulator.
#
# JES (Jython Environment for Students) provides a GUI IDE for students work
# with media files.  It uses Python 2.x syntax and the GUI IDE itself has
# some quirks that make it difficult to work with.
#
# The JES Emulator uses the native Python 3.x implementation, along with
# a few standard additional modules (e.g. PIL image library, wxPython).
#
# To use the JES Emulator:
#   1. Make sure that this file and all supporting JES files are stored in
#      a directory (folder) that is in your Python path.  Instructions for
#      doing this are platform dependent but are easily available on the web.
#   2. When you start Python, or at the top of your Python script, include
#      the line:
#         from JESemu import *
#

# Individual JES modules are imported here
from media import *
