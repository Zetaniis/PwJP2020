import numpy as np

a = np.random.rand(8,8)
b = np.random.rand(8,8)

def matMul(a, b):
    c = []
    for i in range(0, len(a)):
        row = []
        for j in range(0, len(b[i])):
            val = 0
            for l in range(0, len(a[i])):
                val += a[i][l]*b[l][j]
            row.append(val)
        c.append(row)
    return c

print("Wartosc mnozenia wynosi: " + str(matMul(a, b)))
