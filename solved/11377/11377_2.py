import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt")

input = sys.stdin.readline


def bfs():
    for i in range(length):
        level[i] = -1

    q = deque()
    q.append(0)
    level[0] = 0

    while q:
        x = q.popleft()

        for y in graph[x]:
            if level[y] == -1 and c[x][y] - f[x][y] > 0:
                level[y] = level[x] + 1
                q.append(y)

    return level[length-1] != -1


def dfs(x, flow):
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

                work[x] = z
                return r

        z += 1

    work[x] = z
    return 0


n, m, k = map(int, input().split())
length = n + m + 3

graph = defaultdict(list)
c = [[0] * length for _ in range(length)]
f = [[0] * length for _ in range(length)]

c[0][length-2] = k
graph[0].append(length-2)
graph[length-2].append(0)

for i in range(1, n+1):
    c[0][i] = 1
    c[length-2][i] = 1

    graph[0].append(i)
    graph[i].append(0)
    graph[length-2].append(i)
    graph[i].append(length-2)

for i in range(1, m+1):
    c[n+i][length-1] = 1

    graph[n+i].append(length-1)
    graph[length-1].append(n+i)

for i in range(1, n+1):
    works = deque(map(int, input().split()))
    num = works.popleft()

    for j in range(num):
        c[i][n+works[j]] = 1

        graph[i].append(n+works[j])
        graph[n+works[j]].append(i)

result = 0

level = [-1] * length

while bfs():
    work = [0] * length

    while True:
        flows = dfs(0, 1000)

        if flows <= 0:
            break

        result += flows

print(result)