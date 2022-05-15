import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt")


def dfs(graph, start):
    global n
    check = [False] * (n+1)
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        if not check[node]:
            check[node] = True
            visited.append(node)
            cand = graph[node]
            cand.reverse()
            stack.extend(cand)

    return visited


def bfs(graph, start):
    global n
    q = deque()
    q.append(start)
    visited = []
    check = [False] * (n+1)

    while q:
        node = q.popleft()
        if not check[node]:
            check[node] = True
            visited.append(node)
            q.extend(graph[node])

    return visited


n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for key in graph.keys():
    graph[key].sort()

a = bfs(graph, v)
b = dfs(graph, v)
print(*b)
print(*a)

