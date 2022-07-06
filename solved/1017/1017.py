import sys
sys.stdin = open("input.txt")


def dfs(k):
    global num
    if visited[k]:
        return False
    visited[k] = True

    for p in match[k]:
        if p != num and p != 0:
            if not what[p] or dfs(what[p]):
                what[p] = k
                visited[p] = True
                return True

    return False


n = int(input())
nums = list(map(int, input().split()))

primes = [False, False] + [True] * 1999
for i in range(2, 2001):
    if primes[i]:
        for j in range(2*i, 2001, i):
            primes[j] = False

match = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j and primes[nums[i]+nums[j]]:
            match[i].append(j)

result = []

for num in match[0]:
    what = [0] * n
    what[0] = num
    what[num] = 0
    for i in range(n):
        visited = [False] * n
        visited[0] = True
        visited[num] = True

        dfs(i)

    verification = [0] * n
    for i in range(n):
        verification[what[i]] += 1
        if verification[what[i]] >= 2:
            break
    else:
        result.append(nums[num])

if not result:
    result.append(-1)

result.sort()
print(*result)
