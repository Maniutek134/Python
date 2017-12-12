
matrix_size=8
matrix = [[j for i in range(matrix_size)] for j in range(matrix_size)]


def mxMultiply(matrix1,matrix2):
    matrix3 = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                matrix3[i][j]=matrix3[i][j]+(matrix1[j][k])*(matrix2[k][j])

    return matrix3

print(mxMultiply(matrix,matrix))

