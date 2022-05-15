import sys
import heapq
from collections import defaultdict

sys.stdin = open("input.txt")

n = int(input())
m = int(input())

buses = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    buses[s].append((w, e))

s, e = map(int, input().split())

q = []
heapq.heappush(q, (0, s))

inf = 1e09
distance = [[inf, []] for _ in range(n+1)]
distance[s][0] = 0
distance[s][1] = [s]

while q:
    dist, node = heapq.heappop(q)
    if distance[node][0] >= dist:
        for next in buses[node]:
            cost = distance[node][0] + next[0]
            if cost <= distance[next[1]][0]:
                distance[next[1]][0] = cost
                distance[next[1]][1] = distance[node][1] + [next[1]]
                heapq.heappush(q, (cost, next[1]))

print(distance[e][0])
print(len(distance[e][1]))
print(*distance[e][1])