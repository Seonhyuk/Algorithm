import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline


def dfs(x, v):
    if v == size - 1:
        return 0

    if dp[x][v] != -1:
        return dp[x][v]

    dp[x][v] = 300000
    for i in range(n):
        if v & (1 << i):
            continue
        dp[x][v] = min(dp[x][v], dfs(x + 1, v | (1 << i)) + matrix[x][i])

    return dp[x][v]


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

size = 2 ** n
dp = [[-1] * size for _ in range(n)]

print(dfs(0, 0))
