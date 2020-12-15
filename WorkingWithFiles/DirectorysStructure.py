import os

def listDir(currentDir):
    os.chdir(currentDir)
    for dir in os.listdir(currentDir):
        if(os.path.isdir(os.path.realpath(dir))):
            listDir(os.path.realpath(dir))
        else:
            print(dir + "  -  " + os.path.realpath(currentDir))
    os.chdir(os.path.dirname(os.path.realpath(currentDir)))

path = ".."
print("Enter directory to start listing files")
path = input()
listDir(path)


