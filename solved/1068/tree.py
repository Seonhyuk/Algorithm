import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n = int(input())
    nodes = list(map(int, input().split()))

    tree = {}
    for i in range(-1, n):
        tree[i] = []

    for j in range(n):
        tree[nodes[j]].append(j)

    denode = int(input())

    for key in tree.keys():
        if denode in tree[key]:
            tree[key].remove(denode)

    que = [-1]
    cnt = 0

    while que:
        node = que.pop(0)
        if tree[node]:
            for v in tree[node]:
                que.append(v)
        else:
            cnt += 1

    if len(tree[-1]) == 0:
        cnt = 0

    print(cnt)