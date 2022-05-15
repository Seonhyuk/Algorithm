import sys
import heapq
from collections import defaultdict

sys.stdin = open("input.txt")

n, m, x = map(int, input().split())
graph = defaultdict(list)
inf = int(1e08)
distance = [inf] * (n+1)

for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    graph[s].append((t, e))

heap = []
heapq.heappush(heap, (0, x))
distance[x] = 0

while heap:
    dist, end = heapq.heappop(heap)

    if dist <= distance[end]:
        for d in graph[end]:
            if dist + d[0] < distance[d[1]]:
                distance[d[1]] = dist + d[0]
                heapq.heappush(heap, (dist+d[0], d[1]))

result = 0

for i in range(1, n+1):
    space = [inf] * (n+1)
    space[i] = 0
    heap = []
    heapq.heappush(heap, (0, i))

    while heap:
        dist, end = heapq.heappop(heap)
        if dist <= space[end]:
            for d in graph[end]:
                if dist + d[0] < space[d[1]]:
                    space[d[1]] = dist + d[0]
                    heapq.heappush(heap, (dist + d[0], d[1]))

    result = max(result, space[x]+distance[i])

print(result)