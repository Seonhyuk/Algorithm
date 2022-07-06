import sys
sys.stdin = open("input.txt")


def backtrack(teams, level=0, idx=0):
    global check, n, result, ability
    if level == n//2:
        team2 = []
        for i in range(n):
            if i not in teams:
                team2.append(i)

        sum_ability = 0
        sum_ability2 = 0
        for i in range(n//2):
            for j in range(i+1, n//2):
                sum_ability += ability[teams[i]][teams[j]] + ability[teams[j]][teams[i]]
                sum_ability2 += ability[team2[i]][team2[j]] + ability[team2[j]][team2[i]]

        value = abs(sum_ability - sum_ability2)
        if result is None:
            result = value
        elif result > value:
            result = value

        return
    else:
        for i in range(idx, n):
            if check[i]:
                check[i] = False
                teams.append(i)
                backtrack(teams, level+1, i+1)
                teams.pop()
                check[i] = True


n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
check = [True] * n
result = None
team = []
backtrack(team)
print(result)