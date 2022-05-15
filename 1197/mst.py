import heapq
import sys


def prim(graph, start):
    candidate = graph[start]
    heapq.heapify(candidate)
    visited[start] = True
    mst = []
    total = 0

    while candidate:
        w, s, e = heapq.heappop(candidate)
        if not visited[e]:
            visited[e] = True
            total += w
            mst.append([s, e])
            for node in graph[e]:
                if not visited[node[2]]:
                    heapq.heappush(candidate, node)

    return total


v, e = map(int, input().split())
graph = {}
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    try:
        graph[a].append([c, a, b])
    except Exception:
        graph[a] = [[c, a, b]]

    try:
        graph[b].append([c, b, a])
    except Exception:
        graph[b] = [[c, b, a]]

visited = [False] * (v+1)
print(prim(graph, 1))