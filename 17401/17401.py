import sys
sys.stdin = open("input.txt")


# 행렬 곱하는 함수
def product(matrix1, matrix2):
    global n

    result = []
    for i in range(n):
        sub = []
        for j in range(n):
            cnt = 0
            for k in range(n):
                cnt += matrix1[i][k] * matrix2[k][j]
            sub.append(cnt % 1000000007)
        result.append(sub)

    return result


# N제곱 분할정복
def power(matrix, N):
    global n
    if N == 0:
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return m

    if N == 1:
        return matrix
    else:
        new_matrix = power(matrix, N // 2)
        if N % 2:
            return product(product(new_matrix, new_matrix), matrix)
        else:
            return product(new_matrix, new_matrix)


t, n, d = map(int, input().split())

time_tunnel = []

for _ in range(t):
    tunnel = int(input())
    matrix = [[0] * n for _ in range(n)]
    for _ in range(tunnel):
        a, b, c = map(int, input().split())
        matrix[a-1][b-1] = c

    time_tunnel.append(matrix)

# 1회 주기당 계산을 위한 단위 행렬 생성
solution = [[0] * n for _ in range(n)]
for i in range(n):
    solution[i][i] = 1

# 만든 단위행렬에 주기에 있는 모든 통로의 수를 곱해줌
for i in range(t):
    solution = product(solution, time_tunnel[i])

# d를 t로 나눈 몫 만큼 solution이 반복됨
result = power(solution, d // t)

# d를 t로 나눈 나머지만큼을 time_tunnel에 순서대로 곱해줌
for i in range(d%t):
    result = product(result, time_tunnel[i])

for i in range(n):
    print(*result[i])