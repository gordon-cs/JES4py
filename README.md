# JES4py - a JES emulator for Python 3

[**JES**](https://github.com/gatech-csl/jes), the Jython Environment for Students, is an educational IDE used in the Media Computation curriculum developed by Mark Guzdial and Barbara Ericson at Georgia Tech. More details on the curriculum are available at http://www.mediacomputation.org/.  

[**Jython**](https://www.jython.org/) is a Java implementation of Python 2.x and was designed to allow rapid application development and scripting access to Java functionality.

The **JES4py** implements a subset of JES features that can be used in Python 3.x scripts.  The goal is to provide the pedogocial assets of JES without requiring Jython or needing to use JES's IDE.

## Prerequisites
1. An IDE (Integrated Development Environment) of your choice.  [**Visual Studio Code**](https://code.visualstudio.com/) is recommended if you have no preference.
2. [**Python**](https://www.python.org/downloads/) 3.x Installed
3. **A Supported OS**:  Windows, Linux, macOS

## Installing JES4py

JES4py needs Python 3.  Before proceeding, find out how to run Python 3 from the command line on your computer.  Usually this is done by typing `python` or `python3` at the command line prompt.  You can check your version with `python --version` or `python3 --version`.

Ideally you will be able to install JES4py using a single command (use either `python` or `python3` as appropriate):
```
python -m pip -U jes4py
```
If this fails, it is probably due to some missing prequistes on your system.  Study the error message for clues as to what is needed.  Rerun the above command once you've installed the missing software.

## Using JES4py

Users should include the following line at a Python 3.x command prompt
or in a Python 3.x script to make use of JES functions"
```
from jes4py import *
```
