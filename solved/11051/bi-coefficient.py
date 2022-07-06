n, k = map(int, input().split())
if k > n // 2:
    k = n - k

matrix = [[0 for _ in range(n+1)] for _ in range(k+1)]
matrix[0] = [1 for i in range(n+1)]
total, total2 = 0, 0

for i in range(1, k+1):
    for j in range(1, n+1):
        matrix[i][j] = matrix[i-1][j-1] + matrix[i][j-1]

print(matrix[k][n] % 10007)