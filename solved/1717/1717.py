import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline


def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    parent[r2] = r1


n, m = map(int, input().split())

parent = list(range(n+1))

while m:
    m -= 1

    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
