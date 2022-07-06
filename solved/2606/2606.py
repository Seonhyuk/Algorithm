import sys
from collections import defaultdict, deque

n = int(input())
m = int(input())

visited = [False] * (n+1)
result = 0

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = deque([1])
visited[1] = True
while q:
    node = q.popleft()
    for next in graph[node]:
        if not visited[next]:
            result += 1
            q.append(next)
            visited[next] = True

print(result)