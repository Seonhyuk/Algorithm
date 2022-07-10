import sys
from collections import deque, defaultdict
sys.stdin = open("input.txt")

input = sys.stdin.readline


def level(root):
    q = deque()
    q.append(root)

    while q:
        x = q.popleft()

        for next in graph[x]:
            l[next] = l[x] + 1
            q.append(next)


t = int(input())
for _ in range(t):
    n = int(input())

    p = [0] * (n+1)
    l = [0] * (n+1)
    graph = defaultdict(list)

    for _ in range(n-1):
        a, b = map(int, input().split())
        p[b] = a
        graph[a].append(b)

    root = 0
    for i in range(1, n+1):
        if p[i] == 0:
            root = i

    level(root)

    n1, n2 = map(int, input().split())

    while n1 != n2:
        if l[n1] == l[n2]:
            n1 = p[n1]
            n2 = p[n2]
        elif l[n1] > l[n2]:
            n1 = p[n1]
        else:
            n2 = p[n2]

    print(n1)

