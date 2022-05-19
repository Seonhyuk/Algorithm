import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline


def is_palindrome(s, e):
    while s < e:
        if nums[s] != nums[e]:
            return False
        s += 1
        e -= 1

    return True


n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 1

        elif dp[i][j] == 1:
            continue

        else:
            if is_palindrome(i, j):
                s, e = i, j
                while s < e:
                    dp[s][e] = 1
                    s += 1
                    e -= 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])