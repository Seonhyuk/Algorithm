import sys
from collections import defaultdict
sys.stdin = open("input.txt")

n = int(input())

words = []

for _ in range(n):
    word = input()
    words.append(word)

words.sort(reverse=True, key=lambda x: len(x))

location = defaultdict(list)
length = len(words[0])

while length > 0:
    for i in range(n):
        if len(words[i]) >= length:
            alpha = words[i][len(words[i]) - length]
            location[alpha].append(length)

    length -= 1

value = defaultdict(int)

for key in location.keys():
    for i in range(len(location[key])):
        value[key] += 10 ** (location[key][i] - 1)

num = 9
result = 0
res = list(value.values())
res.sort(reverse=True)

for i in range(len(res)):
    result += res[i] * num
    num -= 1

print(result)
