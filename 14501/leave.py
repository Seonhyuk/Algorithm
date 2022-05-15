import sys
sys.stdin = open("input.txt")


def leave(total_pay=0, idx=0):
    global days, pays, check, n, max_pay
    if idx > n:
        return

    if total_pay > max_pay:
        max_pay = total_pay

    for i in range(idx, n):
        if check[i]:
            check[i] = False

            total_pay += pays[i]
            leave(total_pay, i+days[i])
            total_pay -= pays[i]

            check[i] = True


n = int(input())

days = []
pays = []

for _ in range(n):
    d, p = map(int, input().split())
    days.append(d)
    pays.append(p)

check = [True] * n
max_pay = 0
leave()
print(max_pay)