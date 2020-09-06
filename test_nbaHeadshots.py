import headshots
import os, shutil

def testSingleID():
    
    headshots.getHeadshotById(2544, folder="testFolder/", fileName="lebron.png")
    assert(os.path.exists("testFolder/lebron.png"))
    os.remove("testFolder/lebron.png")

    headshots.getHeadshotById(2544, folder="testFolder/testFolder/")
    assert(os.path.exists("testFolder/testFolder/2544.png"))
    os.remove("testFolder/testFolder/2544.png")

    headshots.getHeadshotById(1, folder="testFolder/testFolder/", fileName="NonValidPlayer.png")
    assert(os.path.exists("testFolder/testFolder/NonValidPlayer.png") == False)

    headshots.getHeadshotById("hi", folder="testFolder/testFolder/")
    assert(os.path.exists("testFolder/testFolder/hi.png") == False)

    os.rmdir("testFolder/testFolder")
    os.rmdir("testFolder")


def testMultipleID():

    headshots.getAllHeadshots("testFolder/")
    assert(os.path.exists("testFolder/"))
    shutil.rmtree("testFolder/")



