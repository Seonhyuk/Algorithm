page = int(__import__("sys").stdin.readline())
result = [0] * 10
point, start = 1, 1


def calc(x):
    while x > 0:
        result[x % 10] += point
        x //= 10


while start <= page:
    while page % 10 != 9 and start <= page:
        calc(page)
        page -= 1

    if page < start:
        break

    while start % 10 != 0 and start <= page:
        calc(start)
        start += 1

    start //= 10
    page //= 10
    for i in range(10):
        result[i] += (page - start + 1) * point

    point *= 10

print(*result)