import sys
import pprint
sys.stdin = open("input.txt")

n, m = input(), input()
if len(n) < len(m):
    n, m = m, n

a, b = len(n), len(m)

dp = [[''] * (b+1) for _ in range(a+1)]

for i in range(a):
    for j in range(b):
        if n[i] == m[j]:
            dp[i+1][j+1] = dp[i][j] + m[j]
        else:
            if len(dp[i][j+1]) >= len(dp[i+1][j]):
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = dp[i+1][j]

print(len(dp[-1][-1]))
if len(dp[-1][-1]):
    print(dp[-1][-1])