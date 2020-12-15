import numpy as np

a = np.random.rand(128,128)
b = np.random.rand(128,128)


def matSum(a, b):
    c = []
    for i in range(0, len(a)):
        row = []
        for j in range(0, len(a[i])):
            row.append(a[i][j]+b[i][j])
        c.append(row)
    return c

print("Suma macierzy wynosi: " + str(matSum(a,b)))