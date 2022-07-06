import sys
sys.stdin = open("input.txt")

from collections import deque

s = input()
t = deque(input())

rev = False

while len(t) >= len(s):
    if not rev:
        t.pop()
        if t[-1] == 'B':
            rev = not rev
    else:
        t.popleft()
        if t[0] == 'B':
            rev = not rev

if rev:
    t.reverse()

print(1 if ''.join(t) == s else 0)