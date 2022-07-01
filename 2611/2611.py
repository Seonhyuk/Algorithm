import sys
from collections import deque, defaultdict

sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
route = [0 for _ in range(n+1)]
graph = defaultdict(list)

check = [False] * (n+1)
check[1] = True

edges = [0] * (n + 1)

m = int(input())
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((s, e, w))
    edges[e] += 1

q = deque(graph[1])

while q:
    s, e, w = q.popleft()

    if dp[e] < dp[s] + w:
        dp[e] = dp[s] + w
        route[e] = s

    edges[e] -= 1
    if edges[e] == 0 and not check[e]:
        check[e] = True

        q.extend(graph[e])

p = [1]
result = [1]
while True:
    x = p.pop()
    if route[x] == 0:
        break

    result.append(route[x])
    p.append(route[x])

    if route[x] == 1:
        break

result.reverse()

print(dp[1])
print(*result)
