import sys
sys.stdin = open("follownum.txt")

k = int(input())

for _ in range(k):
    N = int(input())
    max_num = 1
    max_list = [N]

    for i in range(1, N+1):
        follow = [N]
        follow.append(i)

        while follow[-1] >= 0:
            follow.append(follow[-2]-follow[-1])
        
        follow.pop()

        if len(follow) >= max_num:
            max_num = len(follow)
            max_list = follow

    max_list = map(str, max_list)

    a = " ".join(max_list)
    print(max_num)
    print(a)