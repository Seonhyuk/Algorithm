import sys
from collections import deque
# sys.stdin = open("input.txt")


def bfs(y, x):
    global n, m

    q = deque([(y, x)])

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + d[i][0]
            dx = x + d[i][1]
            if 0 <= dy < n and 0 <= dx < m and matrix[dy][dx] and not check[dy][dx]:
                check[dy][dx] = True
                q.append((dy, dx))


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())

    matrix = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1

    check = [[False] * m for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and not check[i][j]:
                check[i][j] = True
                bfs(i, j)
                result += 1

    print(result)