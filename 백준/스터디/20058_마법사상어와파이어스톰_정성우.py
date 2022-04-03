import sys
from collections import deque
from copy import deepcopy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

input = sys.stdin.readline
n, q = map(int, input().split())

dist = [list(map(int, input().split())) for _ in range(1 << n)]
lst = list(map(int, input().split()))


def turn90(i, j, l):
    m = 2 ** l
    new_arr = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            new_arr[r][c] = dist[i + m - 1 - c][j + r]
    for r in range(m):
        for c in range(m):
            dist[i + r][j + c] = new_arr[r][c]

    return new_arr


def bfs(i, j):
    group = 1
    dist[i][j] = 0
    q = deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < (1 << n) and 0 <= nc < (1 << n) and dist[nr][nc]:
                q.append((nr, nc))
                group += 1
                dist[nr][nc] = 0
    return group


for l in lst:
    for i in range(0, 1 << n, 1 << l):
        for j in range(0, 1 << n, 1 << l):
            turn90(i, j, l)

    # 얼음이 동시에 녹아야하므로 복사해서 원본을 temp에 저장
    temp = deepcopy(dist)
    for r in range(1 << n):
        for c in range(1 << n):
            if dist[r][c]:
                cnt = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < (1 << n) and 0 <= nc < (1 << n) and temp[nr][nc]:
                        cnt += 1
                if cnt < 3:
                    dist[r][c] -= 1

print(sum(sum(i) for i in dist))
max_group = 0
for i in range(1 << n):
    for j in range(1 << n):
        if dist[i][j]:
            max_group = max(max_group, bfs(i, j))

print(max_group)
