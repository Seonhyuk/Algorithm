import sys


def dfs(k):
    if visited[k]:
        return False
    visited[k] = True

    for num in possible[k]:
        if not books[num] or dfs(books[num]):
            books[num] = k
            return True

    return False


T = int(input())
for tc in range(T):
    n, m = map(int, sys.stdin.readline().split())

    possible = [[] for _ in range(m+1)]
    books = [0] * (n+1)

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        for j in range(a, b+1):
            possible[i+1].append(j)

    for i in range(1, m+1):
        visited = [False] * (m+1)
        dfs(i)

    result = 0
    for i in range(1, n+1):
        if books[i]:
            result += 1

    print(result)