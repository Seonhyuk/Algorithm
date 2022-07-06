import sys
sys.stdin = open("input.txt")


n, k = map(int, input().split())
result = [[0 for _ in range(k)] for _ in range(n)]
result[0] = [i for i in range(1, k+1)]
for i in range(1, n):
    for j in range(k):
        result[i][j] = sum(result[i-1][:j+1])

print(result[n-1][k-1] % 1000000000)