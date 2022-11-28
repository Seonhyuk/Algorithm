import sys
sys.stdin = open("input.txt")

input = __import__("sys").stdin.readline

n = int(input())
total = 0
xor = 0

for _ in range(n):
    a = list(map(int, input().split()))

    if len(a) == 1:
        if a[0] == 3:
            print(total)
        else:
            print(xor)

    else:
        if a[0] == 1:
            total += a[1]
            xor ^= a[1]
        else:
            total -= a[1]
            xor ^= a[1]