import sys
sys.stdin = open("input.txt")


def make_tree(n):
    global number, tree, idx
    if n <= number:
        make_tree(n*2)
        tree[n] = values[idx]
        idx += 1
        make_tree(n*2 + 1)


level = int(input())
values = list(map(int, input().split()))
idx = 0

number = 2**(level) - 1

tree = [0] + [0] * number

make_tree(1)

k = 1
last = 2
while last <= number+1:
    print(*tree[k:last])
    k = last
    last *= 2
