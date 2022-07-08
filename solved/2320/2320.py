import sys
sys.stdin = open("input.txt")

n = int(input())
words = [input() for _ in range(n)]
length = [0] * n

for i in range(n):
    length[i] = len(words[i])

size = 2 ** n

dp = [[0] * size for _ in range(n)]
result = 0

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            m = 0
            for k in range(n):
                if k != j and (words[k][-1] == words[j][0] or i & ~(1 << j) == 0):
                    m = max(m, dp[k][i & ~(1 << j)] + length[j])

            dp[j][i] = m
            result = max(m, result)

print(result)