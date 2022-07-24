import sys
import heapq
sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())
plus = []
zero = []
minus = []
result = 0

for _ in range(n):
    num = int(input())

    if num > 1:
        heapq.heappush(plus, -num)
    elif num == 1:
        result += 1
    elif num == 0:
        zero.append(0)
    else:
        heapq.heappush(minus, num)

while len(minus) > 1:
    x = heapq.heappop(minus)
    y = heapq.heappop(minus)

    result += x * y

if len(minus) == 1:
    if len(zero) > 0:
        zero.pop()
        minus.pop()
    else:
        x = minus.pop()
        result += x

while len(plus) > 1:
    x = heapq.heappop(plus)
    y = heapq.heappop(plus)

    result += x * y

if len(plus) == 1:
    x = plus.pop()
    result -= x

print(result)