import sys
sys.stdin = open("input.txt")


from collections import deque

n, m, k = map(int, input().split())
matrix = [input() for _ in range(n)]
inf = int(1e09)
distance = [[[inf] * (k+1) for _ in range(m)] for _ in range(n)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque()
distance[0][0][0] = 1
q.append((0, 0, 0))
result = inf

while q:
    y, x, level = q.popleft()
    if y == n-1 and x == m-1:
        result = min(result, distance[y][x][level])
    for i in range(4):
        dy = y + d[i][0]
        dx = x + d[i][1]
        if 0 <= dy < n and 0 <= dx < m:
            nlevel = level + 1 if matrix[dy][dx] == '1' else level
            if nlevel <= k:
                if distance[dy][dx][nlevel] == inf or distance[dy][dx][nlevel] > distance[y][x][level]+1:
                    if matrix[dy][dx] == '0':
                        distance[dy][dx][nlevel] = distance[y][x][level] + 1
                    else:
                        if distance[y][x][level] % 2:
                            distance[dy][dx][nlevel] = distance[y][x][level] + 1
                        else:
                            distance[dy][dx][nlevel] = distance[y][x][level] + 2
                    q.append((dy, dx, nlevel))

if result == inf:
    print(-1)
else:
    print(result)