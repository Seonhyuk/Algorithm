import sys
sys.stdin = open("input.txt")

n, k = map(int, input().split())
schedule = list(map(int, input().split()))

multitap = [0] * n
result = 0

for i in range(k):
    for j in range(n):
        if multitap[j] == 0:
            multitap[j] = schedule[i]
            break
        elif multitap[j] == schedule[i]:
            break
    else:
        next = [101] * n
        for j in range(n):
            diff = 0
            for t in range(i+1, k):
                if schedule[t] == multitap[j]:
                    next[j] = diff
                    break
                diff += 1

        v, idx = 0, 0

        for t in range(n):
            if next[t] > v:
                v = next[t]
                idx = t

        multitap[idx] = schedule[i]

        result += 1

print(result)