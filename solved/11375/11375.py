import sys
sys.stdin = open("input.txt")


def search(x):
    if worked[x]:
        return False
    worked[x] = True

    for work in emps[x]:
        if not works[work] or search(works[work]):
            works[work] = x
            return True

    return False


n, m = map(int, input().split())

emps = [[] for _ in range(n+1)]
works = [0] * (m+1)

for i in range(1, n+1):
    possible = list(map(int, input().split()))
    for j in range(1, possible[0]+1):
        emps[i].append(possible[j])

for i in range(1, n+1):
    worked = [False] * (n+1)
    search(i)

result = 0
for i in range(1, m+1):
    if works[i]:
        result += 1

print(result)