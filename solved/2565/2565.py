import sys
from bisect import bisect_left

n = int(input())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lines.sort(key=lambda x: x[0])

dp = []

for i in range(n):
    a = bisect_left(dp, lines[i][1])

    if a >= len(dp):
        dp.append(lines[i][1])
    else:
        dp[a] = lines[i][1]

print(n - len(dp))
