import sys
sys.stdin = open("input.txt")


def dfs(mat, start, sub):
    q = start[:]
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = []

    while q:
        y, x = q.pop(0)
        for i in range(4):
            dy = y + d[i][0]
            dx = x + d[i][1]
            if 0 <= dy < n and 0 <= dx < m and mat[dy][dx] == 0 and (dy, dx) not in visited:
                visited.append((dy, dx))
                q.append((dy, dx))
                sub -= 1

    return sub


def bruteforce(level=0, idx=0):
    global matrix, result, virus
    if level == 3:
        s = cnt
        a = dfs(matrix, virus, s)
        if a > result:
            result = a
        return
    else:
        for i in range(idx, empty_num):
            if not empty_check[i]:
                empty_check[i] = True
                matrix[empty[i][0]][empty[i][1]] = 1
                bruteforce(level+1, i+1)
                matrix[empty[i][0]][empty[i][1]] = 0
                empty_check[i] = False


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = n * m - 3
virus = []
empty = []
result = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            empty.append((i, j))
        elif matrix[i][j] == 2:
            virus.append((i, j))
            cnt -= 1
        else:
            cnt -= 1

empty_num = len(empty)
empty_check = [False] * empty_num

bruteforce()

print(result)
