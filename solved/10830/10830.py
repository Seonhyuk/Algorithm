def multiply(matrix1, matrix2):
    global n
    result = []
    for i in range(n):
        result2 = []
        for j in range(n):
            value = 0
            for t in range(n):
                value += matrix1[i][t] * matrix2[t][j]
            result2.append(value % 1000)
        result.append(result2)
    return result


def power(matrix, exponent):
    if exponent <= 1:
        return matrix
    else:
        if exponent % 2 == 0:
            new_exponent = power(matrix, exponent // 2)
            return multiply(new_exponent, new_exponent)
        else:
            new_exponent = power(matrix, exponent // 2)
            return multiply(multiply(new_exponent, new_exponent), matrix)


n, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

if k == 1:
    for i in range(n):
        for j in range(n):
            mat[i][j] = mat[i][j] % 1000
    z = mat
else:
    z = power(mat, k)

for x in range(n):
    print(*z[x])