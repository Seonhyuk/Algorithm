import sys
from collections import defaultdict, deque
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


def dfs(x, flows):
    if x == size - 1:
        return flows

    z = work[x]

    for p in range(z, len(graph[x])):
        y = graph[x][p]

        if level[y] == level[x] + 1 and c[x][y] - f[x][y] > 0:
            res = dfs(y, min(flows, c[x][y] - f[x][y]))

            if res > 0:
                f[x][y] += res
                f[y][x] -= res

                work[x] = p + 1
                return res

    work[x] = len(graph[x])
    return 0


t = int(input())
d = [(-1, -1), (0, -1), (-1, 1), (0, 1), (1, -1), (1, 1)]

for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]

    total = n * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'x':
                total -= 1

    size = n * m + 2

    c = [[0] * size for _ in range(size)]
    f = [[0] * size for _ in range(size)]

    graph = defaultdict(list)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'x':
                continue

            node_num = m * i + j + 1

            if j % 2 == 0:
                c[node_num][size-1] = 1
                graph[node_num].append(size-1)
                graph[size-1].append(node_num)

            else:
                c[0][node_num] = 1
                graph[0].append(node_num)
                graph[node_num].append(0)

                for x in range(6):
                    di = i + d[x][0]
                    dj = j + d[x][1]

                    if 0 <= di < n and 0 <= dj < m:
                        to_node_num = m * di + dj + 1

                        c[node_num][to_node_num] = 1
                        graph[node_num].append(to_node_num)
                        graph[to_node_num].append(node_num)

    level = [-1] * size

    result = 0

    while bfs():
        work = [0] * size

        while True:
            flow = dfs(0, 1000)

            if flow < 1:
                break
            result += flow

    print(total - result)
