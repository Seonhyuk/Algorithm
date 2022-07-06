import sys
sys.stdin = open("input.txt")


def preorder(alpha='A'):
    if alpha != '.':
        print(alpha, end='')
        preorder(tree[alpha][0])
        preorder(tree[alpha][1])


def inorder(alpha='A'):
    if alpha != '.':
        inorder(tree[alpha][0])
        print(alpha, end='')
        inorder(tree[alpha][1])


def postorder(alpha='A'):
    if alpha != '.':
        postorder(tree[alpha][0])
        postorder(tree[alpha][1])
        print(alpha, end='')


n = int(input())
tree = {}
for _ in range(n):
    node = input().split()
    tree[node[0]] = node[1:]

preorder()
print()
inorder()
print()
postorder()
print()