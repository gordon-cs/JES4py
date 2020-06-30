import json
import os
import ast

CONFIG_WRAPPIXELVALUES = 0
CONFIG_MEDIAPATH = ""
CONFIG_FILENAME = ".jesconf"

def readFromConfig():
    filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
    global CONFIG_MEDIAPATH
    if os.path.exists(filePath):
        f = open(filePath, "r")
        contents = f.read()
        dict = json.loads(contents)
        CONFIG_MEDIAPATH = dict["CONFIG_MEDIAPATH"]
        f.close()
    else:
        f = open(filePath, "w+")
        dict = {"CONFIG_WRAPPIXELVALUES": 0, "CONFIG_MEDIAPATH": ""}
        f.write(str(dict))
        f.close()


def writeToConfig(newPath):
    filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
    if os.path.exists(filePath):
        f = open(filePath, "r")
        contents = f.read()
        #dict = ast.literal_eval(contents)
        dict = json.loads(contents)
        dict["CONFIG_MEDIAPATH"]=newPath
        f.close()
        f = open(filePath, "w")
        f.write(json.dumps(dict))
        #f.write(str(dict))
        f.close()
    else:
        f = open(filePath, "w")
        dict = {"CONFIG_WRAPPIXELVALUES": 0, "CONFIG_MEDIAPATH": newPath}
        f.write(json.dumps(dict))
        f.close()