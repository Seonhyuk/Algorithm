import sys
sys.stdin = open("input.txt")


def search(n, alphabets, check, idx=0):
    global password, consonants
    if len(password) == n:
        if 'a' in password or 'e' in password or 'i' in password or 'o' in password or 'u' in password:
            cnt = 0
            for p in password:
                if p in consonants:
                    cnt += 1
            if cnt >= 2:
                print(password)
        return

    else:
        for i in range(idx, len(alphabets)):
            if check[i]:
                check[i] = False
                password += alphabets[i]
                search(n, alphabets, check, i+1)
                password = password[:len(password)-1]
                check[i] = True


l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
check_list = [True] * c
password = ''
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
search(l, alpha, check_list)