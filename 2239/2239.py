import sys, copy
# sys.stdin = open("input.txt")


def x_check(num, x):
    for i in range(9):
        if sudoku[x][i] == num:
            return False
    return True


def y_check(num, y):
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True


def s_check(num, x, y):
    x, y = x - x % 3, y - y % 3
    for i in range(3):
        for j in range(3):
            if sudoku[x+i][y+j] == num:
                return False
    return True


def backtrack(level=0):
    global n
    if level == n:
        for i in range(9):
            s = ''
            for j in range(9):
                s += str(sudoku[i][j])
            print(s)
        exit()

    x, y = zeros[level]
    for j in range(1, 10):
        if x_check(j, x) and y_check(j, y) and s_check(j, x, y):
            sudoku[x][y] = j
            backtrack(level + 1)
            sudoku[x][y] = 0


sudoku = [list(map(int, input())) for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))

result = []
n = len(zeros)
backtrack()