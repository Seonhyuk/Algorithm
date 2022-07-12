import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    last = list(map(int, input().split()))

    p = [0] * (n+1)
    p2 = [0] * (n+1)
    for i in range(n):
        p[last[i]] = i
        p2[last[i]] = i

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if p[a] > p[b]:
            p2[a] -= 1
            p2[b] += 1
        else:
            p2[a] += 1
            p2[b] -= 1

    rank = [0] * n
    for i in range(1, n+1):
        if rank[p2[i]]:
            print("IMPOSSIBLE")
            break
        else:
            rank[p2[i]] = i
    else:
        print(*rank)