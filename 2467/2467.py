import sys
sys.stdin = open("input.txt")

n = int(input())
lst = list(map(int, input().split()))

result = 1e10
result2 = []
for i in range(n-1):
    start = i + 1
    end = \
        n - 1
    mid = (start + end) // 2
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == -lst[i]:
            break
        else:
            if lst[mid] > -lst[i]:
                end = mid - 1
            else:
                start = mid + 1

    if abs(lst[i] + lst[mid]) < result:
        result = abs(lst[i] + lst[mid])
        result2 = [lst[i], lst[mid]]

    if i < mid < n-1:
        if abs(lst[i] + lst[mid+1]) < result:
            result = abs(lst[i] + lst[mid+1])
            result2 = [lst[i], lst[mid+1]]

    if i + 1 < mid < n:
        if abs(lst[i] + lst[mid-1]) < result:
            result = abs(lst[i] + lst[mid-1])
            result2 = [lst[i], lst[mid-1]]

print(*result2)