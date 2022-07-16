import sys
from math import gcd

sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]
k = int(input())

r = [[(j*10**len(str(nums[i])) + nums[i]) % k for j in range(k)] for i in range(n)]

size = 2 ** n

dp = [[0] * size for _ in range(k)]
dp[0][0] = 1

for i in range(1, 1 << n):
    for j in range(n):
        if i & (1 << j):
            t = i & ~(1 << j)
            for l in range(k):
                dp[r[j][l]][i] += dp[l][t]

s = dp[0][-1]
m = 0
for i in range(k):
    m += dp[i][-1]

if s == m:
    print("1/1")
elif s == 0:
    print("0/1")
else:
    z = gcd(s, m)
    s //= z
    m //= z

    print(f"{s}/{m}")
