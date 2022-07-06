import sys
from collections import deque


sys.stdin = open("input.txt")
input = sys.stdin.readline


def maximum_flow():
    global result
    global n

    while True:
        v = [-1] * (n+1)

        q = deque()
        q.append(1)

        while q:
            x = q.popleft()

            if x == 2:
                break

            for y in range(n+1):
                if c[x][y] - f[x][y] > 0 and v[y] == -1:
                    q.append(y)
                    v[y] = x

        if v[2] == -1:
            break

        idx = 2
        while idx != 1:
            f[v[idx]][idx] += 1
            f[idx][v[idx]] -= 1
            idx = v[idx]

        result += 1


n, m = map(int, input().split())

c = [[0] * (n+1) for _ in range(n+1)]
f = [[0] * (n+1) for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    c[s][e] += 1
    graph[s].append(e)

result = 0
maximum_flow()

print(result)