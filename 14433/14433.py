import sys
sys.stdin = open("input.txt")


def dfs(n, k):
    if selected[n]:
        return False
    selected[n] = True

    if k == 0:
        for num in my[n]:
            if not my_t[num] or dfs(my_t[num], k):
                my_t[num] = n
                return True
    else:
        for num in op[n]:
            if not op_t[num] or dfs(op_t[num], k):
                op_t[num] = n
                return True

    return False


n, m, k, t = map(int, input().split())
my = [[] for _ in range(n+1)]
op = [[] for _ in range(n+1)]

my_t = [0] * (m+1)
op_t = [0] * (m+1)

for _ in range(k):
    i, j = map(int, input().split())
    my[i].append(j)

for _ in range(t):
    i, j = map(int, input().split())
    op[i].append(j)


for _ in range(2):
    for i in range(1, n+1):
        selected = [False] * (n+1)
        dfs(i, _)

a, b = 0, 0
for i in range(1, m+1):
    if my_t[i]:
        a += 1
    if op_t[i]:
        b += 1

if a >= b:
    print('그만 알아보자')
else:
    print('네 다음 힐딱이')