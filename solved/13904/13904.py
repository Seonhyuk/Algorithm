import sys
import heapq

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(arr, (-w, d))

result = [0] * 1001

for _ in range(n):
    w, d = heapq.heappop(arr)
    if not result[d]:
        result[d] = -w
    else:
        while d > 1:
            d -= 1
            if not result[d]:
                result[d] = -w
                break

print(sum(result))