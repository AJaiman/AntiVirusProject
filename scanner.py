import os

#os.chdir(path) sets working directory
#os.stat(path) gets file stats
#os.walk() will give you the root, dirs, and files in a direcotry (including in all the subdirs)
susTypes = ["exe", "dll", "bat", "ps1"]

def isSus(filePath):
    return False

def scanDirectory(path):
    files = []
    for root, dirs, fs in os.walk(path):
        files.append([root, fs])
    print(files, "\n")
    for pair in files:
        fileList = pair[1]
        newFileList = []
        for file in fileList:
            n = file.split(".")
            if n[-1] in susTypes:
                newFileList.append(file)
        pair[1] = newFileList
    print(files)
    #susFiles = []
    #return susFiles

scanDirectory("C:\\Users\\aravj\\Downloads")