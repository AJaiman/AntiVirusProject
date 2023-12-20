import os
import win32api

#os.chdir(path) sets working directory
#os.stat(path) gets file stats
#os.walk() will give you the root, dirs, and files in a direcotry (including in all the subdirs)
susTypes = ["exe", "dll", "bat", "ps1"]

#Checks to see if a file has a digital signiture
def digitalSignatureCheck(filePath):
    try:
        d = win32api.GetFileVersionInfo(filePath, "\\")
        d['Signature']
        return True
    except Exception:
        return False


#Checks to see if a file fits the requirements to be suspected
def isSus(filePath):
    return False

#Scans a directory and adds any sus files to the main sus files list
def scanDirectory(path):
    files = []

    for root, dirs, fs in os.walk(path):
        files.append([root, fs])

    for pair in files:
        fileList = pair[1]
        newFileList = []

        for file in fileList:
            n = file.split(".")

            if n[-1] in susTypes:
                newFileList.append(file)

        pair[1] = newFileList


    #susFiles = []
    #return susFiles

scanDirectory("C:\\Users\\aravj\\Downloads")