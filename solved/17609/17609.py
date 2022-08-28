import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline


def is_palin(word, result=0):
    start, end = 0, len(word) - 1

    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1

        else:
            if result == 0:
                if word[start+1] == word[end] or word[start] == word[end-1]:
                    result += 1

                    if word[start+1] == word[end] and word[start] == word[end-1]:
                        a = is_palin(word[start+1:end+1], 1)
                        b = is_palin(word[start:end], 1)
                        return min(a, b)
                    elif word[start+1] == word[end]:
                        start += 1
                    elif word[start] == word[end-1]:
                        end -= 1

                else:
                    return 2
            else:
                return 2

    return result


n = int(input())
for _ in range(n):
    word = input().rstrip()

    print(is_palin(word))