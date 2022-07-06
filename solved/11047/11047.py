import sys
sys.stdin = open("input.txt")

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

result = 0
for i in range(n-1, -1, -1):

    a = k // coins[i]
    result += a
    k -= a * coins[i]

print(result)