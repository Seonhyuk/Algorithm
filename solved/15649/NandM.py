import sys, pprint
sys.stdin = open("input.txt")


def backtrack(total, level=0, idx=0):
    global n, m, check
    if level == m:
        print(*total)
        return
    else:
        for i in range(idx, n):
            total.append(i+1)
            backtrack(total, level+1, i)
            total.pop()


n, m = map(int, input().split())
total = []
backtrack(total)