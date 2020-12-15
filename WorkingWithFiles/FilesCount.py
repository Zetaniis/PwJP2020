import os
list=[]
for name in os.listdir("/dev"):
    list.append(name)
print(len(list))