import numpy as np
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def sum_matrix(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum



#we used numpy library that has the matrix multplication inside it.
#what it does is calculating the dot product between two matrices
#by multiplying row by column of each matrix
def mult_matrix(matrixA , matrixB):
   return np.dot(matrixA,matrixB)




def main():

    sizeMatrix = int(input("Enter matrixes size: "))
    matrixA = []
    matrixB = []
    for i in range(sizeMatrix):
        temp = [0]*sizeMatrix
        matrixA.append(temp)

    for i in range(sizeMatrix):
        temp = [0] * sizeMatrix
        matrixB.append(temp)


    print("Enter values for matrix A: ")
    for i in range(sizeMatrix):
        for j in range(sizeMatrix):
            matrixA[i][j] = int(input())

    print("Enter values for matrix B: ")
    for i in range(sizeMatrix):
        for j in range(sizeMatrix):
            matrixB[i][j] = int(input())

    print("Matrix A:")
    print_matrix(matrixA)

    print("Matrix B:")
    print_matrix(matrixB)

    print("The of both matrix is: ",sum_matrix(matrixA)+sum_matrix(matrixB) )

    print("The mult of both matrix is: ")
    print_matrix(mult_matrix(matrixA, matrixB))


main()

