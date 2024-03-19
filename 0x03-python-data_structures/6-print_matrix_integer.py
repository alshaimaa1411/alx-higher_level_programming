#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for z in i:
            if z == [-1]:
                print("{:d}".format(z), end="")
            else:
                print("{:d}".format(z), end=" ")
        print()
