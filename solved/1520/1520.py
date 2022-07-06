import sys
sys.setrecursionlimit(25000)


def dp(y, x):
    if y == 0 and x == 0:
        return 1

    if computed[y][x]:
        return mat[y][x]

    value = 0
    for i in range(4):
        dy = y + d[i][0]
        dx = x + d[i][1]
        if 0 <= dy < n and 0 <= dx < m and matrix[y][x] < matrix[dy][dx]:
            value += dp(dy, dx)

    mat[y][x] = value
    computed[y][x] = True
    return value


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

computed = [[False] * m for _ in range(n)]

result = 0
mat = [[0] * m for _ in range(n)]
mat[0][0] = 1

dp(n-1, m-1)

print(mat[n-1][m-1])