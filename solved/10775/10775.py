import sys
# sys.stdin = open("test.txt")


def find(n):
    if n != port[n]:
        port[n] = find(port[n])
    return port[n]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    port[r2] = r1


g = int(input())
p = int(input())

port = [i for i in range(g+1)]

result = 0
for _ in range(p):
    n = int(sys.stdin.readline())
    if find(n) != 0:
        result += 1
        n = find(n)
        union(n-1, n)
    else:
        break

print(result)