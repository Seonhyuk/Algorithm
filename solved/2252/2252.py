import sys
from collections import defaultdict, deque

# sys.stdin = open("test.txt")

n, m = map(int, input().split())

graph = defaultdict(list)
in_degree = [0] * (n+1)
check = [False] * (n+1)

for _ in range(m):
    top, bottom = map(int, sys.stdin.readline().split())
    graph[top].append(bottom)
    in_degree[bottom] += 1

lst = deque()
result = []

for i in range(1, n+1):
    if in_degree[i] == 0:
        lst.append(i)

while lst:
    a = lst.popleft()
    result.append(a)
    if a in graph:
        for k in graph[a]:
            in_degree[k] -= 1
            if in_degree[k] == 0:
                lst.append(k)

print(result)