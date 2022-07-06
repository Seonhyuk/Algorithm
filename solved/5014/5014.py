import sys
sys.stdin = open("input.txt")

from collections import deque

f, s, g, u, d = map(int, input().split())

floors = [0] * (f + 1)
visited = [False] * (f + 1)

q = deque()
q.append((s, 0))
visited[s] = True

while q:
    start, cnt = q.popleft()
    for i in [u, -d]:
        new = start + i
        if 0 < new <= f and not visited[new]:
            floors[new] = cnt + 1
            visited[new] = True
            q.append((new, cnt + 1))

if visited[g]:
    print(floors[g])
else:
    print('use the stairs')

