import re

inFile = open('text.txt', 'r')
outFile = open('textF.txt', 'w')

specificWords = ['sie', 'i', 'oraz', 'nigdy', 'dlaczego']

for data in inFile:
    wordList = re.findall(r"[\w']+", data)
    line = ""
    found = False
    for word in wordList:
        for oneWord in specificWords:
            if word == oneWord:
                found = True
        if not found:
            line = line + word + ", "
            found = False
        found = False
    outFile.write(line + '\n')

inFile.close()
outFile.close()