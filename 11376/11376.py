import sys
sys.stdin = open("input.txt")


def dfs(t):
    if visited[t]:
        return False
    visited[t] = True

    for work in possible[t]:
        if t != worked[work] and (not worked[work] or dfs(worked[work])):
            worked[work] = t
            return True

    return False


n, m = map(int, input().split())

possible = [[] for _ in range(n+1)]
worked = [0] * (m+1)

for i in range(1, 1+n):
    works = list(map(int, input().split()))
    for j in range(1, works[0]+1):
        possible[i].append(works[j])

for i in range(1, 1+n):
    visited = [False] * (n+1)
    dfs(i)
    visited = [False] * (n+1)
    dfs(i)

result = 0
for i in range(1, m+1):
    if worked[i]:
        result += 1

print(result)