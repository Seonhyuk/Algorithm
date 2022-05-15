n = int(input())

if n == 1:
    print(10)
else:
    matrix = [[0 for _ in range(10)] for _ in range(n)]
    matrix[0] = [1] * 10
    total = 0

    for i in range(1, n):
        matrix[i][9] = 1

    for i in range(1, n):
        for j in range(8, -1, -1):
            a = matrix[i-1][j] + matrix[i][j+1]
            matrix[i][j] = a
            if i == n-1:
                total += a

    print((total+1)%10007)