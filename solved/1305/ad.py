import sys

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(4)]
for _ in range(m):
    calc = list(map(int, sys.stdin.readline().split()))
    if not calc[0]:
        matrix[calc[2]-1][calc[1]-1] = calc[3]
    else:
        total = 0
        for i in range(calc[2]-1, calc[4]):
            total += sum(matrix[i][calc[1]-1:calc[3]])
        print(total)