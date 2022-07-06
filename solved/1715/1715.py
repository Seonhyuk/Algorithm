import sys, heapq
# sys.stdin = open("input.txt")

n = int(input())
q = []
for i in range(n):
    n = int(input())
    heapq.heappush(q, n)

result = 0

while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a + b
    heapq.heappush(q, (a+b))

print(result)

