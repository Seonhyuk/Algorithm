import sys
import heapq

sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())

min_q = []
max_q = []

k = int(input())
heapq.heappush(max_q, -k)
print(k)

if n >= 2:
    k = int(input())

    if k < -max_q[0]:
        t = -heapq.heappop(max_q)
        heapq.heappush(min_q, t)
        heapq.heappush(max_q, -k)
    else:
        heapq.heappush(min_q, k)

    print(-max_q[0])

    for i in range(n-2):
        k = int(input())

        if -max_q[0] <= k <= min_q[0]:
            if len(max_q) == len(min_q):
                heapq.heappush(max_q, -k)
            else:
                heapq.heappush(min_q, k)
        else:
            if len(max_q) == len(min_q):
                if k < -max_q[0]:
                    heapq.heappush(max_q, -k)
                else:
                    t = heapq.heappop(min_q)
                    heapq.heappush(max_q, -t)
                    heapq.heappush(min_q, k)
            else:
                if k > min_q[0]:
                    heapq.heappush(min_q, k)
                else:
                    t = -heapq.heappop(max_q)
                    heapq.heappush(min_q, t)
                    heapq.heappush(max_q, -k)

        print(-max_q[0])