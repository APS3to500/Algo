import sys

input = sys.stdin.readline

n, h = map(int, input().split())

cave = [int(input()) for _ in range(n)]

up = [0] * (h + 1)  # 석순
down = [0] * (h + 1)  # 종유석

for i in range(n):
    if i % 2:
        down[h - cave[i] + 1] += 1
    else:
        up[cave[i]] += 1

for i in range(1, h + 1):
    down[i] += down[i - 1]

for i in range(h - 1, 0, -1):
    up[i] += up[i + 1]

for i in range(1, h + 1):
    up[i] += down[i]

ans = min(up[1:])
print(ans, up[1:].count(ans))
