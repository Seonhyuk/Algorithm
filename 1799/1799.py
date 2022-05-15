import sys
sys.stdin = open("input.txt")


def searchwhite(w_lst, cnt=0, idx=0):
    global w_result, w_leng

    if w_leng - idx + cnt < w_result:
        return

    for i in range(len(w_lst) - 1):
        if abs(w_lst[-1][0] - w_lst[i][0]) == abs(w_lst[-1][1] - w_lst[i][1]):
            return

    if cnt > w_result:
        w_result = cnt

    for i in range(idx, w_leng):
        w_lst.append(white[i])
        searchwhite(w_lst, cnt + 1, i + 1)
        w_lst.pop()


def searchblack(b_lst, cnt=0, idx=0):
    global b_result, b_leng

    if b_leng - idx + cnt < b_result:
        return

    for i in range(len(b_lst) - 1):
        if abs(b_lst[-1][0] - b_lst[i][0]) == abs(b_lst[-1][1] - b_lst[i][1]):
            return

    if cnt > b_result:
        b_result = cnt

    for i in range(idx, b_leng):
        b_lst.append(black[i])
        searchblack(b_lst, cnt + 1, i + 1)
        b_lst.pop()


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

black = []
white = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            if (i+j) % 2:
                black.append((i, j))
            else:
                white.append((i, j))

w_leng, b_leng = len(white), len(black)
w_result, b_result = 0, 0

w_lst = []
b_lst = []

searchwhite(w_lst)
searchblack(b_lst)

print(w_result + b_result)