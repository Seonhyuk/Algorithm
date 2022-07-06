import sys
from copy import deepcopy

sys.stdin = open("input.txt")


def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    parent[r2] = r1


n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0

while True:
    mx = deepcopy(matrix)
    parent = list(range(n * n))
    for i in range(n):
        for j in range(n):
            for k in range(4):
                di = i + d[k][0]
                dj = j + d[k][1]
                if 0 <= di < n and 0 <= dj < n and parent[i*n + j] != parent[di*n + dj]:
                    if l <= abs(matrix[i][j] - matrix[di][dj]) <= r:
                        union(i*n + j, di*n + dj)

    for i in range(n*n):
        find(i)

    check = {}
    for i in range(n*n):
        if parent[i] not in check:
            check[parent[i]] = [i]
        else:
            check[parent[i]].append(i)

    for key in check.keys():
        if len(check[key]) > 1:
            v = 0
            for value in check[key]:
                v += matrix[value // n][value % n]

            for value in check[key]:
                mx[value // n][value % n] = v // len(check[key])

    if mx == matrix:
        break
    else:
        result += 1
        matrix = mx

print(result)


