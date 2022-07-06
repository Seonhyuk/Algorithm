import sys
sys.stdin = open("input.txt")

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

total = num_list[0]
i, j = 0, 1
inf = int(1e09)
result = inf

while j < n:
    if total < s:n, s = map(int, input().split())
num_list = list(map(int, input().split()))

total = num_list[0]
i, j = 0, 1
inf = int(1e09)
result = inf

while j < n:
    if total < s:
        total += num_list[j]
        j += 1
    else:
        while total - num_list[i] >= s:
            total -= num_list[i]
            i += 1
        result = min(result, j - i)

        total += num_list[j]
        j += 1

while total - num_list[i] >= s:
    total -= num_list[i]
    i += 1

if total >= s:
    result = min(result, j - i)

if result == inf:
    result = 0

print(result)
        total += num_list[j]
        j += 1
    else:
        while total - num_list[i] >= s:
            total -= num_list[i]
            i += 1
        result = min(result, j - i)

        total += num_list[j]
        j += 1

while total - num_list[i] >= s:
    total -= num_list[i]
    i += 1

if total >= s:
    result = min(result, j - i)

if result == inf:
    result = 0

print(result)