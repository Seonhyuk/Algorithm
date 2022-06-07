import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
dp = []

for num in arr:
    if not dp:
        dp.append(num)
    else:
        if dp[-1] < 0:
            dp.append(num)
        else:
            dp.append(dp[-1]+num)

print(max(dp))