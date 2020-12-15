a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
prod = 0

for i in range(0, len(a)):
    prod += a[i]*b[i]

print("Iloczyn skalarny wynosi: " + str(prod))