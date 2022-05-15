import sys
from collections import defaultdict, deque
# sys.stdin = open("test.txt")

n, m = map(int, input().split())

in_degree = [0] * (n+1)
graph = defaultdict(list)

for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(1, order[0]):
        graph[order[i]].append(order[i+1])
        in_degree[order[i+1]] += 1

q = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

result = []
cnt = 0
while q:
    x = q.popleft()
    result.append(x)
    cnt += 1
    if x in graph:
        for t in graph[x]:
            in_degree[t] -= 1
            if in_degree[t] == 0:
                q.append(t)

if cnt == n:
    for i in range(n):
        print(result[i])
else:
    print(0)