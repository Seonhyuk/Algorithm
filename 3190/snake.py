from collections import deque

N = int(input())
matrix = [[0] * N for _ in range(N)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 2

directions = []
l = int(input())
for _ in range(l):
    a = input().split()
    directions.append([int(a[0]), a[1]])

time = 0
x = 0
y = 0
stack = deque([(0, 0)])

direct = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    if directions and time == directions[0][0]:
        if directions[0][1] == 'D':
            direct += 1
        else:
            direct -= 1
        directions.pop(0)
        if direct < 0:
            direct += 4
        elif direct >= 4:
            direct %= 4

    x += dx[direct]
    y += dy[direct]
    time += 1
    if 0 <= x < N and 0 <= y < N and matrix[y][x] != 1:
        a = stack.popleft()
        matrix[a[1]][a[0]] = 0
        if matrix[y][x] == 2:
            stack.appendleft(a)
            matrix[a[1]][a[0]] = 1
        matrix[y][x] = 1
        stack.append((x, y))
    else:
        break

print(time)