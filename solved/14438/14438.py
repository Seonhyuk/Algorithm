import sys
from math import ceil, log

sys.stdin = open("input.txt")

input = sys.stdin.readline


def init(start, end, i=1):
    if start >= end:
        tree[i] = nums[end]
        loc[end] = i
        return nums[end]

    mid = (start + end) // 2
    tree[i] = min(init(start, mid, i*2), init(mid+1, end, i*2+1))
    return tree[i]


def search(start, end, left, right, i=1):
    if right < start or left > end:
        return int(1e10)

    if left <= start and right >= end:
        return tree[i]

    mid = (start + end) // 2
    return min(search(start, mid, left, right, i*2), search(mid+1, end, left, right, i*2+1))


n = int(input())
nums = list(map(int, input().split()))
size = pow(2, ceil(log(n, 2)+1))
tree = [0] * size
loc = [0] * n

init(0, n-1)

m = int(input())

while m:
    m -= 1

    query, x, y = map(int, input().split())

    if query == 1:
        idx = loc[x-1]
        tree[idx] = y

        while idx > 0:
            idx //= 2
            tree[idx] = min(tree[idx*2], tree[idx*2+1])

    else:
        print(search(0, n-1, x-1, y-1))
