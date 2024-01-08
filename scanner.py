import os
import win32api
import r2pipe

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
def scanFile(filePath):
    points = 0

    #Size Check
    if os.path.getsize(filePath) > 1048576:
        points+=1
    
    #System Modification Check
    with open(filePath, "rb") as f:
        data = f.read()
        if b"system(" in data or b"system (" in data:
            points+=1
    
    #Network Connection Check
    # Look for network-related functions
    network_functions = [b"connect", b"send", b"recv"]
    with open(filePath, "rb") as f:
        data = f.read()
        for function in network_functions:
            if function in data:
                points+=1


    if points >= 2:
        return True
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

    susFiles = []
    for subDir in files:
        subdirName = subDir[0]
        for f in subDir[1]:
            fi = subdirName  + "\\\\" + f
            if scanFile(fi):
                susFiles.append(fi)

    
    return susFiles

scanDirectory("C:\\Users\\aravj\\Downloads")