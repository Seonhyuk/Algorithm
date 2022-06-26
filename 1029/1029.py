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
                    if k != j and dp[k][i & ~(1 << j)] >= 0:
                        if dp[k][i & ~(1 << j)] <= cost[k][j]:
                            if dp[j][i] == -1:
                                dp[j][i] = cost[k][j]
                            else:
                                dp[j][i] = min(dp[j][i], cost[k][j])

                            cnt = 0
                            for t in range(n):
                                if i & (1 << t):
                                    cnt += 1
                            if cnt > result:
                                result = cnt

print(result)
