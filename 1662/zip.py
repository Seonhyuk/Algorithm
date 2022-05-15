import sys
sys.stdin = open("input.txt")


def unpack(string):
    global result
    sub = 0
    for i in range(len(string)):
        if string[i] == '(':
            a = stack.pop()
            sub -= 1
            sub += unpack(string[i+1:]) * int(a)
        elif string[i] == ')':
            return sub
        else:
            stack.append(string[i])
            sub += 1

    return result

T = int(input())
for tc in range(T):
    zip = input()
    stack = []
    result = 0

    z = unpack(zip)
    print(z)