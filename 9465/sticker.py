import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(sticker[0][0], sticker[0][1]))
    else:
        sticker[0][1] = sticker[0][1] + sticker[1][0]
        sticker[1][1] = sticker[1][1] + sticker[0][0]


        for i in range(2, n):
            sticker[0][i] = max(sticker[0][i] + sticker[1][i-2], sticker[0][i] + sticker[1][i-1])
            sticker[1][i] = max(sticker[1][i] + sticker[0][i-2], sticker[1][i] + sticker[0][i-1])

        print(max(sticker[0][-1], sticker[1][-1]))