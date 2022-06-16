import sys
sys.stdin = open("input.txt")

n = int(input())
dp = [1, 0, 3]

while len(dp) < n + 1:
    if len(dp) % 2:
        dp.append(0)
    else:
        num = 0
        k = 0
        k += dp[-2] * 3
        while num < len(dp) - 3:
            k += dp[num] * 2
            num += 2
        dp.append(k)

print(dp)