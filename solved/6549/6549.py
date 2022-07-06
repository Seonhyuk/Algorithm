import sys
sys.stdin = open("input.txt")

from collections import deque

while True:
    histogram = deque(map(int, input().split()))
    n = histogram.popleft()
    if not n:
        break

    stack = deque()
    result = 0

    for i in range(len(histogram)):
        while stack and histogram[stack[-1]] > histogram[i]:
            a = stack.pop()
            if stack:
                solution = (i - stack[-1] - 1) * histogram[a]
            else:
                solution = i * histogram[a]
            result = max(result, solution)

        stack.append(i)

    while stack:
        a = stack.pop()
        if stack:
            solution = (len(histogram) - stack[-1] - 1) * histogram[a]
        else:
            solution = histogram[a] * len(histogram)
        result = max(result, solution)

    print(result)
