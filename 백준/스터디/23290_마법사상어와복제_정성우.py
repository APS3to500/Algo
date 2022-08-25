from copy import deepcopy

m, s = map(int, input().split())

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
sdr = [-1, 0, 1, 0]
sdc = [0, -1, 0, 1]

smell = [[0] * 4 for _ in range(4)]
graph = [[[0] * 8 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    fx, fy, d = map(lambda x: int(x) - 1, input().split())
    graph[fx][fy][d] += 1

sr, sc = map(lambda x: int(x) - 1, input().split())


def shark_move(r, c, path, cnt, fish, vis):
    if cnt == 3:
        routes.append((path, fish))
        return

    for i in range(4):
        nr = r + sdr[i]
        nc = c + sdc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            if vis[nr][nc]:
                shark_move(nr, nc, path + (i + 1) * 10 ** (2 - cnt), cnt + 1, fish, vis)
            else:
                vis[nr][nc] = 1
                shark_move(nr, nc, path + (i + 1) * 10 ** (2 - cnt), cnt + 1, fish + sum(graph[nr][nc]), vis)
                vis[nr][nc] = 0


for _ in range(s):
    # 1 복제
    temp = deepcopy(graph)

    # 2 물고기 이동
    graph = [[[0] * 8 for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            for i in range(8):
                if not temp[r][c][i]:
                    continue
                d = i
                fish = temp[r][c][i]

                for _ in range(8):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (sr, sc) and not smell[nr][nc]:
                        graph[nr][nc][d] += fish
                        break
                    else:
                        d = (d - 1) % 8
                else:
                    graph[r][c][i] += fish

    # 3 상어이동

    visited = [[0] * 4 for _ in range(4)]
    routes = []
    shark_move(sr, sc, 0, 0, 0, visited)
    routes.sort(key=lambda x: (-x[1], x[0]))
    path = str(routes[0][0])

    for i in range(3):
        sr += sdr[int(path[i]) - 1]
        sc += sdc[int(path[i]) - 1]
        if sum(graph[sr][sc]) != 0:
            graph[sr][sc] = [0] * 8
            smell[sr][sc] = 3

    # 4 냄세 제거
    for r in range(4):
        for c in range(4):
            if smell[r][c]:
                smell[r][c] -= 1

    # 5 복제 완료
    for r in range(4):
        for c in range(4):
            for i in range(8):
                graph[r][c][i] += temp[r][c][i]
ans = 0
for r in range(4):
    for c in range(4):
        ans += sum(graph[r][c])
print(ans)
