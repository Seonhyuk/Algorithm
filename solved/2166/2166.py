import sys
sys.stdin = open("input.txt")

n = int(input())

nodes = []

for _ in range(n):
    x, y = map(int, input().split())
    nodes.append([x, y])

nodes.append(nodes[0])

a = 0
b = 0
for i in range(n):
    a += nodes[i][0] * nodes[i+1][1]
    b += nodes[i][1] * nodes[i+1][0]

result = (a-b) / 2
print(abs(result))