import sys
# sys.stdin = open("input.txt")

import bisect

n = int(input())
eline = []
for _ in range(n):
    line = tuple(map(int, sys.stdin.readline().split()))
    eline.append(line)

eline.sort()

d = []
q = []

for i in range(n):
    if not d or eline[i][1] > d[-1]:
        d.append(eline[i][1])
        q.append((len(d)-1, eline[i]))

    else:
        mid = bisect.bisect_left(d, eline[i][1])
        d[mid] = eline[i][1]
        q.append((mid, eline[i]))


solution = []
last = len(d)-1
for i in range(len(q)-1, -1, -1):
    if q[i][0] == last:
        last -= 1
    else:
        solution.append(q[i][1][0])

print(len(solution))
print(*reversed(solution))