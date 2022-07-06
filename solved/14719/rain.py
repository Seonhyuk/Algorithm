import sys
sys.stdin = open("input.txt")


h, w = map(int, input().split())
field = list(map(int, input().split()))

left, right = [0] * w, [0] * w

for i in range(w-2, -1, -1):
    if field[i+1] > right[i+1]:
        right[i] = field[i+1]
    else:
        right[i] = right[i+1]

for i in range(1, w):
    if field[i-1] > left[i-1]:
        left[i] = field[i-1]
    else:
        left[i] = left[i-1]

cnt = 0
for i in range(1, w-1):
    if field[i] < min(left[i], right[i]):
        cnt += min(left[i], right[i]) - field[i]

print(cnt)