import sys
sys.stdin = open("input.txt")


def bimatch(N):
    if visited[N]:
        return False
    visited[N] = True

    for num in cows[N]:
        if not sheds[num] or bimatch(sheds[num]):
            sheds[num] = N
            return True

    return False


n, m = map(int, input().split())

cows = [[] for _ in range(n+1)]
sheds = [0] * (m+1)

for i in range(1, n+1):
    info = list(map(int, input().split()))
    for j in range(1, info[0]+1):
        cows[i].append(info[j])

for i in range(1, n+1):
    visited = [False] * (n+1)
    bimatch(i)

result = 0
for i in range(1, m+1):
    if sheds[i]:
        result += 1

print(result)