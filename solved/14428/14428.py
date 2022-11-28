import sys
from math import log, ceil
sys.stdin = open("input.txt")

input = sys.stdin.readline


def init(start, end, i=1):
    if start >= end:
        tree[i] = [nums[end], end]
        loc[end] = i
        return tree[i]

    mid = (start + end) // 2
    a = init(start, mid, i*2)
    b = init(mid+1, end, i*2+1)

    tree[i] = a if a[0] <= b[0] else b
    return tree[i]


def search(start, end, left, right, i=1):
    if start > right or end < left:
        return [2147483647, 0]

    if left <= start and end <= right:
        return tree[i]

    mid = (start + end) // 2
    a = search(start, mid, left, right, i*2)
    b = search(mid+1, end, left, right, i*2+1)

    return a if a[0] <= b[0] else b


n = int(input())
nums = list(map(int, input().split()))

size = pow(2, ceil(log(n, 2)+1))
tree = [[0, 0] for _ in range(size)]
loc = [0] * n

init(0, n-1)

m = int(input())

while m:
    m -= 1

    query, x, y = map(int, input().split())

    if query == 1:
        idx = loc[x-1]
        tree[idx] = [y, x-1]

        while idx > 0:
            idx //= 2
            tree[idx] = tree[idx*2] if tree[idx*2][0] <= tree[idx*2+1][0] else tree[idx*2+1]

    else:
        sys.stdout.write(str(search(0, n-1, x-1, y-1)[1]+1) + '\n')