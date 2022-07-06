import sys

r, c, m = map(int, sys.stdin.readline().split())

sharks = []
for _ in range(m):
    shark = list(map(int, input().split()))
    shark[0] -= 1
    shark[1] -= 1
    sharks.append(shark)

matrix = [[0 for _ in range(c)] for _ in range(r)]
result = 0

for fi in range(c):
    for shark in sharks:
        if matrix[shark[0]][shark[1]] == 0:
            matrix[shark[0]][shark[1]] = [shark[2], shark[3], shark[4]]
        else:
            if matrix[shark[0]][shark[1]][2] < shark[4]:
                matrix[shark[0]][shark[1]] = [shark[2], shark[3], shark[4]]

    for i in range(r):
        if matrix[i][fi] != 0:
            result += matrix[i][fi][2]
            matrix[i][fi] = 0
            break

    sharks = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j]:
                sharks.append([i, j, matrix[i][j][0], matrix[i][j][1], matrix[i][j][2]])
                matrix[i][j] = 0

    for t in range(len(sharks)):
        if sharks[t][3] == 1:
            sharks[t][0] -= sharks[t][2]
        elif sharks[t][3] == 2:
            sharks[t][0] += sharks[t][2]
        elif sharks[t][3] == 3:
            sharks[t][1] += sharks[t][2]
        else:
            sharks[t][1] -= sharks[t][2]

        while sharks[t][0] < 0 or sharks[t][0] >= r:
            if sharks[t][0] < 0:
                sharks[t][0] = abs(sharks[t][0])
                sharks[t][3] = 2
            if sharks[t][0] >= r:
                sharks[t][0] = (r-1) * 2 - sharks[t][0]
                sharks[t][3] = 1

        while sharks[t][1] < 0 or sharks[t][1] >= c:
            if sharks[t][1] < 0:
                sharks[t][1] = abs(sharks[t][1])
                sharks[t][3] = 3
            if sharks[t][1] >= c:
                sharks[t][1] = (c-1) * 2 - sharks[t][1]
                sharks[t][3] = 4

print(result)