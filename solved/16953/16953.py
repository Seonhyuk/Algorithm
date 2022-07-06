import sys
sys.stdin = open("input.txt")

a, b = map(int, input().split())

result = 0
while a < b:
    if b % 10 == 1:
        result += 1
        b //= 10
    else:
        if b % 2:
            result = -2
            break
        else:
            b //= 2
            result += 1

    if a == b:
        break
    elif a > b:
        result = -2
        break

print(result+1)