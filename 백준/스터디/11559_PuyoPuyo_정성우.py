from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

field = [list(input()) for _ in range(12)]
ans = 0


def bfs(a, b, word):
    q = deque([])
    q.append((a, b))
    cand = [(a, b)]
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and field[nr][nc] == word:
                q.append((nr, nc))
                cand.append((nr, nc))
                visited[nr][nc] = 1

    if len(cand) >= 4:
        for r, c in cand:
            field[r][c] = '.'
        return True
    return False


def move():
    for c in range(6):
        q = deque()
        for r in range(11, -1, -1):
            if field[r][c] != '.':
                q.append(field[r][c])

        for r in range(11, -1, -1):
            if q:
                field[r][c] = q.popleft()
            else:
                field[r][c] = '.'


while True:
    flag = False
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if not visited[i][j]:
                visited[i][j] = 1
                if field[i][j] != '.':
                    if bfs(i, j, field[i][j]):
                        flag = True

    if flag:
        ans += 1
        move()
    else:
        break

print(ans)
