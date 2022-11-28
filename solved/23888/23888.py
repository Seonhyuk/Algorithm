import sys, math
sys.stdin = open("input.txt")

input = sys.stdin.readline


def sum_i(i):
    return d * (i * (i + 1)) // 2 + i * (a - d)


a, d = map(int, input().split())
q = int(input())
while q:
    q -= 1
    m, l, r = map(int, input().split())

    if m == 1:
        print(sum_i(r) - sum_i(l-1))
    else:
        if r - l == 0:
            print(a-d + d*l)
        else:
            print(math.gcd(a, d))
