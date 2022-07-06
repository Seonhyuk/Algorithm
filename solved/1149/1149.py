import sys
sys.stdin = open("input.txt")

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
inf = int(1e09)
result = [[inf] * 3 for _ in range(n)]

for i in range(3):
    result[0][i] = matrix[0][i]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j != k:
                result[i][j] = min(result[i][j], result[i-1][k] + matrix[i][j])

print(min(result[-1]))