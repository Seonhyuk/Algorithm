import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())

    matrix = [[0 for i in range(n)] for i in range(k+1)]
    matrix[0] = [i for i in range(1, n+1)]

    for i in range(1, k+1):
        for j in range(n):
            matrix[i][j] = sum(matrix[i-1][:j+1])

    print(matrix[k][n-1])