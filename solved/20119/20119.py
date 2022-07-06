import sys
from collections import defaultdict, deque
# sys.stdin = open("input.txt")

n, m = map(int, input().split())
rec = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

in_order = [0] * m
what = [0] * m
recipe = defaultdict(list)

for i in range(m):
    what[i] = rec[i][-1]
    in_order[i] = rec[i][0]

    for j in range(1, rec[i][0]+1):
        recipe[rec[i][j]].append(i)

l = int(input())
has = deque(map(int, input().split()))

result = set()

while has:
    potion = has.popleft()
    if potion not in result:
        result.add(potion)

        for p in recipe[potion]:
            in_order[p] -= 1

            if in_order[p] == 0:
                has.append(what[p])

result = sorted(list(result))
print(len(result))
print(*result)