import sys
sys.stdin = open("input.txt")

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]

result = [10001] * (k+1)
for coin in coin_list:
    if coin <= k:
        result[coin] = 1

for i in range(1, 1+k):
    min_coin = 10001
    if i not in coin_list:
        for coin in coin_list:
            if i-coin >= 0:
                if result[i-coin] != 0:
                    min_coin = min(result[i-coin], min_coin)

    if min_coin != 10001:
        result[i] = min_coin+1

print(result[-1] if result[-1] != 10001 else -1)
