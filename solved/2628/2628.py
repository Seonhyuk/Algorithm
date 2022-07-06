import sys
sys.stdin = open("paper.txt")

width, height = map(int, input().split())
width_list = [0]
height_list = [0]

n = int(input())
for _ in range(n):
    number, value = map(int, input().split())
    if not number: width_list.append(value)
    else: height_list.append(value)

width_list.sort()
height_list.sort()
a_list, b_list = [width_list[0]], [height_list[0]]

for i in range(1, len(width_list)):
    a_list.append(width_list[i]-width_list[i-1])
a_list.append(height-width_list[-1])

for i in range(1, len(height_list)):
    b_list.append(height_list[i]-height_list[i-1])
b_list.append(width-height_list[-1])

print(max(a_list)*max(b_list))