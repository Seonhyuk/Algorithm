import sys

n = int(input())
t = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    t.append((s, e))

t.sort(key=lambda x: (x[1], x[0]))

start = 0
cnt = 0
for i in range(n):
    if t[i][0] >= start:
        cnt += 1
        start = t[i][1]

print(cnt)