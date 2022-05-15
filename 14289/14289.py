import sys
sys.stdin = open("input.txt")


def product(matrix1, matrix2):
    global n
    result = []
    for i in range(n):
        sub = []
        for j in range(n):
            cnt = 0
            for k in range(n):
                cnt += matrix1[i][k] * matrix2[k][j]
            sub.append(cnt % 1000000007)
        result.append(sub)
    return result


def power(m, N):
    if N == 1:
        return m
    else:
        new_m = power(m, N//2)
        if N % 2:
            return product(product(new_m, new_m), m)
        else:
            return product(new_m, new_m)


n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

d = int(input())

result = power(matrix, d)

print(result[0][0])