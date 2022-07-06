import sys
sys.stdin = open("input.txt")

a, b = map(int, input().split())
m = int(input())

check = False
for _ in range(m):
    x, y = map(int, input().split())
    if x % 2 and y % 2:
        check = True

if a % 2 and b % 2 and check:
    result = (a + b) // 2
elif a % 2 and b % 2:
    result = (a-1 + b-1) // 2
else:
    result = (a + b) // 2

print(result)