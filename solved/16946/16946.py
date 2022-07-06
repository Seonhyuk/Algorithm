import sys
sys.stdin = open("input.txt")

from collections import deque

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

sector = [[0] * m for _ in range(n)]
check = [[False] * m for  _ in range(n)]

cnt_dict = {}

se = 1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '0' and not check[i][j]:
            q = deque()
            q.append((i, j))
            check[i][j] = True
            sector[i][j] = se
            cnt = 1

            while q:
                y, x = q.popleft()
                for t in range(4):
                    dy = y + d[t][0]
                    dx = x + d[t][1]
                    if 0 <= dy < n and 0 <= dx < m and matrix[dy][dx] == '0':
                        if matrix[dy][dx] == '0' and not check[dy][dx]:
                            cnt += 1
                            check[dy][dx] = True
                            q.append((dy, dx))
                            sector[dy][dx] = se

            cnt_dict[se] = cnt
            se += 1

result = []
for i in range(n):
    sub = ''
    for j in range(m):
        if matrix[i][j] == '0':
            sub += '0'
        else:
            cnt = 1
            selected = set()
            for t in range(4):
                dy = i + d[t][0]
                dx = j + d[t][1]
                if 0 <= dy < n and 0 <= dx < m:
                    if matrix[dy][dx] == '0':
                        if sector[dy][dx] not in selected:
                            selected.add(sector[dy][dx])
                            cnt += cnt_dict[sector[dy][dx]]
            sub += str(cnt%10)
    result.append(sub)

for i in range(n):
    print(result[i])