import sys
sys.stdin = open("input.txt")

n = int(input())
solutions = list(map(int, input().split()))

solutions.sort()

result = int(1e10)
answer = []

for i in range(n-2):
    start, end = i + 1, n - 1
    while start < end:
        total = solutions[i] + solutions[start] + solutions[end]
        if abs(total) < result:
            result = abs(total)
            answer = [solutions[i], solutions[start], solutions[end]]

        if total > 0:
            end -= 1
        elif total < 0:
            start += 1
        else:
            break

print(*answer)