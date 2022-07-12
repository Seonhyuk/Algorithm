import sys
sys.stdin = open("input.txt")


def is_palin(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i+1)]:
            return False

    return True


n = int(input())
words = [input() for _ in range(n)]

size = 2 ** n

dp = [[[] for _ in range(size)] for _ in range(n)]

result = 0

for i in range(n):
    dp[i][2**i].append(words[i])
    if is_palin(words[i]):
        result += 1

for i in range(3, 1 << n):
    for j in range(n):
        if i & (1 << j):
            t = i & ~(1 << j)
            for k in range(n):
                if dp[k][t]:
                    for l in range(len(dp[k][t])):
                        new_word = dp[k][t][l] + words[j]
                        dp[j][i].append(new_word)

                        if is_palin(new_word):
                            result += 1

print(result)