import sys, pprint
sys.stdin = open("input.txt")

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e09)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            matrix[i][j] = INF

size = 2**n - 1
dp = [[0] * size for _ in range(n)]

for i in range(1, n):
    dp[i][0] = matrix[i][0]

for a in range(1, size):
    if not a % 2:
        for k in range(n):
            if False if a & (1 << k) else True:
                min_value = INF
                for j in range(1, n):
                    if True if a & (1 << j) else False:
                        m = matrix[k][j] + dp[j][a & ~(1 << j)]
                        if min_value > m:
                            min_value = m

                dp[k][a] = min_value

print(dp[0][size-1])
