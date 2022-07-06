import sys
sys.stdin = open("input.txt")


def dfs(k):
    if visited[k]:
        return False
    visited[k] = True

    for num in mine[k]:
        if not matched[num] or dfs(matched[num]):
            matched[num] = k
            return True

    return False


n, m = map(int, input().split())

mine = [[] for _ in range(n+1)]
matched = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    mine[a].append(b)

for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i)

result = 0
for i in range(1, n+1):
    if matched[i]:
        result += 1

print(result)