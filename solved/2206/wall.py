import sys
from collections import deque

n, m = map(int, input().split())
matrix = [sys.stdin.readline() for _ in range(n)]
distance = -1

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 1))
visited[0][0][1] = 1

while q:
    y, x, w = q.popleft()

    if y == n-1 and x == m-1:
        distance = visited[y][x][w]
        break

    for i in range(4):
        dy = y + d[i][0]
        dx = x + d[i][1]
        if 0 <= dy < n and 0 <= dx < m:
            if matrix[dy][dx] == '1' and w == 1:
                visited[dy][dx][0] = visited[y][x][1] + 1
                q.append((dy, dx, 0))
            elif matrix[dy][dx] == '0' and not visited[dy][dx][w]:
                visited[dy][dx][w] = visited[y][x][w] + 1
                q.append((dy, dx, w))

print(distance)
