import sys
sys.stdin = open("input.txt")

T = int(input())
dp = [1, 1]

for _ in range(T):
    n = int(input())

    while dp[-1] < n:
        dp.append(dp[-1] + dp[-2])

    result = []
    idx = len(dp) - 1

    while n > 0:
        if dp[idx] <= n:
            n -= dp[idx]
            result.append(dp[idx])

        idx -= 1

    result.sort()
    print(*result)