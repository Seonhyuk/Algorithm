import sys
from collections import deque, defaultdict
sys.stdin = open("input.txt")

input = sys.stdin.readline


def bfs():
    for i in range(n):
        level[i] = -1

    level[s] = 0
    q = deque()
    q.append(s)

    while q:
        x = q.popleft()

        for i in range(n):
            if level[i] == -1 and c[x][i] - f[x][i] > 0:
                level[i] = level[x] + 1
                q.append(i)

    return level[t] != -1


def dfs(start, flows):
    if start == t:
        return flows

    z = work[start]

    for y in range(z, n):
        if level[y] == level[start] + 1 and c[start][y] - f[start][y] > 0:
            res = dfs(y, min(flows, c[start][y] - f[start][y]))

            if res > 0:
                f[start][y] += res
                f[y][start] -= res

                work[start] = y
                return res

    work[start] = n - 1
    return 0


n, m = map(int, input().split())

graph = defaultdict(list)
c = [[0] * n for _ in range(n)]
f = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())

    start, end = a-1, b-1

    c[start][end] = w
    c[end][start] = w
    graph[start].append(end)
    graph[end].append(start)

s, t = map(int, input().split())
s, t = s-1, t-1

level = [-1] * n

result = 0

while bfs():
    work = [0] * n

    while True:
        flow = dfs(s, int(1e09))
        if flow <= 0:
            break
        result += flow

print(result)
