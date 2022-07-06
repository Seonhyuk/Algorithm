from collections import deque
from math import ceil


def backtrack(level=0):
    global n, numbers, operators, min_result, max_result, result
    if level == n-1:
        if max_result is None:
            max_result = result
        if min_result is None:
            min_result = result
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
        return

    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            a = numbers.popleft()
            result2 = result
            if i == 0:
                result += a
            elif i == 1:
                result -= a
            elif i == 2:
                result *= a
            else:
                if result >= 0:
                    result //= a
                else:
                    result /= a
                    result = ceil(result)
            backtrack(level+1)
            result = result2
            numbers.appendleft(a)
            operators[i] += 1


n = int(input())
numbers = deque(map(int, input().split()))
operators = list(map(int, input().split()))

result = numbers.popleft()
max_result, min_result = None, None
backtrack()

print(max_result)
print(min_result)