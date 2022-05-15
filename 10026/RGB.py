import sys
sys.stdin = open("input.txt")


def bfs(start, c, t=0):
    global matrix, n, cnt_max, cnt, cnt2

    if t == 0:
        rgb = [matrix[start[0]][start[1]]]
    elif t == 1:
        if matrix[start[0]][start[1]] == 'G' or matrix[start[0]][start[1]] == 'R':
            rgb = ['G', 'R']
        else:
            rgb = ['B']

    c[start[0]][start[1]] = False
    q = [start]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        point = q.pop(0)
        for i in range(4):
            dy = point[0] + d[i][0]
            dx = point[1] + d[i][1]
            if 0 <= dy < n and 0 <= dx < n:
                if matrix[dy][dx] in rgb and c[dy][dx]:
                    c[dy][dx] = False
                    q.append((dy, dx))

    if t == 0:
        cnt += 1
    if t == 1:
        cnt2 += 1


n = int(input())
check = [[True for _ in range(n)] for _ in range(n)]
check2 = [[True for _ in range(n)] for _ in range(n)]
matrix = [input() for _ in range(n)]

cnt = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if check[i][j]:
            bfs((i, j), check)
        if check2[i][j]:
            bfs((i, j), check2, 1)

print(cnt, cnt2)