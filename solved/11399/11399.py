import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
sub = 0
for i in range(n):
    result += sub + arr[i]
    sub += arr[i]

print(result)