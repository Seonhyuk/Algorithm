import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
check = [[0] * m for _ in range(n)]

d = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

cnt = 0
sector = 0
for i in range(n):
    for j in range(m):
        if check[i][j] == 0:
            sector += 1

            q = [(i, j)]
            check[i][j] = sector

            while q:
                y, x = q.pop(0)
                dy = y + d[matrix[y][x]][0]
                dx = x + d[matrix[y][x]][1]
                if 0 <= dy < n and 0 <= dx < m:
                    if check[dy][dx] == 0:
                        check[dy][dx] = sector
                        q.append((dy, dx))
                    elif check[dy][dx] != 0 and check[dy][dx] != sector:
                        cnt += 1

print(sector - cnt)