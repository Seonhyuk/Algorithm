import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n = int(input())

    legal = [0, 1]
    if n <= 1:
        print(n)
    else:
        for i in range(2, n+1):
            if i <= 2:
                legal.append(min(legal[i-1], legal[i-2])+1)
            elif i <= 5:
                legal.append(min(legal[i-1], legal[i-2], legal[i-5])+1)
            else:
                legal.append(min(legal[i-1], legal[i-2], legal[i-5], legal[i-7])+1)
        print(legal[-1])