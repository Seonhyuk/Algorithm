import sys

sys.stdin = open("input.txt")

import bisect

n = int(input())
a = list(map(int, input().split()))
d = []
# result = []

for i in range(n):
    if not d or a[i] > d[-1]:
        d.append(a[i])
        # result.append((len(d)-1, a[i]))
    else:
        mid = bisect.bisect_left(d, a[i])
        d[mid] = a[i]
        # result.append((mid, a[i]))


# solution = []
# last = len(d)-1
# for i in range(len(result)-1, -1, -1):
#     if result[i][0] == last:
#         solution.append(result[i][1])
#         last -= 1

print(len(d))
# print(*reversed(solution))
