import sys
sys.stdin = open("input.txt")


def find(n):
    if n != reps[n]:
        reps[n] = find(reps[n])
    return reps[n]


def union(n1, n2):
    r1 = find(n1)
    r2 = find(n2)
    reps[r2] = r1


n = int(input())
lines = []
reps = list(range(n))

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append([x1, y1, x2, y2])

for i in range(n-1):
    for j in range(i+1, n):
        if find(i) != find(j):
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]

            if x2 < x1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            if x4 < x3:
                x3, x4 = x4, x3
                y3, y4 = y4, y3

            if x1 == x2:
                q = x1
                inclination1 = None
                if y2 < y1:
                    y1, y2 = y2, y1
            else:
                inclination1 = (y2 - y1) / (x2 - x1)

            if x3 == x4:
                w = x3
                inclination2 = None
                if y4 < y3:
                    y3, y4 = y4, y3
            else:
                inclination2 = (y4 - y3) / (x4 - x3)

            if inclination1 == inclination2:
                if inclination1 is not None:
                    if y1 - inclination1 * x1 == y3 - inclination2 * x3:
                        if x4 >= x2:
                            if x2 >= x3:
                                result = 1

                            else:
                                result = 0
                        else:
                            if x4 >= x1:
                                result = 1
                            else:
                                result = 0
                    else:
                        result = 0
                else:
                    if q != w:
                        result = 0
                    else:
                        if y4 >= y2:
                            if y2 >= y3:
                                result = 1
                            else:
                                result = 0
                        else:
                            if y4 >= y1:
                                result = 1
                            else:
                                result = 0

            else:
                if inclination1 is None:
                    x = q
                    y = inclination2 * x - inclination2 * x3 + y3
                elif inclination2 is None:
                    x = w
                    y = inclination1 * x - inclination1 * x1 + y1
                else:
                    x = (inclination1 * x1 - inclination2 * x3 + y3 - y1) / (inclination1 - inclination2)
                    y = inclination1 * x - inclination1 * x1 + y1

                if y2 < y1:
                    y1, y2 = y2, y1
                if y4 < y3:
                    y3, y4 = y4, y3

                if x1 - 0.00001 <= x <= x2 + 0.00001 and x3 - 0.00001 <= x <= x4 + 0.00001 and y1 - 0.00001 <= y <= y2 + 0.00001 and y3 - 0.00001 <= y <= y4 + 0.00001:
                    result = 1
                else:
                    result = 0

            if result == 1:
                union(i, j)

result = set()
result2 = [0] * n

for i in range(n):
    find(i)

for i in range(n):
    result2[reps[i]] += 1
    result.add(reps[i])

print(len(result))
print(max(result2))