import sys
sys.stdin = open("input.txt")


n = int(input())
stairs = [int(input()) for _ in range(n)]

dp_one = [0, stairs[0]]
dp_two = [0, stairs[0]]

while len(dp_one) < n + 1:
    dp_one.append(dp_two[-1] + stairs[len(dp_one)-1])
    dp_two.append(max(dp_one[-3], dp_two[-2]) + stairs[len(dp_two)-1])

print(max(dp_one[-1], dp_two[-1]))