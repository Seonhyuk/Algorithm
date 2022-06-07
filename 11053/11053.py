import sys
sys.stdin = open("input.txt")

from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = [0]

for i in arr:
    a = bisect_left(dp, i)
    if a >= len(dp):
        dp.append(i)
    else:
        dp[a] = i

print(len(dp)-1)