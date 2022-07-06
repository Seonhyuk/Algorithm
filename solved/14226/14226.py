import sys
from collections import deque
sys.stdin = open("input.txt")

n = int(input())
arr = [1001] * 1001
arr[1] = 0
arr[2] = 2

q = deque()
q.append((2, 2, 1))

while q:
    k, cnt, clip = q.popleft()

    if 0 < k + clip <= 1000:
        if cnt + 1 < arr[k+clip]:
            arr[k+clip] = cnt + 1
            q.append((k - 1, cnt + 1, clip))
        q.append((k+clip, cnt+1, clip))

    if 0 < k + k <= 1000:
        if cnt + 2 < arr[k+k]:
            arr[k+k] = cnt + 2
            q.append((k - 1, cnt + 1, clip))
        q.append((k+k, cnt+2, k))

for i in range(999, 0, -1):
    arr[i] = min(arr[i+1]+1, arr[i])

print(arr[n])
