import sys, pprint
sys.stdin = open("input.txt")


def matrix_multiply(matrix1, matrix2):
    matrix1_matrix2 = [
        [matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0],
         matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]],
        [matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0],
         matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]]
    ]
    return matrix1_matrix2


def fib(exponent):
    if exponent <= 1:
        return [[1, 1], [1, 0]]

    if exponent % 2 == 0:
        new_base = fib(exponent / 2)
        return matrix_multiply(new_base, new_base)
    else:
        new_base = fib((exponent - 1) / 2)
        return matrix_multiply(matrix_multiply(new_base, new_base), [[1, 1], [1, 0]])


n = int(input())
if n <= 2:
    result = 1
else:
    a = fib(n-2)
    result = a[0][0] + a[0][1]
