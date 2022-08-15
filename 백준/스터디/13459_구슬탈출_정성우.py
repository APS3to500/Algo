from collections import deque

n, m = map(int, input().split())
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

dist = [list(input()) for _ in range(n)]
visited = set()
q = deque()

for i in range(n):
    for j in range(m):
        if dist[i][j] == "R":
            rr, rc = i, j
        if dist[i][j] == "B":
            br, bc = i, j

q.append((rr, rc, br, bc, 1))
visited.add((rr, rc, br, bc))


def move(r, c, di, dj):
    while True:
        nr = r + di
        nc = c + dj
        if dist[nr][nc] == "#":
            return r, c
        if dist[nr][nc] == "O":
            return nr, nc
        r = nr
        c = nc


flag = False
while q:
    rr, rc, br, bc, cnt = q.popleft()
    if cnt == 11 or flag:
        break
    for k in range(4):
        nrr, nrc = move(rr, rc, dr[k], dc[k])
        nbr, nbc = move(br, bc, dr[k], dc[k])
        if nrr == nbr and nrc == nbc and dist[nrr][nrc] != "O":
            if k == 0:
                if rc > bc:
                    nbc -= dc[k]
                else:
                    nrc -= dc[k]
            elif k == 1:
                if rc > bc:
                    nrc -= dc[k]
                else:
                    nbc -= dc[k]
            elif k == 2:
                if rr > br:
                    nrr -= dr[k]
                else:
                    nbr -= dr[k]
            else:
                if rr > br:
                    nbr -= dr[k]
                else:
                    nrr -= dr[k]

        if (nrr, nrc, nbr, nbc) not in visited and dist[nrr][nrc] != "O" and dist[nbr][nbc] != "O":
            visited.add((nrr, nrc, nbr, nbc))
            q.append((nrr, nrc, nbr, nbc, cnt + 1))

        if dist[nrr][nrc] == "O" and dist[nbr][nbc] != "O":
            flag = True
            break

if flag:
    print(1)
else:
    print(0)
