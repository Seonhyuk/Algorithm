import sys
import heapq
sys.stdin = open("input.txt")

n, l = map(int, input().split())

nums = list(map(int, input().split()))
hq = []
result = []

for i in range(n):
    heapq.heappush(hq, (nums[i], i))

    while hq[0][1] <= i - l:
        heapq.heappop(hq)

    result.append(hq[0][0])

print(*result)