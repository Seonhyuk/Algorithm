import sys
sys.stdin = open("input.txt")

n = int(input())
a = [2]
dp = [3]

while n > len(dp):
    next = (a[-1] * 4 + 3) % 1000000007
    a.append((a[-1] * 2 + 2) % 1000000007)
    dp.append(next)

print(dp[n-1])