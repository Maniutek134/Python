import random

mxSize = 128
a = [[random.randint(0,9) for i in range(mxSize)] for j in range(mxSize)]
b = [[random.randint(0,9) for i in range(mxSize)] for j in range(mxSize)]

matrix3 = [[0 for i in range(mxSize)] for j in range(mxSize)]

def add(matrix1,matrix2):
    for i in range(mxSize):
        for j in range(mxSize):
            matrix3[i][j]= matrix1[i][j]+matrix2[i][j]

    return matrix3

print (add(a,b))