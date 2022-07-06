import sys
sys.stdin = open("input.txt")


def multiply(m1, m2):
    result = []
    for i in range(2):
        sub = []
        for j in range(2):
            cnt = 0
            for k in range(2):
                cnt += m1[i][k] * m2[k][j]
            sub.append(cnt % 1000000000)
        result.append(sub)

    return result


def power(exponent):
    if exponent == 1:
        return [[1, 1], [1, 0]]

    else:
        value = power(exponent//2)
        if exponent % 2:
            return multiply(multiply(value, value), power(1))
        else:
            return multiply(value, value)


a, b = map(int, input().split())

if a-1 <= 2:
    front = a-1
else:
    result = power(a-1)
    front = result[0][0] + result[0][1] - 1

if b <= 2:
    back = b
else:
    result = power(b)
    back = result[0][0] + result[0][1] - 1

print((back - front) % 1000000000)