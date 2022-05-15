import sys
sys.stdin = open("input.txt")

from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))
d = []


for i in range(n):
    if not d or lst[i] > d[-1]:
        d.append(lst[i])
    else:
        a = bisect_left(d, lst[i])
        d[a] = min(d[a], lst[i])

print(len(d))