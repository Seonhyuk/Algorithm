import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    pattern = input()
    n = int(input())
    lst = input()[1:-1]
    reverse = False

    for p in pattern:
        if p == 'R':
            reverse = False if reverse else True
        else:
            numbers = 0
            if reverse:
                a = len(lst) - 1
                while 0 <= a < len(lst):
                    if lst[a].isdigit():
                        a -= 1
                        numbers += 1
                    else:
                        break
            else:
                a = 0
                while 0 <= a < len(lst):
                    if lst[a].isdigit():
                        a += 1
                        numbers += 1
                    else:
                        break

            if not lst:
                print('error')
                break
            if reverse:
                lst = lst[:-(numbers+1)]
            else:
                lst = lst[numbers+1:]
    else:
        if reverse:
            a = lst.split(',')
            a.reverse()
            lst = ",".join(a)

        print('['+lst+']')