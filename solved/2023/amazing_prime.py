import sys
sys.stdin = open("input.txt")


def backtrack(number, level=0):
    global n
    if number == 1:
        return

    if level >= 1:
        for k in range(2, int(number**(1/2))+1):
            if number % k == 0:
                return

    if level == n:
        print(number)

    for i in range(6):
        number = 10*number + numbers[i]
        backtrack(number, level+1)
        number //= 10


n = int(input())

numbers = [1, 2, 3, 5, 7, 9]
number = 0
backtrack(number)