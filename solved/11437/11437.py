import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

p = [-1] * (n+1)
l = [0] * (n+1)
v = [False] * (n+1)
p[1] = 0

graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

while q:
    node = q.popleft()
    v[node] = True

    for next in graph[node]:
        if not v[next]:
            p[next] = node
            l[next] = l[node] + 1
            q.append(next)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    while l[a] != l[b]:
        if l[a] > l[b]:
            a = p[a]
        else:
            b = p[b]

    while a != b:
        a = p[a]
        b = p[b]

    print(a)