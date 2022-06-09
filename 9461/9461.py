import sys
sys.stdin = open("input.txt")

dp = [1, 1, 1]

T = int(input())
for tc in range(T):
    n = int(input())

    while len(dp) < n:
        dp.append(dp[-2] + dp[-3])

    print(dp[n-1])