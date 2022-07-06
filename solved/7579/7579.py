import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0] * 10001 for _ in range(n+1)]

result = 100000000

for i in range(1, n+1):
    for j in range(10001):
        if j - cost[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= m and j < result:
            result = j

print(result)
