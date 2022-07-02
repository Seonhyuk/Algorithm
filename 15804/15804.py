import sys
from collections import deque
sys.stdin = open("input.txt")

n, m = map(int, input().split())

stop = [-1] * n
buses = deque([tuple(map(int, input().split())) for _ in range(m)])

t = 0
while True:
    for i in range(n):
        if stop[i] > 0:
            stop[i] -= 1

    for i in range(n-1, -1, -1):
        if stop[i] == 0:
            for j in range(i+1, n):
                if stop[j] >= 0:
                    break
            else:
                stop[i] = -1

    a = False
    while buses and buses[0][0] <= t:
        a = False
        if stop[0] == -1:
            s, e = buses.popleft()

            for j in range(n):
                if stop[j] >= 0:
                    stop[j-1] = e
                    a = True
                    break
            else:
                stop[n-1] = e
        else:
            break

    t += 1

    if not buses and a:
        print(n-j+1)
        break

    elif not buses and not a:
        print(n-j)
        break




