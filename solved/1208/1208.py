import sys
from itertools import combinations
import bisect
sys.stdin = open("input.txt")

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left = nums[:n//2]
right = nums[n//2:]

a, b = len(left), len(right)
left_sum = []
right_sum = []

for i in range(1, a+1):
    lst = list(combinations(left, i))
    for j in range(len(lst)):
        left_sum.append(sum(lst[j]))

for i in range(1, b+1):
    lst = list(combinations(right, i))
    for j in range(len(lst)):
        right_sum.append(sum(lst[j]))

left_sum.sort()
right_sum.sort()

result = 0
for num in left_sum:
    result += bisect.bisect_right(right_sum, s-num) - bisect.bisect_left(right_sum, s-num)

result += bisect.bisect_right(left_sum, s) - bisect.bisect_left(left_sum, s)
result += bisect.bisect_right(right_sum, s) - bisect.bisect_left(right_sum, s)

print(result)