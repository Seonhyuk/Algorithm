import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n = int(input())
    first_alpha = [0 for _ in range(11)]
    second_alpha = [0 for _ in range(11)]

    string = {}
    result = 0

    for i in range(n):
        s = input()
        result += first_alpha[ord(s[0])-97]
        result += second_alpha[ord(s[1])-97]

        first_alpha[ord(s[0])-97] += 1
        second_alpha[ord(s[1])-97] += 1

        if s in string:
            string[s] += 1
        else:
            string[s] = 1

        result -= (string[s] - 1) * 2

    print(result)
