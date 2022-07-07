import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt")

input = sys.stdin.readline


def bfs():
    for i in range(length):
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


def dfs(start, flows):
    if start == length - 1:
        return flows

    z = work[start]
    while z < len(graph[start]):
        y = graph[start][z]

        if level[y] == level[start] + 1 and c[start][y] - f[start][y] > 0:
            r = dfs(y, min(flows, c[start][y] - f[start][y]))

            if r > 0:
                f[start][y] += r
                f[y][start] -= r

                work[start] = z
                return r

        z += 1

    work[start] = len(graph[start])
    return 0


n, m = map(int, input().split())

length = 2 + n + m
gets = [0] * length

n_lst = list(map(int, input().split()))
m_lst = list(map(int, input().split()))

for i in range(n):
    gets[1+i] = n_lst[i]

for i in range(m):
    gets[n+1+i] = m_lst[i]

gets[-1] = int(1e11)

c = [[0] * length for _ in range(length)]
f = [[0] * length for _ in range(length)]
graph = defaultdict(list)

for i in range(1, n+1):
    c[i][length-1] = gets[length-1]

    graph[i].append(length-1)
    graph[length-1].append(i)

for i in range(n+1, length-1):
    c[0][i] = gets[i]

    graph[0].append(i)
    graph[i].append(0)

    friends = list(map(int, input().split()))

    for j in range(1, friends[0]+1):
        c[i][friends[j]] = gets[friends[j]]
        graph[i].append(friends[j])
        graph[friends[j]].append(i)

level = [-1] * length
result = 0

while bfs():
    work = [0] * length

    while True:
        flow = dfs(0, int(1e11))
        if flow == 0:
            break
        result += flow

print(result)