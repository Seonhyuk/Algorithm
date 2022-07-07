import sys
from collections import defaultdict, deque

sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(s, e):
    global result

    while True:
        v = [-1] * length

        q = deque()
        q.append(s)

        while q:
            x = q.popleft()

            if x == e:
                break

            for y in graph[x]:
                if v[y] == -1 and c[x][y] - f[x][y] > 0:
                    q.append(y)
                    v[y] = x

        if v[e] == -1:
            break

        flow = 1000000

        idx = e
        while idx != s:
            flow = min(flow, c[v[idx]][idx] - f[v[idx]][idx])
            idx = v[idx]

        idx = e
        while idx != s:
            f[v[idx]][idx] += flow
            f[idx][v[idx]] -= flow
            idx = v[idx]

        result += flow


n, k, d = map(int, input().split())

length = n + d + 2
c = [[0] * length for _ in range(length)]
f = [[0] * length for _ in range(length)]

graph = defaultdict(list)

for i in range(1, n+1):
    c[0][i] = k
    graph[0].append(i)
    graph[i].append(0)

d_lst = list(map(int, input().split()))
for i in range(d):
    c[n+1+i][n+d+1] = d_lst[i]
    graph[n+1+i].append(n+d+1)
    graph[n+d+1].append(n+1+i)

for i in range(1, 1+n):
    foods = list(map(int, input().split()))

    for j in range(1, foods[0]+1):
        c[i][n+foods[j]] = 1
        graph[i].append(n+foods[j])
        graph[n+foods[j]].append(i)

result = 0

bfs(0, n+d+1)

print(result)


# dinic 알고리즘

import sys
from collections import deque, defaultdict
sys.stdin = open("input.txt")

input = sys.stdin.readline

inf = int(1e09)


def bfs():
    for i in range(length):
        level[i] = -1

    level[0] = 0

    q = deque()
    q.append(0)

    while q:
        x = q.popleft()

        for y in adj[x]:
            if level[y] == -1 and c[x][y] - f[x][y] > 0:
                level[y] = level[x] + 1
                q.append(y)

    return level[-1] != -1


def dfs(x, flows):
    if x == t:
        return flows

    z = work[x]
    while z < len(adj[x]):

        y = adj[x][z]

        if level[y] == level[x] + 1 and c[x][y] - f[x][y] > 0:
            r = dfs(y, min(c[x][y] - f[x][y], flows))

            if r > 0:
                f[x][y] += r
                f[y][x] -= r

                work[x] = z
                return r

        z += 1

    work[x] = len(adj[x])
    return 0


n, k, d = map(int, input().split())

adj = defaultdict(list)

length = n + d + 2

c = [[0] * length for _ in range(length)]
f = [[0] * length for _ in range(length)]
level = [-1] * length

t = length - 1


for i in range(1, n+1):
    c[0][i] = k

    adj[0].append(i)
    adj[i].append(0)

values = list(map(int, input().split()))
for i in range(1, 1+d):
    val = values[i-1]

    c[n+i][t] = val
    adj[t].append(n+i)
    adj[n+i].append(t)


for i in range(1, 1+n):
    foods = list(map(int, input().split()))

    for j in range(1, foods[0]+1):
        c[i][n+foods[j]] = 1
        adj[i].append(n+foods[j])
        adj[n+foods[j]].append(i)

result = 0

while bfs():
    work = [0] * length

    while True:
        flow = dfs(0, inf)
        if flow == 0:
            break
        result += flow

print(result)