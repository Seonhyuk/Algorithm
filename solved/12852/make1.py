import sys
sys.stdin = open("input.txt")

n = int(input())
value = n
result = [n]

cnt = [0, 0]
for i in range(2, n+1):
    if i % 2 == 0 and i % 3 == 0:
        cnt.append(min(cnt[-1], cnt[i//2], cnt[i//3]) + 1)
    elif i % 2 == 0:
        cnt.append(min(cnt[-1], cnt[i//2]) + 1)
    elif i % 3 == 0:
        cnt.append(min(cnt[-1], cnt[i//3]) + 1)
    else:
        cnt.append(cnt[-1] + 1)

while n > 1:
    min_idx = n-1
    if n % 2 == 0 and n % 3 == 0:
        for k in (n//2, n//3):
            if cnt[k] < cnt[min_idx]:
                min_idx = k
    elif n % 2 == 0:
        if cnt[min_idx] > cnt[n//2]:
            min_idx = n//2
    elif n % 3 == 0:
        if cnt[min_idx] > cnt[n//3]:
            min_idx = n//3

    result.append(min_idx)
    n = min_idx

print(cnt[value])
print(*result)