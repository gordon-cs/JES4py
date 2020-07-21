import json
import os

CONFIG_DICT = {
    "CONFIG_WRAPPIXELVALUES" : False,
    "CONFIG_MEDIA_PATH" : "",
    "CONFIG_SESSION_PATH" : "",
    "CONFIG_JES4PY_PATH" : ""
    }
CONFIG_FILENAME = ".jes4pyconf"

def getConfigVal(key):
    return CONFIG_DICT[key]

def setConfigVal(key, val):
    CONFIG_DICT[key] = val
    writeDict(CONFIG_DICT)

def initPath():
    import jes4py
    CONFIG_DICT["CONFIG_JES4PY_PATH"] = os.path.dirname(jes4py.__file__)

def initDict():
    filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
    if os.path.exists(filePath):
        curDict = readDict(filePath)
        global CONFIG_DICT
        pathDict = readDict(filePath)
        CONFIG_DICT["CONFIG_SESSION_PATH"]=pathDict["CONFIG_MEDIA_PATH"]
        CONFIG_DICT["CONFIG_MEDIA_PATH"]=pathDict["CONFIG_MEDIA_PATH"]

def writeDict(dict):
    filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
    f = open(filePath, "w")
    f.write(json.dumps(dict))
    f.close()

def readDict(filePath):
    f = open(filePath, "r")
    contents = f.read()
    dict = json.loads(contents)
    f.close()
    return dict
