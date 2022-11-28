import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

p = 1000000007


def power(x, exponent):
    if exponent == 1:
        return x
    else:
        new_x = power(x, exponent // 2)
        if exponent % 2:
            return (new_x * new_x * x) % p
        else:
            return (new_x * new_x) % p


n, k = map(int, input().split())
dp = [1, 1]

for i in range(2, n+1):
    dp.append((dp[-1] * i) % p)

answer = (dp[n] * power((dp[k] * dp[n-k]) % p, p-2)) % p
print(answer)
