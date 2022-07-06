import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n = int(input())
    apps = list(map(int, input().split()))
    check = [False] * n
    cnt = [0] * n
    result = 0

    for i in range(n):
        if not check[i]:
            q = [i]

            while q:
                x = q.pop()
                if not check[x]:
                    cnt[x] += 1
                    if cnt[x] >= 2:
                        check[x] = True
                        result += 1

                    if not check[apps[x]-1]:
                        q.append(apps[x]-1)

            q = [i]

            while q:
                x = q.pop()
                if not check[x]:
                    check[x] = True
                    if not check[apps[x]-1]:
                        q.append(apps[x]-1)

    print(n - result)