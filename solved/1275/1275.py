import sys
from math import log, ceil

sys.stdin = open("input.txt")


def segment(left, right, i=1):
    if left == right:
        tree[i] = nums[left]
        location[left] = i
        return tree[i]
    mid = (left + right) // 2
    tree[i] = segment(left, mid, i*2) + segment(mid+1, right, i*2+1)
    return tree[i]


def search(start, end, left, right, i=1):
    if start > right or end < left:
        return 0

    if start >= left and end <= right:
        return tree[i]

    mid = (start + end) // 2
    return search(start, mid, left, right, i*2) + search(mid+1, end, left, right, i*2+1)


n, q = map(int, input().split())
nums = list(map(int, input().split()))
tree = [0] * 2 ** ceil(log(n, 2) + 1)
location = [0] * n

segment(0, n-1)

for _ in range(q):
    x, y, a, b = map(int, sys.stdin.readline().split())

    if x > y:
        x, y = y, x

    print(search(0, n-1, x-1, y-1))

    idx = location[a-1]
    tree[idx] = b
    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx*2] + tree[idx*2+1]
