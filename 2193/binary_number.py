n = int(input())

one_end = [1, 0]
zero_end = [0, 1]

for i in range(n-2):
    one_end.append(zero_end[-1])
    zero_end.append(zero_end[-1]+one_end[-2])

print(one_end[-1]+zero_end[-1])