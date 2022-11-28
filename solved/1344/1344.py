import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

team1 = int(input()) / 100
team2 = int(input()) / 100


def percentage(power, exponent):
    return power ** exponent * (1 - power) ** (18 - exponent)


primes = [2, 3, 5, 7, 11, 13, 17]

dp = [[0] * 19 for _ in range(19)]

for i in range(19):
    dp[0][i] = 1

for i in range(1, 19):
    for j in range(1, 19):
        if i <= j:
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

p1 = 0
p2 = 0

for prime in primes:
    p1 += dp[prime][18] * percentage(team1, prime)
    p2 += dp[prime][18] * percentage(team2, prime)

print(p1 + p2 - p1 * p2)
