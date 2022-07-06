import heapq
import sys
from collections import defaultdict

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    start, end, price = map(int, sys.stdin.readline().split())
    graph[start].append((price, end))

start, end = map(int, input().split())

inf = 1e09

distance = [inf] * (n+1)
distance[start] = 0

s = []
heapq.heappush(s, (0, start))

while s:
    price, start = heapq.heappop(s)
    if distance[start] >= price:
        for value in graph[start]:
            cost = price + value[0]
            if cost < distance[value[1]]:
                distance[value[1]] = cost
                heapq.heappush(s, (cost, value[1]))

print(distance[end])
