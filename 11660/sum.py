import sys

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        result[i][j] += matrix[i][j]
        if j >= 1:
            result[i][j] += result[i][j-1]

for i in range(1, n):
    for j in range(n):
        result[i][j] += result[i-1][j]


for _ in range(m):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())

    if x1 == 1 and y1 == 1:
        print(result[y2-1][x2-1])
    elif x1 == 1:
        print(result[y2-1][x2-1] - result[y1-2][x2-1])
    elif y1 == 1:
        print(result[y2-1][x2-1] - result[y2-1][x1-2])
    else:
        print(result[y2-1][x2-1] - result[y1-2][x2-1] - result[y2-1][x1-2] + result[y1-2][x1-2])