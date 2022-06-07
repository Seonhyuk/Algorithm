import sys
sys.stdin = open("input.txt")

T = int(input())
lst = [int(input()) for _ in range(T)]

a = max(lst)

dp = [1, 1, 2, 4]

while len(dp) < a + 1:
    dp.append(dp[-1] + dp[-2] + dp[-3])

for num in lst:
    print(dp[num])