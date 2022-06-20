import sys
from collections import deque
sys.stdin = open("input.txt")

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = 0
while True:
    check = 0
    check_matrix = [[False] * m for _ in range(n)]
    melted = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and not check_matrix[i][j]:
                check_matrix[i][j] = True
                check += 1

                q = deque()
                q.append((i, j))

                while q:
                    y, x = q.popleft()
                    for t in range(4):
                        dy = y + d[t][0]
                        dx = x + d[t][1]
                        if 0 <= dy < n and 0 <= dx < m and matrix[dy][dx] and not check_matrix[dy][dx]:
                            check_matrix[dy][dx] = True
                            q.append((dy, dx))

            if matrix[i][j]:
                for t in range(4):
                    di = i + d[t][0]
                    dj = j + d[t][1]
                    if 0 <= di < n and 0 <= dj < m and not matrix[di][dj]:
                        melted[i][j] += 1

    if check != 1:
        break

    for i in range(n):
        for j in range(m):
            matrix[i][j] -= melted[i][j]
            if matrix[i][j] < 0:
                matrix[i][j] = 0

    result += 1

if not check:
    result = 0

print(result)
