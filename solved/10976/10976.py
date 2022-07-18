import sys
from collections import defaultdict, deque

sys.stdin = open("input.txt")

input = sys.stdin.readline


def bfs():
    for i in range(n+1):
        level[i] = -1

    level[1] = 0
    q = deque()
    q.append(1)

    while q:
        x = q.popleft()

        for y in graph[x]:
            if level[y] == -1 and c[x][y] - f[x][y] > 0:
                level[y] = level[x] + 1
                q.append(y)

    return level[-1] != -1


def dfs(x, flows):
    if x == n:
        return flows

    z = work[x]
    while z < len(graph[x]):
        y = graph[x][z]

        if level[y] == level[x] + 1 and c[x][y] - f[x][y] > 0:
            r = dfs(y, min(flows, c[x][y] - f[x][y]))

            if r > 0:
                f[x][y] += r
                f[y][x] -= r

                work[x] = z
                return r

        z += 1

    work[x] = len(graph[x])
    return 0


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    c = [[0] * (n+1) for _ in range(n+1)]
    f = [[0] * (n+1) for _ in range(n+1)]

    graph = defaultdict(list)

    for _ in range(m):
        x, y = map(int, input().split())

        graph[x].append(y)
        graph[y].append(x)
        if x == 1 or x == n or y == 1 or y == n:
            c[x][y] = 1
        else:
            c[x][y] = 1000

    level = [-1] * (n+1)
    result = 0

    while bfs():
        work = [0] * (n+1)

        while True:
            flow = dfs(1, 100000)
            if flow == 0:
                break
            result += flow

    print(result)

