import sys
sys.stdin = open("input.txt")

n = int(input())

city = []
for _ in range(n):
    x, y = map(float, input().split())
    city.append((x, y))

dist = [[0] * n for _ in range(n)]
INF = int(1e09)

for i in range(n-1):
    for j in range(i+1, n):
        distance = ((city[i][0] - city[j][0]) ** 2 + (city[i][1] - city[j][1]) ** 2) ** (1/2)
        dist[i][j] = distance
        dist[j][i] = distance

size = 2 ** n - 1
dp = [[0] * size for _ in range(n)]

for i in range(1, n):
    dp[i][0] = dist[i][0]

for i in range(1, size):
    if not i % 2:
        for j in range(n):
            if False if i & (1 << j) else True:
                min_value = INF
                for k in range(1, n):
                    if True if i & (1 << k) else False:
                        m = dist[j][k] + dp[k][i & ~(1 << k)]
                        if m < min_value:
                            min_value = m
                        dp[j][i] = min_value

print(dp[0][-1])