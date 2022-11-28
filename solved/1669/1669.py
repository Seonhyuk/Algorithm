import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

n, m = map(int, input().split())
length = m - n

value = int(((-1) + (1 + 4 * length) ** (1 / 2)) / 2)
remainder = length - value * (value + 1)

operations = 2 * value

if 0 < remainder <= value + 1:
    operations += 1
elif remainder > value + 1:
    operations += 2

print(operations)
