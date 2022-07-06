import sys
sys.stdin = open("input.txt")


def backtrack(level=0, idx=0):
    global n, check, num_list, lotto
    if level == 6:
        print(*num_list)

    for i in range(idx, n):
        if check[i]:
            check[i] = False
            num_list.append(lotto[i])
            backtrack(level+1, i+1)
            num_list.pop()
            check[i] = True


while True:
    lotto = list(map(int, input().split()))
    n = lotto.pop(0)
    if not n:
        break
    else:
        check = [True] * len(lotto)
        num_list = []
        backtrack()
        print()