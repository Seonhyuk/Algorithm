import sys, heapq
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())

jems = []
bags = []

result = 0
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jems, (m, v))

for _ in range(k):
    bags.append(int(input()))

bags.sort()

tmp = []
for bag in bags:
    while jems and jems[0][0] <= bag:
        heapq.heappush(tmp, -heapq.heappop(jems)[1])

    if tmp:
        result -= heapq.heappop(tmp)

print(result)