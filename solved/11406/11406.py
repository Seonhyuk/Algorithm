import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs():
    global length
    for i in range(length):
        level[i] = -1

    level[0] = 0
    q = deque()
    q.append(0)

    while q:
        x = q.popleft()

        for y in graph[x]:
            if level[y] == - 1 and c[x][y] - f[x][y] > 0:
                level[y] = level[x] + 1
                q.append(y)

    return level[-1] != -1


def dfs(x, flow):
    global length
    if x == length - 1:
        return flow

    z = work[x]

    while z < len(graph[x]):
        y = graph[x][z]

        if level[y] == level[x] + 1 and c[x][y] - f[x][y] > 0:
            r = dfs(y, min(flow, c[x][y] - f[x][y]))

            if r > 0:
                f[x][y] += r
                f[y][x] -= r

                return r

        z += 1

    work[x] = z
    return 0


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for _ in range(m)]

length = n + m + 2

c = [[0] * length for _ in range(length)]
f = [[0] * length for _ in range(length)]

graph = defaultdict(list)

for i in range(n):
    c[0][i+1] = a[i]
    graph[0].append(i+1)
    graph[i+1].append(0)

for i in range(m):
    if b[i]:
        c[n+i+1][-1] = b[i]
        graph[length-1].append(n+i+1)
        graph[n+i+1].append(length-1)

for i in range(m):
    for j in range(n):
        if matrix[i][j]:
            c[j+1][n+1+i] = matrix[i][j]
            graph[j+1].append(n+1+i)
            graph[n+1+i].append(j+1)

level = [-1] * length
result = 0

while bfs():
    work = [0] * length

    while True:
        flows = dfs(0, 100000000)
        if flows == 0:
            break
        result += flows

print(result)