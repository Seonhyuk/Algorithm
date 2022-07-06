import sys
import heapq

v, e = map(int, input().split())
start = int(input())
INF = 1e09
distance = [INF] * (v+1)

graph = [[] for _ in range(v+1)]

for _ in range(e):
    u, t, w = map(int, sys.stdin.readline().split())
    graph[u].append([t, w])

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue

    for next in graph[node]:
        cost = distance[node] + next[1]
        if cost < distance[next[0]]:
            distance[next[0]] = cost
            heapq.heappush(q, (cost, next[0]))


for i in range(1, v+1):
    print(distance[i] if distance[i] != INF else 'INF')