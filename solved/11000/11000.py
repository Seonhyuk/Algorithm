import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

times.sort()
rooms = []

for t in times:
    if not rooms:
        heapq.heappush(rooms, t[1])
    else:
        if t[0] >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, t[1])

print(len(rooms))