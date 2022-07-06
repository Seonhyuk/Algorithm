import sys
sys.stdin = open("input.txt")


def product(matrix1 ,matrix2):
    result = []
    for i in range(8):
        sub = []
        for j in range(8):
            cnt = 0
            for k in range(8):
                cnt += matrix1[i][k] * matrix2[k][j]
            sub.append(cnt % 1000000007)
        result.append(sub)
    return result


def power(matrix, n):
    if n == 1:
        return matrix
    else:
        new_matrix = power(matrix, n//2)
        if n % 2:
            return product(product(new_matrix, new_matrix), matrix)
        else:
            return product(new_matrix, new_matrix)


n = int(input())
direction = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

solution = power(direction, n)
print(solution[0][0])