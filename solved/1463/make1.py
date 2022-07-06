import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n = int(input())

    result = [0, 0]
    for i in range(2, n+1):
        if i % 3 == 0 and i % 2 == 0:
            result.append(min(result[i//3], result[i//2], result[-1]) + 1)
        elif i % 3 == 0:
            result.append(min(result[i//3], result[-1]) + 1)
        elif i % 2 == 0:
            result.append(min(result[-1], result[i//2]) + 1)
        else:
            result.append(result[-1] + 1)

    print(result[-1])