import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


g = int(input())
p = int(input())

parent = [x for x in range(g + 1)]

ans = 0
closed = False  # 폐쇄여부

for _ in range(p):
    gi = int(input())
    if not closed:
        x = find(gi)    # 도킹할 수 있는 곳 중 가장 큰 곳을 찾아준다
        if x == 0:  # 더이상 도킹할 수 있는 곳이 없으면
            closed = True
            break
        else:
            union(x, x - 1) # 도킹시킨 후 다음 도킹 예정지를 정해준다
            ans += 1
print(ans)
