import numpy as np
import random
import math

def matDet(data, tot=0):
    indexList = list(range(len(data)))

    if len(data) == 2 and len(data[0]) == 2:
        val = data[0][0]*data[1][1]-data[1][0]*data[0][1]
        return val

    for fc in indexList:
        mat = data[1:]
        height = len(mat)
        for i in range(height):
            mat[i] = mat[i][0:fc]+mat[i][fc+1:]

        sign = (-1)**(fc % 2)
        sub_det = matDet(mat)
        tot+=sign*data[0][fc]*sub_det

    return tot


rand = random.randint(1, 3)
a = np.random.rand(rand, rand)

print("Matrix: " + str(a))
print("Determinant: " + str(matDet(a)))

