import sys
sys.stdin = open("input.txt")

from collections import deque

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = []

for i in range(n):
    check = [False] * n
    q = deque()
    q.append(i)

    while q:
        node = q.popleft()
        for j in range(n):
            if matrix[node][j] == 1 and not check[j]:
                check[j] = True
                q.append(j)

    sub = []
    for j in range(n):
        if check[j]:
            sub.append(1)
        else:
            sub.append(0)

    result.append(sub[:])

for i in range(n):
    print(*result[i])