import sys
sys.stdin = open("input.txt")

from copy import deepcopy


def make_array(a, level=0):
    if level == 10:
        arr.append(a[:])
        return

    for i in range(4):
        if len(a) == 0:
            make_array(a + [i], level+1)
        else:
            if (i != a[-1]) and (i % 2 != a[-1] % 2):
                make_array(a + [i], level+1)


n, m = map(int, input().split())
arr = []
make_array([])
mat = [list(input()) for _ in range(n)]

r, b = 0, 0


for i in range(n):
    for j in range(m):
        if mat[i][j] == 'R':
            r = (i, j)
        elif mat[i][j] == 'B':
            b = (i, j)

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

result = 11

for method in arr:
    red, blue = r, b
    matrix = deepcopy(mat)
    sub_result = 11
    on_blue = False

    for i in range(10):
        if i+1 >= result:
            break

        q = [red]
        meet_blue = False
        on_red = False

        while q:
            y, x = q.pop()

            dy = y + directions[method[i]][0]
            dx = x + directions[method[i]][1]

            if matrix[dy][dx] != '#':
                if matrix[dy][dx] == '.':
                    matrix[y][x] = '.'
                    matrix[dy][dx] = 'R'
                    red = (dy, dx)
                    q.append(red)
                elif matrix[dy][dx] == 'O':
                    matrix[y][x] = '.'
                    sub_result = i + 1
                    on_red = True
                    break
                elif matrix[dy][dx] == 'B':
                    meet_blue = True

        q = [blue]

        while q:
            y, x = q.pop()

            dy = y + directions[method[i]][0]
            dx = x + directions[method[i]][1]

            if matrix[dy][dx] != '#':
                if matrix[dy][dx] == '.':
                    matrix[y][x] = '.'
                    matrix[dy][dx] = 'B'
                    blue = (dy, dx)
                    q.append((dy, dx))
                elif matrix[dy][dx] == 'O':
                    matrix[y][x] = '.'
                    on_blue = True
                    break

        if on_blue:
            break

        if on_red:
            result = min(result, sub_result)
            break

        q = [red]

        while q:
            y, x = q.pop()

            dy = y + directions[method[i]][0]
            dx = x + directions[method[i]][1]

            if matrix[dy][dx] != '#':
                if matrix[dy][dx] == '.':
                    matrix[y][x] = '.'
                    matrix[dy][dx] = 'R'
                    red = (dy, dx)
                    q.append(red)
                elif matrix[dy][dx] == 'O':
                    matrix[y][x] = '.'
                    sub_result = i + 1
                    on_red = True
                    break
                elif matrix[dy][dx] == 'B':
                    meet_blue = True

        q = [blue]

        while q:
            y, x = q.pop()

            dy = y + directions[method[i]][0]
            dx = x + directions[method[i]][1]

            if matrix[dy][dx] != '#':
                if matrix[dy][dx] == '.':
                    matrix[y][x] = '.'
                    matrix[dy][dx] = 'B'
                    blue = (dy, dx)
                    q.append((dy, dx))
                elif matrix[dy][dx] == 'O':
                    matrix[y][x] = '.'
                    on_blue = True
                    break

        if on_blue:
            break

        if on_red:
            result = min(result, sub_result)
            break


if result > 10:
    result = -1

print(result)