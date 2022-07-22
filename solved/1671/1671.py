import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt")

input = sys.stdin.readline


def bfs():
    for i in range(size):
        level[i] = -1

    level[0] = 0

    q = deque()
    q.append(0)

    while q:
        x = q.popleft()

        for y in graph[x]:
            if level[y] == -1 and c[x][y] - f[x][y] > 0:
                level[y] = level[x] + 1
                q.append(y)

    return level[-1] != -1


def dfs(x, flow):
    if x == size - 1:
        return flow

    z = works[x]
    while z < len(graph[x]):
        y = graph[x][z]

        if level[y] == level[x] + 1 and c[x][y] - f[x][y] > 0:
            r = dfs(y, min(flow, c[x][y] - f[x][y]))

            if r > 0:
                f[x][y] += r
                f[y][x] -= r

                works[x] = z
                return r

        z += 1

    works[x] = z
    return 0


n = int(input())
sharks = [list(map(int, input().split())) for _ in range(n)]

graph = defaultdict(list)

size = 2 * n + 2

c = [[0] * size for _ in range(size)]
f = [[0] * size for _ in range(size)]

for i in range(1, n+1):
    c[0][i] = 2
    c[n + i][size-1] = 1

    graph[0].append(i)
    graph[i].append(0)
    graph[n+i].append(size-1)
    graph[size-1].append(n+i)

for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(3):
                if sharks[i][k] < sharks[j][k]:
                    break
            else:
                if sharks[i] == sharks[j] and j > i:
                    continue

                c[i+1][n+j+1] = 1

                graph[i+1].append(n+j+1)
                graph[n+j+1].append(i+1)

level = [-1] * size
result = 0

while bfs():
    works = [0] * size

    while True:
        flows = dfs(0, 1000000)
        if flows < 1:
            break

        result += flows

if result == n:
    result -= 1

print(n-result)