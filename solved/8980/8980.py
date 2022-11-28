import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

commands = []

for _ in range(m):
    start, end, count = map(int, input().split())
    commands.append((end, start, count))

commands.sort()

boxes = [c] * (n+1)
result = 0

for end, start, count in commands:

    capacity = c
    for i in range(start, end):
        capacity = min(capacity, boxes[i])

    capacity = min(capacity, count)

    for i in range(start, end):
        boxes[i] -= capacity

    result += capacity

print(result)
