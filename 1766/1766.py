import sys
import heapq
from collections import defaultdict

# sys.stdin = open("input.txt")

n, m = map(int, input().split())

in_degree = [0] * (n+1)
graph = defaultdict(list)

for _ in range(m):
    pre, post = map(int, sys.stdin.readline().split())
    in_degree[post] += 1
    graph[pre].append(post)

q = []

for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

order = []
while q:
    problem = heapq.heappop(q)
    order.append(problem)
    for p in graph[problem]:
        in_degree[p] -= 1
        if in_degree[p] == 0:
            heapq.heappush(q, p)

print(*order)