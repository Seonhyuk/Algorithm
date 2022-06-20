import sys
sys.stdin = open("input.txt")

n = int(input())
a, b, c, d = [], [], [], []

for _ in range(n):
    q, w, e, r = map(int, input().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)

lst1 = dict()
for num1 in a:
    for num2 in b:
        if (num1 + num2) in lst1:
            lst1[num1 + num2] += 1
        else:
            lst1[num1 + num2] = 1

result = 0
for num1 in c:
    for num2 in d:
        if -(num1 + num2) in lst1:
            result += lst1[-(num1 + num2)]

print(result)
