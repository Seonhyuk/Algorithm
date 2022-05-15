import sys
from collections import defaultdict
sys.setrecursionlimit(10000)


def dp(w):
    if dist[w] != inf:
        return dist[w]
    else:
        part = []
        for i in range(len(must[w])):
            part.append(dp(must[w][i]))
        dist[w] = max(part) + times[w]
        return dist[w]


T = int(input())
for tc in range(1, 1+T):
    n, k = map(int, input().split())

    inf = 1e09
    times = [0] + list(map(int, input().split()))
    dist = [inf] * (n+1)

    must = defaultdict(list)
    sub = set()
    for _ in range(k):
        pre, post = map(int, sys.stdin.readline().split())
        must[post].append(pre)
        sub.add(post)

    for i in range(1, n+1):
        if i not in sub:
            dist[i] = times[i]

    w = int(input())
    dp(w)
    print(dist[w])