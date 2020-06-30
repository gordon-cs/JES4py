import os
import JESConfig
import json
from media import *
    
filePath = os.path.join(os.path.expanduser("~"), JESConfig.CONFIG_FILENAME)
f = open(filePath, "r")
contents = f.read()
dict = json.loads(contents)
JESConfig.CONFIG_MEDIAPATH = dict["CONFIG_MEDIAPATH"]
f.close()