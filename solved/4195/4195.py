import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline


def find(name):
    if name != p[name]:
        p[name] = find(p[name])
    return p[name]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)

    if r1 != r2:
        p[r2] = r1
        friends[r1] += friends[r2]


t = int(input())
for _ in range(t):
    f = int(input())

    p = dict()
    friends = dict()

    for _ in range(f):
        name1, name2 = input().split()

        if name1 not in p:
            p[name1] = name1
            friends[name1] = 1
        if name2 not in p:
            p[name2] = name2
            friends[name2] = 1

        union(name1, name2)

        print(friends[find(name1)])