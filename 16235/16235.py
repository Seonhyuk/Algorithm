import sys
sys.stdin = open("input.txt")
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix = [[5] * n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    y, x, age = map(int, input().split())
    tree[y-1][x-1].append(age)

died = deque()
during = deque()
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                length = len(tree[i][j])
                for _ in range(length):
                    level = tree[i][j].pop()
                    if level <= matrix[i][j]:
                        matrix[i][j] -= level
                        level += 1
                        tree[i][j].appendleft(level)
                    else:
                        died.append([i, j, level])

    while died:
        y, x, level = died.pop()
        matrix[y][x] += level // 2

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for t in range(len(tree[i][j])):
                    if tree[i][j][t] % 5 == 0:
                        for q in range(8):
                            dy = i + d[q][0]
                            dx = j + d[q][1]
                            if 0 <= dy < n and 0 <= dx < n:
                                during.append([dy, dx])

    while during:
        du = during.popleft()
        tree[du[0]][du[1]].append(1)

    for i in range(n):
        for j in range(n):
            matrix[i][j] += a[i][j]

result = 0
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            result += len(tree[i][j])

print(result)