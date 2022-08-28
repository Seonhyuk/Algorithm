__import__("sys").stdin = open("input.txt")
input = __import__("sys").stdin.readline


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, string):
        node = self.root
        for s in string:
            if s not in node:
                node[s] = {}
            if "*" in node:
                return False
            node = node[s]

        node["*"] = True
        return True


t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    numbers.sort()

    trie = Trie()

    for num in numbers:
        result = trie.insert(num)

        if not result:
            print("NO")
            break
    else:
        print("YES")

