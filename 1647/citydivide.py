import sys
import heapq


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    parent[root2] = root1


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

road = []
for _ in range(m):
    a, b, w = map(int, input().split())
    heapq.heappush(road, (w, a, b))

weight = []
edges = 0

while edges < n-1:
    w, start, end = heapq.heappop(road)
    if find(start) != find(end):
        union(start, end)
        weight.append(w)
        edges += 1

weight.pop()
print(sum(weight))