import sys
sys.stdin = open("input.txt")

n = int(input())
w_leng = int(input())
string= input()

cnt = 0
pattern = 'I' + 'OI' * n
leng = 2*n + 1


def KMP(p, s):
    global w_leng, leng, cnt
    lps = [0] * leng

    makelps(p, lps)

    i, j = 0, 0
    while i < length:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == leng:
            cnt += 1
            j = lps[j-1]


def makelps(p, lps):
    i, j = 1, 0

    while i < len(p):
        if p[j] == p[i]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j-1]


KMP(pattern, string)
print(cnt)