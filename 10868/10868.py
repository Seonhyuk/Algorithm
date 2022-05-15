import sys
from math import log, ceil

# sys.stdin = open("input.txt")


def segment(left, right, i=1):
    if left == right:
        tree[i] = nums[left]
        return tree[i]

    mid = (left + right) // 2
    x = segment(left, mid, i*2)
    y = segment(mid+1, right, i*2+1)
    tree[i] = min(x, y)
    return tree[i]


def search(start, end, left, right, i=1):
    if start > right or end < left:
        return 1000000001

    if start >= left and end <= right:
        return tree[i]

    mid = (start + end) // 2
    x = search(start, mid, left, right, i*2)
    y = search(mid+1, end, left, right, i*2+1)
    return min(x, y)


n, m = map(int, input().split())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

tree = [0] * 2 ** ceil(log(n, 2) + 1)
segment(0, n-1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(search(0, n-1, a-1, b-1))