import sys
sys.stdin = open("square.txt")

square_list = []

for _ in range(4):
    num_list = list(map(int, input().split()))
    square_list.append(num_list)

max_x = square_list[0][2]
max_y = square_list[0][3]

for square in square_list:
    if square[2] > max_x:
        max_x = square[2]
    if square[3] > max_y:
        max_y = square[3]

location = [[0 for _ in range(max_x)] for _ in range(max_y)]

for square in square_list:
    for y in range(square[1], square[3]):
        for x in range(square[0], square[2]):
            location[y][x] = 1
        
cnt = 0
for l in location:
    for i in l:
        cnt += i

print(cnt)

