import sys
sys.stdin = open("input.txt")

from bisect import bisect_left


def find(n):
    if rep[n] != n:
        rep[n] = find(rep[n])
    return rep[n]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    rep[r2] = r1


n, m, k = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

rep = [i for i in range(m+1)]

cs = list(map(int, input().split()))

for card in cs:
    t = bisect_left(cards, card+1)
    print(cards[find(t)])
    union(find(t)+1, find(t))