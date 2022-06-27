import sys
sys.stdin = open("input.txt")

n = int(input())
cost = [list(map(int, input())) for _ in range(n)]

dp = [[-1] * (1 << n) for _ in range(n)]
dp[0][1] = 0

result = 0
for i in range(3, 1 << n):
    if i % 2:
        for j in range(1, n):
            if i & (1 << j):
                for k in range(n):
                    if k != j and cost[k][j] >= dp[k][i & ~(1 << j)] >= 0:
                        if dp[j][i] == -1:
                            dp[j][i] = cost[k][j]
                        else:
                            dp[j][i] = min(dp[j][i], cost[k][j])

                        cnt = bin(i)[2:].count('1')
                        result = max(result, cnt)

print(result)
