import sys
sys.stdin = open("input.txt")

n = int(input())
arr = [int(input()) for _ in range(n)]

dp1 = [0, arr[0]]
dp2 = [0, arr[0]]

while len(dp1) < n + 1:
    dp1.append(dp2[-1] + arr[len(dp1)-1])
    dp1[-1] = max(dp1)
    dp2.append(max(dp1[-3], dp2[-2]) + arr[len(dp2)-1])
    dp2[-1] = max(dp2)

print(max(max(dp1), max(dp2)))