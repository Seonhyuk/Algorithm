import sys
sys.stdin = open("input.txt")


def dfs(y=0, x=0, cnt=1):
    global result, n, m

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(4):
        dy = y + d[i][0]
        dx = x + d[i][1]
        if 0 <= dy < n and 0 <= dx < m:
            if not visited[matrix[dy][dx]]:
                visited[matrix[dy][dx]] = 1
                dfs(dy, dx, cnt+1)
                visited[matrix[dy][dx]] = 0
    else:
        if cnt > result:
            result = cnt


n, m = map(int, input().split())
matrix = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]
visited = [0] * 26

result = 0
visited[matrix[0][0]] = 1

dfs()

print(result)