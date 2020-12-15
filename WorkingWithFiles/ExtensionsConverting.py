import os


def changeExt(inData):
    name, ext = os.path.splitext(inData)
    if (ext == '.jpg'):
        print(inData, name)
        os.rename(inData, name + '.png')
        return 2
    return 1


for i in range(3):
    file = open("file" + str(i) +".jpg", "w+")

print("Enter file path to convert one file or directory path to convert all files int the directory")
inData = input()

if (os.path.isfile(os.path.realpath(inData))):
    changeExt(os.path.realpath(inData))

elif (os.path.isdir(os.path.realpath(inData))):
    i = 0;
    print(i)
    os.chdir(os.path.realpath(inData))
    for file in os.listdir('..'):
        i += changeExt(os.path.realpath(file)) - 1;
    print("Changes extensions for " + str(i) + " files.")