import sys
sys.stdin = open("input.txt")


def multiply(matrix1, matrix2):
    new_matrix = []
    for i in range(2):
        sub = []
        for j in range(2):
            cnt = 0
            for k in range(2):
                cnt += matrix1[i][k] * matrix2[k][j]
            if cnt >= 0:
                sub.append(cnt % 1000000007)
            else:
                sub.append(cnt)
        new_matrix.append(sub)
    return new_matrix


def power(exponent):
    if exponent == 1:
        return [[4, -1], [1, 0]]
    else:
        new_exponent = exponent // 2
        value = power(new_exponent)
        if exponent % 2:
            return multiply(multiply(value, value), power(1))
        else:
            return multiply(value, value)


n = int(input())

if n % 2:
    print(0)
else:
    result = power(n // 2)
    print((result[0][0] + result[0][1]) % 1000000007)