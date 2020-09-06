import requests, os

def allIds():
    
    ids = []
    with open("playerIds.txt") as f:    
        for line in f.readlines() :
            ids.append(line.rstrip("\n"))
    return ids

def getHeadshotById(id, folder=None, fileName=None):
    
    if not fileName:
        fileName = str(id) + ".png"

    if not folder:
        folder = ""
    
    url = "https://datadunkstorage.blob.core.windows.net/headshots/" + str(id) +".png"
    
    if not os.path.isdir(folder) and folder is not "":
        os.mkdir(folder)
        
    r = requests.get(url, allow_redirects=True)
    if r.ok:
        open(folder + fileName, 'wb').write(r.content)
    else:
        print("Error: Not a valid id. Please specify a valid id.")

def getAllHeadshots(folder):
    
    for id in allIds():
        getHeadshotById(id, folder)


#getHeadshotById(-1, folder="testFolder/", fileName="NonValidPlayer.png")