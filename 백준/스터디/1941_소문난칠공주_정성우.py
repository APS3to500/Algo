dr = [0, -1, 1, 0]
dc = [1, 0, 0, -1]
dist = [input() for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
ans = set()


def track(y, s, cnt, ls):
    if y >= 4:
        return

    if cnt == 7:
        ls.sort()
        ans.add(tuple(ls))
        return

    for r, c in ls:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                visited[nr][nc] = 1
                if dist[nr][nc] == "Y":
                    track(y + 1, s, cnt + 1, ls + [(nr, nc)])
                else:
                    track(y, s + 1, cnt + 1, ls + [(nr, nc)])
                visited[nr][nc] = 0


for i in range(5):
    for j in range(5):
        if not visited[i][j]:
            visited[i][j] = 1
            if dist[i][j] == "Y":
                track(1, 0, 1, [(i, j)])
            else:
                track(0, 1, 1, [(i, j)])

print(len(ans))
