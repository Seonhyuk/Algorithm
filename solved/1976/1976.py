import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline


def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    parent[r2] = r1


n = int(input())
m = int(input())
parent = list(range(n+1))

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] and find(i+1) != find(j+1):
            union(i+1, j+1)

route = list(map(int, input().split()))

answer = "YES"

for i in range(m-1):
    if find(route[i]) != find(route[i+1]):
        answer = "NO"
        break

print(answer)
