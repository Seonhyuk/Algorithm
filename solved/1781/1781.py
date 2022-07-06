import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    d, c = map(int, input().split())
    q.append((-c, d))

q.sort()
solved = [-1] * (n+1)
result = 0

for i in range(n):
    d = q[i][1]
    while d > 0:
        if solved[d] >= 0:
            d = solved[d]
        else:
            solved[d] = d - 1
            solved[q[i][1]] = d - 1
            result += -q[i][0]
            break

print(result)