import sys
import heapq

n = int(input())
q = []

for _ in range(n):
    k = int(sys.stdin.readline())

    if k:
        heapq.heappush(q, k)
    else:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)