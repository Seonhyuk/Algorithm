import sys
sys.stdin = open("switch.txt")

def change_switch(n):
    if n == 0:
        return 1
    else:
        return 0

N = int(input())
switch = list(map(int, input().split()))
people_num = int(input())
people = []
for _ in range(people_num):
    person = list(map(int, input().split()))
    people.append(person)

for person in people:
    if person[0] == 1:
        num = person[1]
        while num-1 < len(switch):
            switch[num-1] = change_switch(switch[num-1])
            num += person[1]
        
    else:
        num = person[1]
        switch[num-1] = change_switch(switch[num-1])
        i = 1
        while True:
            if num+i <= len(switch) and num-1-i >= 0 and switch[num-1-i] == switch[num-1+i]:
                switch[num-1-i] = change_switch(switch[num-1-i])
                switch[num-1+i] = change_switch(switch[num-1+i])
                i += 1
            else:
                break

k = 0
for s in switch:
    print(s, end=" ")
    k += 1
    if k == 20:
        k = 0
        print()