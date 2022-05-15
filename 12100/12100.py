import sys
from copy import deepcopy
sys.stdin = open("input.txt")


def lean(i):
    global n
    check = [[False] * n for _ in range(n)]

    if i == 0:
        for t in range(1, n):
            for k in range(n):
                if matrix[t][k] != 0:
                    y = 0
                    while t + y - 1 >= 0:
                        if matrix[t+y-1][k] == 0:
                            y -= 1
                        elif matrix[t+y-1][k] == matrix[t][k] and not check[t+y-1][k]:
                            matrix[t+y-1][k] *= 2
                            matrix[t][k] = 0
                            check[t+y-1][k] = True
                            y = 0
                            break
                        else:
                            break
                    if y != 0:
                        matrix[t+y][k] = matrix[t][k]
                        matrix[t][k] = 0

    elif i == 1:
        for t in range(n-2, -1, -1):
            for k in range(n):
                if matrix[t][k] != 0:
                    y = 0
                    while t + y + 1 < n:
                        if matrix[t+y+1][k] == 0:
                            y += 1
                        elif matrix[t+y+1][k] == matrix[t][k] and not check[t+y+1][k]:
                            matrix[t+y+1][k] *= 2
                            matrix[t][k] = 0
                            check[t+y+1][k] = True
                            y = 0
                            break
                        else:
                            break
                    if y != 0:
                        matrix[t+y][k] = matrix[t][k]
                        matrix[t][k] = 0

    elif i == 2:
        for t in range(1, n):
            for k in range(n):
                if matrix[k][t] != 0:
                    y = 0
                    while t + y - 1 >= 0:
                        if matrix[k][t+y-1] == 0:
                            y -= 1
                        elif matrix[k][t+y-1] == matrix[k][t] and not check[k][t+y-1]:
                            matrix[k][t+y-1] *= 2
                            matrix[k][t] = 0
                            check[k][t+y-1] = True
                            y = 0
                            break
                        else:
                            break
                    if y != 0:
                        matrix[k][t+y] = matrix[k][t]
                        matrix[k][t] = 0

    else:
        for t in range(n-2, -1, -1):
            for k in range(n):
                if matrix[k][t] != 0:
                    y = 0
                    while t + y + 1 < n:
                        if matrix[k][t+y+1] == 0:
                            y += 1
                        elif matrix[k][t+y+1] == matrix[k][t] and not check[k][t+y+1]:
                            matrix[k][t+y+1] *= 2
                            matrix[k][t] = 0
                            check[k][t+y+1] = True
                            y = 0
                            break
                        else:
                            break
                    if y != 0:
                        matrix[k][t+y] = matrix[k][t]
                        matrix[k][t] = 0


def make_order(o, level=0):
    if level == 5:
        order.append(o[:])
    else:
        for i in range(4):
            o.append(i)
            make_order(o, level+1)
            o.pop()


n = int(input())
ori = [list(map(int, input().split())) for _ in range(n)]

max_num = max(sum(ori, []))

order = []
make_order([])
result = 0

for o in order:
    matrix = deepcopy(ori)
    for i in range(5):
        lean(o[i])

    result = max(result, max(sum(matrix, [])))

print(result)