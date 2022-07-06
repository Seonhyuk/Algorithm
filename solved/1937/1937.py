import sys
sys.setrecursionlimit(300*300)

input = sys.stdin.readline


def dfs(i, j):
    if not dp[i][j]:
        dp[i][j] = 1
        for a, b, in d:
            di = i + a
            dj = j + b

            if 0 <= di < n and 0 <= dj < n and matrix[di][dj] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(di, dj) + 1)

    return dp[i][j]


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for i in range(n):
    for j in range(n):
        dfs(i, j)

print(max(sum(dp, [])))
