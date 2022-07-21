import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt")

input = sys.stdin.readline


def max_flow(start, end):
    global result
    global length

    while True:
        v = [-1] * length
        q = deque()
        q.append(start)

        while q:
            x = q.popleft()

            for y in graph[x]:
                if c[x][y] - f[x][y] > 0 and v[y] == -1:
                    q.append(y)
                    v[y] = x

                    if y == end:
                        break

        if v[end] == -1:
            break

        flow = 1000

        idx = end
        while idx != start:
            flow = min(flow, c[v[idx]][idx] - f[v[idx]][idx])
            idx = v[idx]

        idx = end
        while idx != start:
            f[v[idx]][idx] += flow
            f[idx][v[idx]] -= flow
            idx = v[idx]

        result += flow


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

max_flow(0, length-1)

print(result)