import sys
import heapq
from collections import defaultdict

# sys.stdin = open("test.txt")

n, e = map(int, input().split())

graph = defaultdict(list)

for _ in range(e):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))

inf = 1e11
m = list(map(int, input().split()))
mid = [1] + m + [n]
mid2 = [1] + [m[1]] + [m[0]] + [n]

result = 0

for i in range(3):
    distance = [inf] * (n + 1)
    dijk = []
    heapq.heappush(dijk, (0, mid[i]))
    distance[mid[i]] = 0

    while dijk:
        dist, node = heapq.heappop(dijk)
        if distance[node] >= dist:
            for next in graph[node]:
                cost = dist + next[0]
                if cost < distance[next[1]]:
                    distance[next[1]] = cost
                    heapq.heappush(dijk, (cost, next[1]))

    if distance[mid[i+1]] == inf:
        result = -1
        break

    result += distance[mid[i+1]]

result2 = 0

for i in range(3):
    distance = [inf] * (n + 1)
    dijk = []
    heapq.heappush(dijk, (0, mid2[i]))
    distance[mid2[i]] = 0

    while dijk:
        dist, node = heapq.heappop(dijk)
        if distance[node] >= dist:
            for next in graph[node]:
                cost = dist + next[0]
                if cost < distance[next[1]]:
                    distance[next[1]] = cost
                    heapq.heappush(dijk, (cost, next[1]))

    if distance[mid2[i+1]] == inf:
        result2 = -1
        break

    result2 += distance[mid2[i+1]]

print(result if result < result2 else result2)