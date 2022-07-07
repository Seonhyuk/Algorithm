import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt")

input = sys.stdin.readline


def bfs():
    for i in range(52):
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

    return level[25] != -1


def dfs(start, flow):
    if start == 25:
        return flow

    z = work[start]
    while z < len(graph[start]):
        y = graph[start][z]

        if level[y] == level[start] + 1 and c[start][y] - f[start][y] > 0:
            res = dfs(y, min(flow, c[start][y]-f[start][y]))

            if res > 0:
                f[start][y] += res
                f[y][start] -= res

                work[start] = z

                return res

        z += 1

    work[start] = len(graph[start])
    return 0


n = int(input())

graph = defaultdict(list)

c = [[0] * 52 for _ in range(52)]
f = [[0] * 52 for _ in range(52)]

for _ in range(n):
    s, e, fl = input().split()

    s = ord(s)
    if 65 <= s < 91:
        s -= 65
    else:
        s -= 71

    e = ord(e)
    if 65 <= e < 91:
        e -= 65
    else:
        e -= 71

    fl = int(fl)

    c[s][e] = fl
    graph[s].append(e)
    graph[e].append(s)

level = [-1] * 52

result = 0

while bfs():
    work = [0] * 52

    while True:
        flows = dfs(0, 100000000)
        if flows == 0:
            break
        result += flows

print(result)
