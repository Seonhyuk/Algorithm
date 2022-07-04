import sys
from math import log2, ceil

sys.stdin = open("input.txt")
input = sys.stdin.readline


def init(left, right, i=1):
    if left == right:
        matching[left] = i
        return 0

    mid = (left + right) // 2
    tree[i] = init(left, mid, i*2) + init(mid+1, right, i*2+1)
    return tree[i]


def search(left, right, start, end, i=1):
    if end < left or start > right:
        return 0

    if start <= left and right <= end:
        return tree[i]

    mid = (left + right) // 2
    return search(left, mid, start, end, i*2) + search(mid+1, right, start, end, i*2+1)


n, m = map(int, input().split())
tree = [0] * (2**(ceil(log2(n))+1))
matching = [0] * n
init(0, n-1)

for _ in range(m):
    method, start, end = map(int, input().split())

    if method == 0:
        if end < start:
            start, end = end, start

        print(search(0, n-1, start-1, end-1))
    else:
        idx = matching[start-1]
        tree[idx] = end

        while idx > 1:
            idx //= 2
            tree[idx] = tree[idx*2] + tree[idx*2+1]
