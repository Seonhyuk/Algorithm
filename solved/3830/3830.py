import sys
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt")


def find(n):
    if n != rep[n]:
        tmp = find(rep[n])
        diff[n] += diff[rep[n]]
        rep[n] = tmp
    return rep[n]


def union(n1, n2, k):
    r1 = rep[n1]
    r2 = rep[n2]
    if r1 != r2:
        rep[r2] = r1
        diff[r2] = diff[n1] + k - diff[n2]


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    rep = list(range(n+1))
    diff = [0] * (n+1)

    for _ in range(m):
        work = sys.stdin.readline().split()
        for i in range(1, len(work)):
            work[i] = int(work[i])

        find(work[1])
        find(work[2])

        if work[0] == '!':
            union(work[1], work[2], work[3])
        else:
            if rep[work[1]] == rep[work[2]]:
                print(diff[work[2]] - diff[work[1]])
            else:
                print("UNKNOWN")