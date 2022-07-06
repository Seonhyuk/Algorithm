import sys
from collections import deque

sys.stdin = open("input.txt")

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

k, w, b = (0, 0), [], (0, 0)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            k = (i, j)
        elif matrix[i][j] == '*':
            w.append((i, j, 0))
        elif matrix[i][j] == 'D':
            b = (i, j)

distance = [[0] * m for _ in range(n)]

q = deque(w)
q.append((k[0], k[1], 1))
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y, x, t = q.popleft()

    for i, j in d:
        dy = y + i
        dx = x + j

        if 0 <= dy < n and 0 <= dx < m:
            if t and matrix[dy][dx] != '*' and matrix[dy][dx] != 'X' and not distance[dy][dx]:
                distance[dy][dx] = distance[y][x] + 1
                q.append((dy, dx, 1))

            elif not t and (matrix[dy][dx] == '.' or matrix[dy][dx] == 'S'):
                matrix[dy][dx] = '*'
                q.append((dy, dx, 0))

if distance[b[0]][b[1]]:
    print(distance[b[0]][b[1]])
else:
    print('KAKTUS')
