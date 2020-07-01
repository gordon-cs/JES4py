import json
import os

# CONFIG_WRAPPIXELVALUES = 0
# CONFIG_MEDIAPATH = ""
CONFIG_DICT = {
    "CONFIG_WRAPPIXELVALUES": False,
    "CONFIG_MEDIAPATH": ""
    }
CONFIG_FILENAME = ".jesconf"

def writeDict(dict):
    filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
    f = open(filePath, "w")
    f.write(json.dumps(dict))
    f.close()

def getConfigVal(key):
    return CONFIG_DICT[key]

def setConfigVal(key, val):
    CONFIG_DICT[key] = val
    writeDict(CONFIG_DICT)

def initDict():
    filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
    if os.path.exists(filePath):
        curDict = readDict(filePath)
        global CONFIG_DICT
        CONFIG_DICT = curDict.copy()

def readDict(filePath):
    f = open(filePath, "r")
    contents = f.read()
    dict = json.loads(contents)
    f.close()
    return dict
