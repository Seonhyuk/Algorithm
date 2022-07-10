import sys
sys.setrecursionlimit(2500)
sys.stdin = open("input.txt")


def dfs(y, x, cnt=0):
    global result

    if cnt > k[y][x]:
        k[y][x] = cnt
    else:
        return

    if result < cnt:
        result = cnt

    for i in range(4):
        dy = y + d[i][0] * int(matrix[y][x])
        dx = x + d[i][1] * int(matrix[y][x])

        if 0 <= dy < n and 0 <= dx < m:
            if check[dy][dx]:
                print(-1)
                exit()
            else:
                if matrix[dy][dx] == "H":
                    result = max(result, cnt+1)
                else:
                    check[dy][dx] = True
                    dfs(dy, dx, cnt+1)
                    check[dy][dx] = False
        else:
            result = max(result, cnt+1)


n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]
check = [[False] * m for _ in range(n)]
k = [[-1] * m for _ in range(n)]
check[0][0] = True
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = 0
dfs(0, 0, 0)

print(result)