import sys
from collections import deque

n =  int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
size = 2
eat = 0
shark = (0, 0)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            shark = (i, j)

dist = 0
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
inf = 999
while True:
    distance = [[inf] * n for _ in range(n)]
    distance[shark[0]][shark[1]] = 0
    matrix[shark[0]][shark[1]] = 0
    q = deque()
    q.append(shark)

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + d[i][0]
            dx = x + d[i][1]
            if 0 <= dy < n and 0 <= dx < n:
                if matrix[dy][dx] <= size and distance[dy][dx] > distance[y][x] + 1:
                    distance[dy][dx] = distance[y][x] + 1
                    q.append((dy, dx))

    eat_i, eat_j = 0, 0
    min_dist = 999
    eat_possible = False
    for i in range(n):
        for j in range(n):
            if distance[i][j] < min_dist and 0 < matrix[i][j] < size:
                min_dist = distance[i][j]
                eat_i, eat_j = i, j
                eat_possible = True

    if eat_possible:
        dist += min_dist
        eat += 1
        if eat == size:
            eat = 0
            size += 1
        shark = (eat_i, eat_j)
        matrix[eat_i][eat_j] = 0
    else:
        break

print(dist)