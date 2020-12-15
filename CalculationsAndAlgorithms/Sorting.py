import random
import sys

data = []

for i in range(0, 50):
    data.append(random.randint(0, sys.maxsize))

check = data

for i in range(0, len(data)-1):
    for j in range(0, len(data)-1-i):
        if (data[j] > data[j+1]):
            data[j], data[j+1] = data[j+1], data[j]

check.sort()

print("Czy custom sort jest poprawny: " + str(check == data))
