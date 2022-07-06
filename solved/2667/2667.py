import sys
sys.stdin = open("input.txt")

from collections import deque

n = int(input())
matrix = [list(map(int, list(input()))) for _ in range(n)]
check = [[0] * n for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cnt = 0
result = []

for i in range(n):
    for j in range(n):
        if not check[i][j] and matrix[i][j] == 1:
            cnt += 1
            sub = 1
            check[i][j] = cnt
            q = deque()
            q.append((i, j))

            while q:
                y, x = q.popleft()
                for t in range(4):
                    dy = y + d[t][0]
                    dx = x + d[t][1]
                    if 0 <= dy < n and 0 <= dx < n:
                        if matrix[dy][dx] and not check[dy][dx]:
                            sub += 1
                            q.append((dy, dx))
                            check[dy][dx] = cnt

            result.append(sub)


print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])