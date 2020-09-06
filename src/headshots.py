import urllib.request
import os.path

def allIds():
    
    ids = []
    with open("playerIds.txt") as f:    
        for line in f.readlines() :
            ids.append(line.rstrip("\n"))
    return ids

def getHeadshotById(id, location, fileName=None):
    
    if not fileName:
        fileName = str(id) + ".png"
    url = "https://datadunkstorage.blob.core.windows.net/headshots/" + str(id) +".png"
    
    if not os.path.isdir(location):
        os.mkdir(location)

    try:
        urllib.request.urlretrieve(url, location + fileName)
    except:
        print("Error: Not a valid id. Please specify a valid id.")

def getAllHeadshots(location):
    
    for id in allIds():
        getHeadshotById(id, location)