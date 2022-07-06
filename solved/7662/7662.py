import sys
import heapq

# sys.stdin = open("test.txt")

T = int(input())
for tc in range(T):
    k = int(input())
    min_q = []
    max_q = []
    visited = [False] * k

    for i in range(k):
        m, n = sys.stdin.readline().split()
        n = int(n)
        if m == 'I':
            heapq.heappush(min_q, (n, i))
            heapq.heappush(max_q, (-n, i))
            visited[i] = True

        else:
            if n == -1:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(i)

            elif n == 1 and max_q:
                a = heapq.heappop(max_q)
                while max_q and not visited[a[1]]:
                    a = heapq.heappop(min_q)
                visited[a[1]] = False

    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    print(f'{-max_q[0][0]} {min_q[0][0]}' if max_q and min_q else 'EMPTY')