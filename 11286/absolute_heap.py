import heapq

n = int(input())

heap = []
for _ in range(n):
    x = int(input())

    if not x:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))