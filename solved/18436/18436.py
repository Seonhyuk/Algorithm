import sys
from math import log, ceil
sys.stdin = open("input.txt")

input = sys.stdin.readline


def init(start, end, i=1):
    if start >= end:
        tree[i] = nums[end] % 2
        loc[end] = i
        return tree[i] % 2

    mid = (start + end) // 2
    tree[i] = init(start, mid, i*2) + init(mid+1, end, i*2+1)
    return tree[i]


def search(start, end, left, right, i=1):
    if start > right or end < left:
        return 0
    if start >= left and right >= end:
        return tree[i]

    mid = (start + end) // 2
    return search(start, mid, left, right, i*2) + search(mid+1, end, left, right, i*2+1)


n = int(input())
nums = list(map(int, input().split()))
loc = [0] * n
tree = [0] * pow(2, ceil(log(n, 2)+1))

init(0, n-1)

m = int(input())
while m:
    m -= 1
    query, x, y = map(int, input().split())

    if query == 1:
        idx = loc[x-1]
        tree[idx] = y % 2

        while idx > 0:
            idx //= 2
            tree[idx] = tree[idx*2] + tree[idx*2+1]

    elif query == 2:
        print(y-x+1-search(0, n-1, x-1, y-1))

    else:
        print(search(0, n-1, x-1, y-1))
