#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        x = len(matrix)
        for i in range (0, x):
            y = len(matrix[i])
            for z in range(0, y):
                if z == y:
                    print("{:d}".format(matrix[i][z]))
                else:
                    print("{:d}".format(matrix[i][z]), end=" ")
            print()
    else:
        print(end="")
