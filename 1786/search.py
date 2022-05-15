import sys
sys.stdin = open("input.txt")


def kmpSearch(p, t):
    global cnt, result
    m, n = len(p), len(t)
    lps = [0] * m

    computeLps(p, lps)

    i, j = 0, 0
    while i < n:
        if p[j] == t[i]:
            i += 1
            j += 1
        elif p[j] != t[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == m:
            cnt += 1
            result.append(i-j+1)
            j = lps[j - 1]


def computeLps(p, lps):
    leng = 0

    i = 1
    while i < len(p):
        if p[i] == p[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1


text = input()
pattern = input()
cnt = 0
result = []
kmpSearch(pattern, text)
print(cnt)
print(*result)