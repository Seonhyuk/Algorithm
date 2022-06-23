import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

inf = 2 ** 31

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        if i == 1:
            dp[j][j+1] = matrix[j][0] * matrix[j][1] * matrix[j+1][1]

        else:
            state = inf
            for k in range(j, j+i):
                state = min(state, dp[j][k] + dp[k+1][i+j] + matrix[j][0] * matrix[k][1] * matrix[i+j][1])

            dp[j][j+i] = state

print(dp[0][n-1])