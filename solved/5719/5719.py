import sys
import heapq
from collections import deque

sys.stdin = open("input.txt")

input = sys.stdin.readline


def dijstra():
    q = []
    q.append((0, s))

    distance = [inf] * n
    distance[s] = 0

    while q:
        dist, end = heapq.heappop(q)

        if distance[end] >= dist:

            for next in graph[end]:
                new = dist + next[0]
                if matrix[end][next[1]] and distance[next[1]] > new:
                    distance[next[1]] = new
                    heapq.heappush(q, (new, next[1]))

    return distance


def bfs():
    q = deque()
    q.append(d)

    while q:
        x = q.popleft()

        for prev in inverse[x]:
            if x == s: continue
            if result[x] - prev[0] == result[prev[1]] and matrix[prev[1]][x]:
                matrix[prev[1]][x] = False
                q.append(prev[1])


while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())

    inf = int(1e07)

    graph = [[] for _ in range(n)]
    inverse = [[] for _ in range(n)]

    for i in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((p, v))
        inverse[v].append((p, u))

    matrix = [[True] * n for _ in range(n)]

    result = dijstra()
    bfs()
    result = dijstra()

    print(result[d] if result[d] != inf else -1)
