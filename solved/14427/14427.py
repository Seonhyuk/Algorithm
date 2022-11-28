import sys
from math import ceil, log
sys.stdin = open("input.txt")

input = sys.stdin.readline


def init(start, end, i=1):
    if start >= end:
        tree[i] = nums[end]
        idx_tree[i] = end
        loc[end] = i
        return tree[i]

    mid = (start + end) // 2
    a = init(start, mid, i*2)
    b = init(mid+1, end, i*2+1)
    if a <= b:
        tree[i] = a
        idx_tree[i] = idx_tree[i*2]
    else:
        tree[i] = b
        idx_tree[i] = idx_tree[i*2+1]
    return tree[i]


n = int(input())
nums = list(map(int, input().split()))
tree = [0] * 2 ** ceil(log(n, 2) + 1)
idx_tree = [0] * 2 ** ceil(log(n, 2) + 1)
loc = [0] * n

init(0, n-1)

m = int(input())

while m:
    m -= 1
    query = list(map(int, input().split()))

    if query[0] == 1:
        x, y = query[1]-1, query[2]
        tree[loc[x]] = y
        idx = loc[x]

        while idx:
            idx //= 2
            left, right = tree[idx*2], tree[idx*2+1]
            if left <= right:
                tree[idx] = left
                idx_tree[idx] = idx_tree[idx*2]
            else:
                tree[idx] = right
                idx_tree[idx] = idx_tree[idx*2+1]

    else:
        print(idx_tree[1]+1)

