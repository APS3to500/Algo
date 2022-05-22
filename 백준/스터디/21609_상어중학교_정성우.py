from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def find_big(x, y):
    q = deque()
    q.append((x, y))
    vis[x][y] = True
    clr = 1
    rainbow = 0
    rainbow_blocks = []
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc] and (arr[nr][nc] == arr[x][y] or arr[nr][nc] == 0):
                vis[nr][nc] = True
                if arr[nr][nc] == arr[x][y]:
                    clr += 1
                    q.append((nr, nc))
                elif arr[nr][nc] == 0:
                    rainbow += 1
                    q.append((nr, nc))
                    rainbow_blocks.append((nr, nc))

    for nr, nc in rainbow_blocks:
        vis[nr][nc] = False
    return clr + rainbow, rainbow, x, y


def remove_block(x, y, z):
    v = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    v[x][y] = True
    arr[x][y] = -2
    b = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] and (arr[nr][nc] == 0 or arr[nr][nc] == z):
                b += 1
                v[nr][nc] = True
                q.append((nr, nc))
                arr[nr][nc] = -2
    return b * b


def gravity():
    for c in range(n):
        for r in range(n - 2, -1, -1):
            if arr[r][c] > -1:
                idx = r
                while True:
                    if idx + 1 < n and arr[idx + 1][c] == -2:
                        arr[idx + 1][c] = arr[idx][c]
                        arr[idx][c] = -2
                        idx += 1
                    else:
                        break


def rotate():
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[n - 1 - j][i] = arr[i][j]
    return new_arr


ans = 0
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

while True:
    vis = [[False] * n for _ in range(n)]
    blocks = []
    # 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] not in (0, -1, -2) and not vis[i][j]:
                x, y, z, w = find_big(i, j)
                if x >= 2:
                    blocks.append((x, y, z, w))

    blocks.sort(reverse=True)
    if not blocks:
        break

    # 2
    r, c = blocks[0][2], blocks[0][3]
    ans += remove_block(r, c, arr[r][c])

    # 3.
    gravity()

    # 4.
    arr = rotate()

    # 5.
    gravity()

print(ans)
