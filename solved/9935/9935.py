__import__("sys").stdin = open("input.txt")
input = __import__("sys").stdin.readline

string = input().rstrip()
c = input().rstrip()

stack = []
alpha = c[-1]
length = len(c)

for s in string:
    stack.append(s)

    if s == alpha and c == "".join(stack[-length:]):
        for _ in range(length):
            stack.pop()

result = "".join(stack)

if result:
    print(result)
else:
    print("FRULA")
