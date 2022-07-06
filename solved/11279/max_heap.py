import sys
sys.stdin = open("input.txt")

# en-heap
def en_heap(n):
    global last
    last += 1
    tree[last] = n

    c = last      # 마지막으로 삽입된 원소의 위치
    p = c // 2    # c의 부모 노드
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


# de-heap
def de_heap():
    global last
    tmp = tree[1]               # 1번 노드를 뺀다
    tree[1] = tree[last]        # 마지막 노드를 1번 노드로 가져오고
    last -= 1                   # 트리의 길이를 1 낮춘다

    p = 1                       # 부모노드와
    c = p * 2                   # 자식노드를 초기화 한 후
    while c <= last:            # 트리의 leaf까지 탐색한다
        if c+1 <= last and tree[c] < tree[c+1]:     # 왼쪽 노드보다 오른쪽 노드가 크다면
            c += 1                                  # 오른쪽 노드를 선택한다

        if tree[p] < tree[c]:                       # 자식 노드가 부모 노드보다 크다면
            tree[p], tree[c] = tree[c], tree[p]     # 둘의 위치를 바꾼다
            p = c                                   # 자식노드로 내려가 다시 탐색한다
            c = p * 2
        else:
            break                                   # 부모노드가 더 크다면 멈춘다

    return tmp


n = int(input())
tree = [0] * (n+1)
last = 0

for _ in range(n):
    node = int(sys.stdin.readline())

    if node == 0:
        if last == 0:
            print(0)
        else:
            print(de_heap())
    else:
        en_heap(node)