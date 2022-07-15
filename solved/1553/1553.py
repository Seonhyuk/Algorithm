import sys
sys.stdin = open("input.txt")


def dfs(start, cnt):
    global result

    if cnt == 28:
        result += 1
        return

    if not check[start//7][start%7]:
        y = start // 7
        x = start % 7
        c = 0
        for i in range(4):
            dy = y + d[i][0]
            dx = x + d[i][1]

            if 0 <= dy < 8 and 0 <= dx < 7 and not check[dy][dx]:
                if matrix[y][x] > matrix[dy][dx]:
                    a = matrix[dy][dx]
                    b = matrix[y][x]
                else:
                    a = matrix[y][x]
                    b = matrix[dy][dx]

                if domino[(a, b)]:
                    c += 1
                    continue
                else:
                    domino[(a, b)] = True
                    check[y][x] = True
                    check[dy][dx] = True
                    dfs(start+1, cnt+1)
                    domino[(a, b)] = False
                    check[y][x] = False
                    check[dy][dx] = False

        if c == 4:
            return

    else:
        dfs(start+1, cnt)


matrix = [list(map(int, input())) for _ in range(8)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
check = [[False] * 7 for _ in range(8)]
domino = dict()

for i in range(7):
    for j in range(i, 7):
        domino[(i, j)] = False

result = 0
dfs(0, 0)

print(result)