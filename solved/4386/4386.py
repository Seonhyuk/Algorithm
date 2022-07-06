import sys
import heapq


def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


def union(n1, n2):
    root1 = find(n1)
    root2 = find(n2)
    parent[root2] = root1


n = int(input())
stars = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

parent = list(range(n+1))

q = []
for i in range(n-1):
    for j in range(i+1, n):
        heapq.heappush(q, (((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])** 2)**(1/2), i+1, j+1))

lines = 0
result = 0

while lines < n-1:
    dist, start, end = heapq.heappop(q)
    if find(start) != find(end):
        union(start, end)
        result += dist
        lines += 1

print(f'{result:0.2f}')