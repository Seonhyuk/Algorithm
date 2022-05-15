import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]

    time = [[0 for _ in range(m)] for _ in range(n)]

    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    que = [(0, 0)]
    visited = [(0, 0)]

    while que:
        a = que.pop(0)
        y, x = a[0], a[1]
        for i in range(4):
            dy = y + d[i][0]
            dx = x + d[i][1]
            if 0 <= dy < n and 0 <= dx < m and matrix[dy][dx] == '1':
                if (dy, dx) not in visited:
                    visited.append((dy, dx))
                    que.append((dy, dx))
                    time[dy][dx] = time[y][x] + 1

    print(time[n-1][m-1] + 1)