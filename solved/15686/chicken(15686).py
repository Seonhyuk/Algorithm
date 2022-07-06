import sys
sys.stdin = open("input.txt")


def bruteforce(chicken_list, level=0, idx=0):
    global m, min_total
    if level == m:
        total = 0
        for h in home:
            distance = 1000000
            for c in chicken_list:
                distance = min(abs(h[0] - c[0]) + abs(h[1] - c[1]), distance)
            total += distance

        if total < min_total:
            min_total = total

    else:
        for i in range(idx, len(chicken)):
            chicken_list.append(chicken[i])
            bruteforce(chicken_list, level+1, i+1)
            chicken_list.pop()


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            home.append((i, j))
        elif matrix[i][j] == 2:
            chicken.append((i, j))

min_total = 1000000
chicken_list = []

bruteforce(chicken_list)

print(min_total)