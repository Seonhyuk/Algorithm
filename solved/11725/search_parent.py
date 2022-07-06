import sys

n = int(input())
parent = [0] * (n+1)
tree = {}

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    try:
        tree[a].append(b)
    except Exception:
        tree[a] = [b]

    try:
        tree[b].append(a)
    except Exception:
        tree[b] = [a]

q = [1]
visited = [False] * (n+1)
visited[1] = True

while q:
    v = q.pop(0)
    for i in tree[v]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            parent[i] = v

for j in range(2, n+1):
    print(parent[j])