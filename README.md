# JES4py - a JES emulator for Python 3

[**JES**](https://github.com/gatech-csl/jes), the Jython Environment for
Students, is an educational IDE used in the Media Computation curriculum
developed by Mark Guzdial and Barbara Ericson at Georgia Tech. More details
on the curriculum are available at http://www.mediacomputation.org/.  

[**Jython**](https://www.jython.org/) is a Java implementation of Python 2.x
and was designed to allow rapid application development and scripting access
to Java functionality.

[**JES4py**](https://github.com/gordon-cs/JES4py) implements a subset of JES
features that can be used in Python 3.x scripts.  The goal is to provide the
pedagogical assets of JES without requiring Jython or needing to use JES's IDE.

## Prerequisites
1. An IDE (Integrated Development Environment) of your choice.
[**Visual Studio Code**](https://code.visualstudio.com/) is recommended if you
have no preference.
2. [**Python**](https://www.python.org/downloads/) 3.6 or higher
3. **A Supported OS**: Windows, MacOS, Linux

## Installing JES4py

JES4py needs Python 3.6 or higher.  Before proceeding, find out how to run
Python 3 from the command line on your computer.  Usually this is done by
typing `python` or `python3` at the command prompt.  You can check your
version with `python --version` or `python3 --version`.

Ideally you will be able to install JES4py using a single command: use either
```
python -m pip install -U jes4py
```
or
```
python3 -m pip install -U jes4py
```
If this fails, it is probably due to some missing prerequisites on your system.
Study the error message for clues as to what is needed.  Trying to install the
prerequisite one-by-one may be helpful (using `python` or `python3` as
appropriate):
```
python3 -m pip install -U wxPython
python3 -m pip install -U wave
python3 -m pip install -u simpleaudio
```
Once these are installed, rerun the command
```
python3 -m pip install -U jes4py
```
to install the JES4py package.

## Using JES4py

To use JES4py functions in a Python interactive session you should type the
following command at the Python prompt.
```
from jes4py import *
```

To access JES4py functions in from a Python program, you should include the
same line at the top of any file containing a Python program that uses JES4py
functions.  For example:
```
from jes4py import *

filename = pickAFile()
print('Hello! You picked the file', filename)

```
