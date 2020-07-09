import json
import os

CONFIG_DICT = {
    "CONFIG_WRAPPIXELVALUES" : False,
    "CONFIG_MEDIAPATH" : "",
    "CONFIG_SESSIONPATH" : "",
    "CONFIG_JESPATH" : ""
    }
CONFIG_FILENAME = ".jesconf"

def getConfigVal(key):
    return CONFIG_DICT[key]

def setConfigVal(key, val):
    CONFIG_DICT[key] = val
    writeDict(CONFIG_DICT)

def initJESPath():
    import JESemu
    CONFIG_DICT["CONFIG_JESPATH"] = os.path.dirname(JESemu.__file__)

def initDict():
    filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
    if os.path.exists(filePath):
        curDict = readDict(filePath)
        global CONFIG_DICT
        pathDict = readDict(filePath)
        CONFIG_DICT["CONFIG_SESSIONPATH"]=pathDict["CONFIG_MEDIAPATH"]
        CONFIG_DICT["CONFIG_MEDIAPATH"]=pathDict["CONFIG_MEDIAPATH"]

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
