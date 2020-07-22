"""
Student: Asaf Yosef Ben Shabat
ID: 312391774
Assignment no. 3
Program: matrix.py
"""


def transposed_matrix(A):  # transposing a matrix with loops
    result = [[0 for i in range(len(A))] for j in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            result[i][j] = A[j][i]
    return result


def transposed_by_comprehension(A):  # list comprehension solution for transposing a matrix
    MT = [[row[i] for row in A] for i in range(len(A[0]))]
    return MT


def matrix_mult(A, B):  # multiplying 2 matrices
    A = transposed_matrix(A)  # transposing the matrix "A"
    mat_multiplied = [[0 for i in range(len(A))] for j in range(len(B[0]))]
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(len(B)):
                mat_multiplied[i][j] += float(A[i][k] * B[k][j])  # float for the requested output
    return mat_multiplied


def print_matrix(MatrixT):  # prints a matrix
    for i in MatrixT:
        MAT = str(i)[1:-1]
        print(MAT)
    return 0


# main program
f = open("matrices.txt", "r")
ReadFile = f.read()[2:].split("B=")
ReadFile = [i.split("\n") for i in ReadFile]
A = [line.split() for line in ReadFile[0] if line]
B = [line.split() for line in ReadFile[1] if line]
A = [[int(A[i][j]) for j in range(0, len(A[0]))] for i in range(0, len(A))]
B = [[int(B[i][j]) for j in range(len(B[0]))] for i in range(len(B))]
MatrixT = matrix_mult(A, B)
print_matrix(MatrixT)
