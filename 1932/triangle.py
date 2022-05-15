import sys

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * i for i in range(1, n+1)]
result[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            result[i][j] = result[i-1][j] + triangle[i][j]
        elif j == i:
            result[i][j] = result[i-1][j-1] + triangle[i][j]
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-1]) + triangle[i][j]

print(max(result[-1]))