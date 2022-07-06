import sys
sys.stdin = open("input.txt")

n = int(input())
buildings = list(map(int, input().split()))
stack = []
index_stack = []
laser = [0] * n

for i in range(n - 1, 0, -1):
    if buildings[i] < buildings[i - 1]:
        laser[i] = i
        while stack:
            if stack[-1] < buildings[i - 1]:
                stack.pop()
                laser[index_stack.pop()] = i
            else:
                break
    else:
        stack.append(buildings[i])
        index_stack.append(i)

print(*laser)
