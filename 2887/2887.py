import sys
import heapq
# sys.stdin = open("input.txt")


def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


def union(n1, n2):
    root1 = find(n1)
    root2 = find(n2)
    parent[root2] = root1


n = int(input())
parent = list(range(n+1))
tunnel = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    tunnel.append((a, b, c, i))

tu = []
for i in range(3):
    tunnel.sort(key=lambda x: x[i])
    for j in range(1, n):
        heapq.heappush(tu, (abs(tunnel[j][i] - tunnel[j-1][i]), tunnel[j][3], tunnel[j-1][3]))

edge = 0
result = 0

while edge < n-1:
    w, start, end = heapq.heappop(tu)
    if find(start) != find(end):
        union(start, end)
        edge += 1
        result += w

print(result)