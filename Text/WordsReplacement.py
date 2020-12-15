import re

inFile = open('text.txt', 'r')
outFile = open('textF.txt', 'w')

specificWords = {'i':'oraz', 'oraz':'i', 'nigdy':'prawie nigdy', 'dlaczego':'czemu'}

for data in inFile:
    wordList = re.findall(r"[\w']+", data)
    line = ""
    found = False
    for word in wordList:
        for oneWord in specificWords:
            if word == oneWord:
                line = line + specificWords[word] + ", "
                found = True
        if not found:
            line = line + word + ", "
            found = False
        found = False
    outFile.write(line + '\n')

inFile.close()
outFile.close()