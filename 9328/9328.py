import sys, heapq
from collections import defaultdict

sys.stdin = open("input.txt")
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    matrix = [list(input()) for _ in range(n)]

    key = input().strip()
    keys = defaultdict(bool)

    if key != '0':
        for k in key:
            keys[k.upper()] = True
    result = 0
    doors = []
    for i in range(n):
        if i == 0 or i == n - 1:
            lst = range(m)
        else:
            lst = [0, m-1]

        for j in lst:
            if matrix[i][j] != '*':
                if matrix[i][j] == '.':
                    doors.append((0, i, j))
                elif 65 <= ord(matrix[i][j]) <= 90:
                    if keys[matrix[i][j]]:
                        doors.append((0, i, j))
                        matrix[i][j] = '.'
                    else:
                        doors.append((1, i, j))
                elif 97 <= ord(matrix[i][j]) <= 122:
                    keys[matrix[i][j].upper()] = True
                    doors.append((0, i, j))
                    matrix[i][j] = '.'
                elif matrix[i][j] == '$':
                    result += 1
                    doors.append((0, i, j))
                    matrix[i][j] = '.'

    check = [[False] * m for _ in range(n)]

    for d in doors:
        check[d[1]][d[2]] = True

    heapq.heapify(doors)

    while doors and doors[0][0] < 100:
        a, y, x = heapq.heappop(doors)

        if a >= 1:
            if not keys[matrix[y][x]]:
                heapq.heappush(doors, (a+1, y, x))
                continue

        for i in range(4):
            dy = y + directions[i][0]
            dx = x + directions[i][1]

            if 0 <= dy < n and 0 <= dx < m and not check[dy][dx]:
                alpha = matrix[dy][dx]
                if alpha == '*':
                    continue
                elif alpha == '.':
                    check[dy][dx] = True
                    heapq.heappush(doors, (0, dy, dx))
                elif 65 <= ord(alpha) <= 95:
                    if keys[alpha]:
                        check[dy][dx] = True
                        matrix[dy][dx] = '.'
                        heapq.heappush(doors, (0, dy, dx))
                    else:
                        check[dy][dx] = True
                        heapq.heappush(doors, (a+1, dy, dx))
                elif 97 <= ord(alpha) <= 122:
                    check[dy][dx] = True
                    keys[alpha.upper()] = True
                    matrix[dy][dx] = '.'
                    heapq.heappush(doors, (0, dy, dx))
                elif alpha == '$':
                    check[dy][dx] = True
                    result += 1
                    heapq.heappush(doors, (0, dy, dx))
                    matrix[dy][dx] = '.'

    print(result)