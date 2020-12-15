import json

def newRecord(record):
    for x in record:
        print("Input " + x +":")
        record[x] = str(input())
    return record

file = open("json.json", 'r+')
record = {"firstName": "", "lastName": "", "age": "", "address": "" }

try:
    data = json.load(file)
except:
    data = [newRecord(record)]

while True:
    print(data)
    print("a - add record, d - delete record, q - quit")
    choice = str(input())
    if choice == "a":
        data.append(newRecord(record))
    elif choice == "d":
        print("Input the firstName od the record to delete it")
        value = input()
        for i in range(len(data)):
            if data[i]["firstName"] == value:
                data.pop(i)
                break
    elif choice == "q":
        break

file.truncate(0)
file.seek(0)
json.dump(data, file)
file.close()









