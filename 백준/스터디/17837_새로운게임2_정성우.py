n, k = map(int, input().split())
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)
piece = dict()
maps = [list(map(int, input().split())) for _ in range(n)]
dist = [[list() for _ in range(n)] for _ in range(n)]
for i in range(1, k + 1):
    r, c, d = map(lambda x: int(x) - 1, input().split())
    piece[i] = [r, c, d]
    dist[r][c].append(i)

turn = 0
flag = False
while True:
    turn += 1

    for i in range(1, k + 1):
        r, c, d = piece[i]
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            # white
            if maps[nr][nc] == 0:
                idx = dist[r][c].index(i)
                for a in dist[r][c][idx:]:
                    piece[a] = [nr, nc, piece[a][2]]
                dist[nr][nc].extend(dist[r][c][idx:])
                dist[r][c] = dist[r][c][:idx]
                if len(dist[nr][nc]) >= 4:
                    flag = True
                    break

            # red
            elif maps[nr][nc] == 1:
                idx = dist[r][c].index(i)
                for a in dist[r][c][idx:]:
                    piece[a] = [nr, nc, piece[a][2]]
                dist[nr][nc].extend(dist[r][c][idx:][::-1])
                dist[r][c] = dist[r][c][:idx]
                if len(dist[nr][nc]) >= 4:
                    flag = True
                    break

            # blue
            else:
                if d in (0, 1):
                    d = 1 - d
                else:
                    d = 5 - d
                nr = r + dr[d]
                nc = c + dc[d]
                piece[i] = [r, c, d]  # 이동을 못해도 방향은 바꿔줘야한다.
                if 0 <= nr < n and 0 <= nc < n and maps[nr][nc] != 2:
                    idx = dist[r][c].index(i)
                    for a in dist[r][c][idx:]:
                        piece[a] = [nr, nc, piece[a][2]]
                    piece[i] = [nr, nc, d]
                    # 방향을 바꾼후에 이동할때도 색을 고려해서 쌓아야한다.
                    if maps[nr][nc] == 0:
                        dist[nr][nc].extend(dist[r][c][idx:])
                    elif maps[nr][nc] == 1:
                        dist[nr][nc].extend(dist[r][c][idx:][::-1])
                    dist[r][c] = dist[r][c][:idx]
                    if len(dist[nr][nc]) >= 4:
                        flag = True
                        break
        else:
            if d in (0, 1):
                d = 1 - d
            else:
                d = 5 - d
            nr = r + dr[d]
            nc = c + dc[d]
            piece[i] = [r, c, d]
            if 0 <= nr < n and 0 <= nc < n and maps[nr][nc] != 2:
                idx = dist[r][c].index(i)
                for a in dist[r][c][idx:]:
                    piece[a] = [nr, nc, piece[a][2]]
                piece[i] = [nr, nc, d]
                if maps[nr][nc] == 0:
                    dist[nr][nc].extend(dist[r][c][idx:])
                elif maps[nr][nc] == 1:
                    dist[nr][nc].extend(dist[r][c][idx:][::-1])
                dist[r][c] = dist[r][c][:idx]
                if len(dist[nr][nc]) >= 4:
                    flag = True
                    break

    if flag:
        break
    if turn > 1000:
        turn = -1
        break
print(turn)
