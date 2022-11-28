import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline


def printout(node, level=0):
    lst = list(node.keys())
    lst.sort()

    for key in lst:
        print('--' * level + key)
        if node[key]:
            printout(node[key], level+1)


n = int(input())

values = {}

for i in range(n):
    value = input().rstrip().split()

    node = values

    for j in range(1, int(value[0])+1):
        if value[j] not in node:
            node[value[j]] = {}

        node = node[value[j]]

printout(values)