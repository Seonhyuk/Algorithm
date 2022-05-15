import sys, pprint
sys.stdin = open("input.txt")

n, k = map(int, input().split())
matrix = [[0 for _ in range(k+1)] for _ in range(n+1)]

weight = [0]
value = [0]

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(n+1):
    for j in range(k+1):
        if j >= weight[i]:
            if value[i] + matrix[i-1][j-weight[i]] > matrix[i-1][j]:
                matrix[i][j] = value[i] + matrix[i-1][j-weight[i]]
            else:
                matrix[i][j] = matrix[i-1][j]
        else:
            matrix[i][j] = matrix[i-1][j]

print(matrix[n][k])