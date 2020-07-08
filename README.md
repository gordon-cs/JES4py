# JES-emulator

[**JES**](https://github.com/gatech-csl/jes), the Jython Environment for Students, is an educational IDE used in the Media Computation curriculum developed by Mark Guzdial and Barbara Ericson at Georgia Tech. More details on the curriculum are available at http://www.mediacomputation.org/.  

[**Jython**](https://www.jython.org/) is a Java implementation of Python 2.x and was designed to allow rapid application development and scripting access to Java functionality.

The **JES-Emulator** implements a subset of JES features that can be used in Python 2.x and Python 3.x scripts.  The goal is to provide the pedogocial assets of JES without requiring Jython or needing to use JES's IDE.

## Installation of Dependencies

Several dependencies need to be installed before you can use the JES-emulator.  Currently these include PIL (the Python Image Library) or Pillow (an updated fork of PIL).  Instructions to do this are OS-dependent:

### Windows

TBD

### Mac OS-X

TBD

### Linux
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

## Using the JES-emulator

Users should include the following line at a Python 3.x command prompt
or in a Python 3.x script to make use of JES functions
```
from JESemu import *
```
(NOTE: we need to decide on the name of this function - I suggest `JESmedia.py`.  We can then similarly name any other updated versions of the JES Python files that we decide to include.)