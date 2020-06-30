import json
import os
import ast

# CONFIG_WRAPPIXELVALUES = 0
# CONFIG_MEDIAPATH = ""
CONFIG_DICT = {
    "CONFIG_WRAPPIXELVALUES": False,
    "CONFIG_MEDIAPATH": ""
    }
CONFIG_FILENAME = ".jesconf"


# def updateConfigFile(key, val):
#     filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
#     if os.path.exists(filePath):
#         dict = readDict(filePath)
#         dict[key]=val
#         f = open(filePath, "w")
#         f.write(json.dumps(dict))
#         #f.write(str(dict))
#         f.close()
#     else:
#         dict = CONFIG_DICT
#         dict[key]=val
#         writeDict(dict)

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

# def readOrGenerateConfig():
#     filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
#     global CONFIG_MEDIAPATH
#     if os.path.exists(filePath):
#         dict = readDict(filePath)
#         CONFIG_MEDIAPATH = dict["CONFIG_MEDIAPATH"]
#         CONFIG_WRAPPIXELVALUES = dict["CONFIG_WRAPPIXELVALUES"]
#     else:
#         f = open(filePath, "w+")
#         dict = generateDict()
#         f.write(json.dumps(dict))
#         f.close()


# def updateOrGenerateConfig(newPath):
#     filePath = os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)
#     if os.path.exists(filePath):
#         f = open(filePath, "r")
#         contents = f.read()
#         #dict = ast.literal_eval(contents)
#         dict = json.loads(contents)
#         dict["CONFIG_MEDIAPATH"]=newPath
#         f.close()
#         f = open(filePath, "w")
#         f.write(json.dumps(dict))
#         #f.write(str(dict))
#         f.close()
#     else:
#         f = open(filePath, "w")
#         dict = {"CONFIG_WRAPPIXELVALUES": 0, "CONFIG_MEDIAPATH": newPath}
#         f.write(json.dumps(dict))
#         f.close()